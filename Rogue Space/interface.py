'''
Created on Apr 15, 2013

@author: asjoberg
'''
import pygame,misc
import data as g
import queue
class MessageLog(): ##NEED TO PASS IN WIDTH AND SUCH
    def __init__(self,startx,starty,width,height,fontsize = g.MSGSIZE):
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
            self.display()
            pygame.display.update()        
            #TODO need input handler class
            for newEvent in pygame.event.get():
                if newEvent.type == pygame.KEYDOWN:
                    if newEvent.key == 8:
                        if len(inputString) != 0:
                            inputString = inputString [:-1]  
                    elif newEvent.key == 13:
                        self.history[-1] += inputString
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
    
class ItemList():
    def __init__(self, xstart, ystart, width, height ,font = g.FONTNAME, fontsize = g.MSGSIZE, toAdd = [], **itemDict):
        self.letters1 = queue.PriorityQueue(26)
        self.letters2 = queue.PriorityQueue(26)
        
        self.xstart = xstart
        self.ystart = ystart  
        self.width = width
        self.height = height
        self.font = font
        self.fontsize = fontsize
        self.surface = pygame.Surface( (self.width,self.height) )  
        
        for i in "abcdefghijklmnopqrstuvwxyz": 
            self.letters1.put(i)
        for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.letters2.put(i)
         
        self.usedLetters = []
        self.items = {}
        print("items to be added are:" , toAdd)
        if toAdd:
            for item in toAdd:
                self.addItem(item)
    
    def addItem(self,item,mapping = None):
        '''
        if mapping: ##TODO: add support for explicit item assignment
            if :
                self.items[mapping] = item
                self.usedLetters += list(mapping)
        '''
                
        if not self.letters1.empty():
            newLetter = self.letters1.get()
            self.items[newLetter] = item
            self.usedLetters += list(newLetter)
            return True
        elif not self.letters2.empty():
            newLetter = self.letters2.get()
            self.items[newLetter] = item
            self.usedLetters += list(newLetter)
        else:
            return False
            print("Error, adding to full inventory")
        
    def getItem(self,key):
        ret = self.items.pop(key)
        self.usedLetters.remove(key)
        if (len(self.items) == 0):
            self.owner.inventory = None
            
        return ret
    
    def get_value(self,key):
        try:
            return self.items[key]
        except:
            return None
        
    def isFull(self):
        return self.letters1.empty() and self.letters2.empty()
    
    def peek(self):
        return self.items[self.usedLetters[0]]
        
      
    def getKeys(self):
        return self.items.keys()
    
    def display(self):
        g.SCREEN.blit(self.surface, (self.xstart,self.ystart) )
        pygame.display.update()
        
    def examine(self):
        self.displayItems()
        
        while True:
            g.CLOCK.tick(60)
            for newEvent in pygame.event.get():
                if newEvent.type == pygame.KEYDOWN:
                    key = newEvent.unicode
                    if key in self.usedLetters:
                        self.items[key].displayDescription()
                        self.displayItems()
                    elif key ==" ":
                        return
                    
    def update_display(self):
        self.surface.fill(g.BLACK)
        keys = list(self.items.keys())
        keys.sort()
        print("keys are" , keys)
        
        xoffset = yoffset = 0
        
        for key in keys:
            if yoffset >= 19 * (self.fontsize+5):
                yoffset = 0
                xoffset += (22 * (self.fontsize//2)) + 5
            misc.printText("- " + key, self.font, self.fontsize,  xoffset,  yoffset, surface = self.surface)
            
            if type(self.items[key]) == str:
                itemName = self.items[key]
            else:
                itemName = self.items[key].name
                
            if len(itemName) > 20:
                itemName = itemName [:-3] + "..."
            print("printing:" , itemName)
            misc.printText(itemName, self.font, self.fontsize, xoffset + self.fontsize, yoffset,surface = self.surface)
            yoffset += self.fontsize + 5
    
    
    
class Input_Handler():
    
    def __init__(self):
        self.action_dict = {}
        pass
    
    def handle(self):
        pass
    
    
    
'''   
class InputBox():
    def __init__(self,xPos,yPos,length,height = g.MSGSIZE,promptString = ""):
        self.xPos = xPos
        self.yPos = yPos
        self.length = length
        self.height = height
        self.promptString = promptString
        
        
    def getInput(self):
        inputString = ""
        inputSurface = pygame.Surface( (self.width, g.MSGSIZE) )
        
        for newEvent in pygame.event.get():
            if newEvent.type == pygame.KEYDOWN:
                if newEvent.key == 8:
                    if len(self.string) != 0:
                        self.string = self.string [:-1]
    '''