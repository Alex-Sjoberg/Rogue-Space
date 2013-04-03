'''
Created on Mar 10, 2013

@author: asjoberg
'''
import data as g
import entity,pygame
import math


def displayMap(playerX,playerY, ship = g.CURSHIP):
##    debugMapDisplay()
    print(g.CURSHIP)
    g.MAPDISP.fill((0,0,0))
    for y in range(g.Yt):
        for x in range(g.Xt):
##            print (playerY, Yt//2, playerX)
            displayAt(playerX-g.Xt//2 +x, playerY-g.Yt//2 +y,x,y,ship)
    displayUI()

def displayAt(xTile,yTile,x,y,ship):
##    print(yTile,xTile,x,y , )
    if isinstance(ship.entMap[yTile][xTile] , entity.Entity):
        g.SCREEN.blit(ship.entMap[yTile][xTile].tile.image,(x*g.FONTSIZE//2,y*g.FONTSIZE))
    elif ship.map[yTile][xTile].component:
        g.SCREEN.blit(ship.map[yTile][xTile].component.tile.image,(x*g.FONTSIZE//2,y*g.FONTSIZE))
    elif ship.map[yTile][xTile].inventory:
        g.SCREEN.blit(ship.map[yTile][xTile].inventory.peek().tile.image,(x*g.FONTSIZE//2,y*g.FONTSIZE))
    else:
        g.SCREEN.blit(ship.map[yTile][xTile].tile.image,(x*g.FONTSIZE//2,y*g.FONTSIZE))
    
def debugMapDisplay(ship):
    for i in range (len(ship.map)):
        print()
        for j in range(len(ship.map[15])):
            print(ship.map[i][j].char,end = '')
            
def checkMove(direction,x,y,ship):
    
    if direction == "UP":
        if y == 0 or not ship.map[y-1][x].walkable:
            return False
    elif direction == "DOWN":
        if y == len(ship.map) or not ship.map[y+1][x].walkable:
            return False
    elif direction == "LEFT":
        if x == 0 or not ship.map[y][x-1].walkable:
            return False
    elif direction == "RIGHT":
        if x == len(ship.map[0]) or not ship.map[y][x+1].walkable:
            return False
    return True

def checkOccupied(direction,x,y,ship):
    
    if direction == "UP":
        target = ship.entMap[y-1][x]
    elif direction == "DOWN":
        target = ship.entMap[y+1][x]
    elif direction == "LEFT":
        target = ship.entMap[y][x-1]
    elif direction == "RIGHT":
        target = ship.entMap[y][x+1]
        
    if isinstance(target, entity.Entity):
        return target
    else:
        return None

def printText(txtText, Textfont, Textsize , Textx, Texty, Textcolor = (255,255,255),surface = g.SCREEN):
    myfont = pygame.font.SysFont(Textfont, Textsize)
    label = myfont.render(txtText, 1, Textcolor)
    surface.blit(label, (Textx, Texty))

def printComponents():
    for comp in g.COMPLIST:
        print(comp," ",comp.name)
        
def log(newMessage):
    g.MPENDING.append(newMessage)

def logNow(newMessage):
    g.MPENDING.append(newMessage)
    processMessages()

def processMessages():
    print("messages")
    if len(g.MPENDING) == 0:
        displayLog()
        return
    g.MPENDING = logLines(g.MPENDING)
    numLines = len(g.MPENDING)
    ystart = g.LOGDISP.get_height() - g.FONTSIZE
    
##Keep going until out of new lines to display
    while True:
        g.LOGDISP.fill(g.BLACK) #blank the message log
        yoffset = 0    
        available = 6
        numLines = len(g.MPENDING) #see how many new lines need to be displayed
        
        if numLines > available:#if its more than a single screen
            
            print("Pending:" , g.MPENDING)
            g.MHISTORY += g.MPENDING[:available - 1]#add appropriate number to 
            g.MPENDING = g.MPENDING[available - 1:]
            g.MHISTORY.append("--More--")
            
            for i in range(1, available+1 if len(g.MHISTORY) >= available else len(g.MHISTORY)+1):
                print(i," From history",g.MHISTORY[-i])
                printText(g.MHISTORY[-i], "Courier", g.MSGSIZE, 0, ystart + yoffset, surface = g.LOGDISP)
                yoffset -= g.FONTSIZE            
            
            displayLog()
            pygame.display.update()
            
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        waiting = False        
            
        else: 
            g.MHISTORY += g.MPENDING
            g.MPENDING.clear()
            for i in range(1, available+1 if len(g.MHISTORY) >= available else len(g.MHISTORY)+1):
                print(i," From history",g.MHISTORY[-i])
                printText(g.MHISTORY[-i], "Courier", g.MSGSIZE, 0, ystart + yoffset, surface = g.LOGDISP)
                yoffset -= g.FONTSIZE  
            displayLog()
            pygame.display.update()               
            break
        
            

              
        if len(g.MPENDING) == 0:
            break 

        
    
def displayUI():
    pygame.draw.line(g.SCREEN, g.WHITE, (0, (g.Yt)*g.FONTSIZE), ((g.Xt)*g.FONTSIZE//2, (g.Yt)*g.FONTSIZE), 2)
    pygame.draw.line(g.SCREEN, g.WHITE, ((g.Xt)*g.FONTSIZE//2, 0), ((g.Xt)*g.FONTSIZE//2, g.height), 2)
    processMessages()
    displayMinimap()
    
def displayLog():
    g.SCREEN.blit(g.LOGDISP , (2,g.Yt*g.FONTSIZE+2))
    
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

def initMinimap():
    for y in range (len(g.MINIMAP)):
        for x in range (len(g.MINIMAP[0])):
            g.MINIDISP.blit( g.MINIMAP[y][x].image , (x*g.MINISIZE//2 , y*g.MINISIZE))
            
    
def displayMinimap():
    print("displaying minimap")
    print(g.Xt*g.FONTSIZE)
    g.SCREEN.blit(g.MINIDISP, (g.Xt*g.FONTSIZE//2 + 5, 2) )
        

def redraw(xPos,yPos,ship):
    displayMap(xPos, yPos, ship)
    displayUI()
    
def distance(p1,p2):
    return math.sqrt( (p2[0] - p1[0])**2 + (p2[1] - p2[1])**2 )

def midpoint(p1,p2):
    return ( ((p1[0]+p2[0]) // 2) , ((p1[1] + p2[1]) // 2) )

def xdif(x1,x2):
    return x2 -x1

def ydif(y1,y2):
    return y2-y1


    