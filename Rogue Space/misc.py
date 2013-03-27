'''
Created on Mar 10, 2013

@author: asjoberg
'''
import data as g
import entity,pygame


def displayMap(playerX,playerY):
##    debugMapDisplay()
    g.SCREEN.fill((0,0,0))
    for y in range(g.Yt):
        for x in range(g.Xt):
##            print (playerY, Yt//2, playerX)
            displayAt(playerX-g.Xt//2 +x, playerY-g.Yt//2 +y,x,y)
    displayUI()

def displayAt(xTile,yTile,x,y):
##    print(yTile,xTile,x,y , )
    if isinstance(g.ENTS[yTile][xTile] , entity.Entity):
        g.SCREEN.blit(g.ENTS[yTile][xTile].tile.image,(x*g.FONTSIZE//2,y*g.FONTSIZE))
    elif g.playMap[yTile][xTile].component:
        g.SCREEN.blit(g.playMap[yTile][xTile].component.tile.image,(x*g.FONTSIZE//2,y*g.FONTSIZE))
    elif g.playMap[yTile][xTile].inventory:
        g.SCREEN.blit(g.playMap[yTile][xTile].inventory.peek().tile.image,(x*g.FONTSIZE//2,y*g.FONTSIZE))
    else:
        g.SCREEN.blit(g.playMap[yTile][xTile].tile.image,(x*g.FONTSIZE//2,y*g.FONTSIZE))
    
def debugMapDisplay():
    for i in range (len(g.playMap)):
        print()
        for j in range(len(g.playMap[15])):
            print(g.playMap[i][j].char,end = '')
            
def checkMove(direction,x,y):
    
    if direction == "UP":
        if y == 0 or not g.playMap[y-1][x].walkable:
            return False
    elif direction == "DOWN":
        if y == len(g.playMap) or not g.playMap[y+1][x].walkable:
            return False
    elif direction == "LEFT":
        if x == 0 or not g.playMap[y][x-1].walkable:
            return False
    elif direction == "RIGHT":
        if x == len(g.playMap[0]) or not g.playMap[y][x+1].walkable:
            return False
    return True

def checkOccupied(direction,x,y):
    
    if direction == "UP":
        target = g.ENTS[y-1][x]
    elif direction == "DOWN":
        target = g.ENTS[y+1][x]
    elif direction == "LEFT":
        target = g.ENTS[y][x-1]
    elif direction == "RIGHT":
        target = g.ENTS[y][x+1]
        
    if isinstance(target  , entity.Entity):
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
    #g.MHISTORY.append(newMessage)
    
    printText(newMessage, "Arial" , g.FONTSIZE//2, 0,2, surface = g.LOGDISP)

def processMessages():
    available = 6
    if len(g.MPENDING) == 0:
        return
    else:
        pending = logLines(g.MPENDING)
        numLines = len(pending)
        ystart = g.LOGDISP.get_height()
        yoffset = 0
        for i in range(6 if numLines >= 6 else numLines):
            printText(pending[-i])
        
        
    g.MHISTORY += g.MPENDING
def displayUI():
    g.SCREEN.blit(g.LOGDISP , (0,g.Yt*g.FONTSIZE))
    pygame.draw.line(g.SCREEN, g.WHITE, (0, (g.Yt)*g.FONTSIZE), ((g.Xt)*g.FONTSIZE//2, (g.Yt)*g.FONTSIZE), 2)
    pygame.draw.line(g.SCREEN, g.WHITE, ((g.Xt)*g.FONTSIZE//2, 0), ((g.Xt)*g.FONTSIZE//2, g.height), 2)
    
def logLines(messages):
    logLines = []
    for line in messages:
        while len(line) // 30 != 0:
            logLines.append(line[:30])
            line = line[30:]
        logLines.append(line)
        

def redraw():
    displayMap()
    displayUI()
    