'''
Created on Apr 15, 2013

@author: asjoberg
'''
import pygame,misc
import data as g
class MessageLog(): ##NEED TO PASS IN WIDTH AND SUCH
    def __init__(self,startx,starty,width,height,fontsize):
        self.width = width
        self.height = height
        self.xstart = startx
        self.ystart = starty
        self.pending = []
        self.history = []
        self.image = pygame.Surface( (width,height) )
#LOGDISP = pygame.Surface( ((Xt*FONTSIZE)//2 - 2 , FONTSIZE*6 - 2) )

    def log(self, newMessage):
        self.pending.append(newMessage)

    def logNow(self,newMessage):
        self.pending.append(newMessage)
        self.processMessages()

    def processMessages(self):
        if len(self.pending) == 0:
            self.display()
            return
        self.pending = logLines(self.pending)
        numLines = len(self.pending)
        ystart = self.image.get_height() - g.FONTSIZE
    
##Keep going until out of new lines to display
        while True:
            self.image.fill(g.BLACK) #blank the message log
            yoffset = 0    
            available = 6
            numLines = len(self.pending) #see how many new lines need to be displayed
            
            if numLines > available:#if its more than a single screen
                
                self.history += self.pending[:available - 1]#add appropriate number to 
                self.pending = self.pending[available - 1:]
                self.history.append("--More--")
                
                for i in range(1, available+1 if len(self.history) >= available else len(self.history)+1):
                    misc.printText(self.history[-i], "Courier", g.MSGSIZE, 0, ystart + yoffset, surface = self.image)
                    yoffset -= g.FONTSIZE
                
                self.display()
                pygame.display.update()
                
                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            waiting = False        
                
            else: 
                self.history += self.pending
                self.pending.clear()
                for i in range(1, available+1 if len(self.history) >= available else len(self.history)+1):
                    misc.printText(self.history[-i], "Courier", g.MSGSIZE, 0, ystart + yoffset, surface = self.image)
                    yoffset -= g.FONTSIZE  
                self.display()
                pygame.display.update()               
                break
              
            if len(self.pending) == 0:
                break 

        
    
    def prompt(self, promptString):
        inputString = ""
        inputSurface = pygame.Surface( (self.image.get_width(), g.MSGSIZE) )
        self.logNow(promptString)
        inputStart = (len(promptString) +4) * (g.MSGSIZE//2)
        
        while True:
            misc.redraw(g.PLAYER.xDisp, g.PLAYER.yDisp, g.CURSHIP)
            pygame.display.update()        
            
            for newEvent in pygame.event.get():
                if newEvent.type == pygame.KEYDOWN:
                    if newEvent.key == 8:
                        if len(inputString) != 0:
                            inputString = inputString [:-1]  
                    elif newEvent.key == 13:
                        self.history[-1] += inputString
                        print("Exiting")
                        return inputString
                    else:
                        inputString += (newEvent.unicode)
                    inputSurface.fill(g.BLACK)
                    misc.printText(inputString, "Courier", g.MSGSIZE, 0,0 , g.WHITE, surface = inputSurface)
                    self.image.blit(inputSurface, (inputStart,self.image.get_height() - g.FONTSIZE) )
    
                    
    def display(self):
        g.SCREEN.blit(self.image , (self.xstart,self.ystart))
    
def logLines(messages):
    logLines = []
    #maxLineLen = (g.LOGDISP.get_width() // g.MSGSIZE)
    maxLineLen = 67
    for line in messages:
        while len(line) // (maxLineLen+1) != 0:
            logLines.append(line[:maxLineLen-1])
            line = line[maxLineLen:]
        logLines.append(line)
    return logLines

def displayLog():
    g.LOG.processMessages()

def displayUI():
    pygame.draw.line(g.SCREEN, g.WHITE, (0, (g.Yt)*g.FONTSIZE), ((g.Xt)*g.FONTSIZE//2, (g.Yt)*g.FONTSIZE), 2)
    pygame.draw.line(g.SCREEN, g.WHITE, ((g.Xt)*g.FONTSIZE//2, 0), ((g.Xt)*g.FONTSIZE//2, g.height), 2)
    displayLog()
    
class InputBox():
    def __init__(self,xPos,yPos,length,height = g.MSGSIZE):
        self.xPos = xPos
        self.yPos = yPos
        
        
    def getInput(self,prompt = ""):
        for newEvent in pygame.event.get():
            if newEvent.type == pygame.KEYDOWN:
                if newEvent.key == 8:
                    if len(self.string) != 0:
                        self.string = self.string [:-1]
