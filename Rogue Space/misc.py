'''
Created on Mar 10, 2013

@author: asjoberg
'''
import data as g
import interface as UI
import entity,pygame
import math


def displayMap(playerX,playerY,playerZ, ship = g.CURSHIP):
##    debugMapDisplay()

    g.MAPDISP.fill((0,0,0))
    for y in range(g.Yt):
        for x in range(g.Xt):
##            print (playerY, Yt//2, playerX)
            displayAt(playerX-g.Xt//2 +x, playerY-g.Yt//2 +y,playerZ, x,y,ship)
    UI.displayUI()##<- BAD, Why displaying UI here???

def displayAt(xTile,yTile,zLvl,x,y,ship):
   # print(zLvl,yTile,xTile)
    if isinstance(ship.entMap[zLvl][yTile][xTile] , entity.Entity):
        g.SCREEN.blit(ship.entMap[zLvl][yTile][xTile].tile.image,(x*g.FONTSIZE//2,y*g.FONTSIZE))
    elif ship.map[zLvl][yTile][xTile].component:
        g.SCREEN.blit(ship.map[zLvl][yTile][xTile].component.tile.image,(x*g.FONTSIZE//2,y*g.FONTSIZE))
    elif ship.map[zLvl][yTile][xTile].inventory:
        g.SCREEN.blit(ship.map[zLvl][yTile][xTile].inventory.peek().tile.image,(x*g.FONTSIZE//2,y*g.FONTSIZE))
    else:
        g.SCREEN.blit(ship.map[zLvl][yTile][xTile].tile.image,(x*g.FONTSIZE//2,y*g.FONTSIZE))
    
def debugMapDisplay(ship):
    for z in range(len(ship.map)):
        print("Level " , z)
        for i in range (len(ship.map[0])):
            print()
            for j in range(len(ship.map[0][15])):
                try:
                    print(ship.map[z][i][j].char,end = '')
                except:
                    print("?",end="")
            
def checkMove(direction,x,y,z,ship):
    
    if direction == "UP":
        if y == 0 or not ship.map[z][y-1][x].walkable:
            return False
    elif direction == "DOWN":
        if y == len(ship.map[0]) or not ship.map[z][y+1][x].walkable:
            return False
    elif direction == "LEFT":
        if x == 0 or not ship.map[z][y][x-1].walkable:
            return False
    elif direction == "RIGHT":
        if x == len(ship.map[0][0]) or not ship.map[z][y][x+1].walkable:
            return False
    return True

def checkOccupied(direction,x,y,z,ship):
    
    if direction == "UP":
        target = ship.entMap[z][y-1][x]
    elif direction == "DOWN":
        target = ship.entMap[z][y+1][x]
    elif direction == "LEFT":
        target = ship.entMap[z][y][x-1]
    elif direction == "RIGHT":
        target = ship.entMap[z][y][x+1]
        
    if isinstance(target, entity.Entity):
        return target
    else:
        return None

def printText(txtText, Textfont, Textsize , Textx, Texty, Textcolor = (255,255,255),surface = g.SCREEN):
    myfont = pygame.font.SysFont(Textfont, Textsize)
    label = myfont.render(txtText, 1, Textcolor)
    surface.blit(label, (Textx, Texty))

def printComponents(ship):
    for comp in ship.components:
        print(comp," ",comp.name)
        
def makeMinimap():
    shipCoords = []
    for ship in g.SHIPS:
        shipCoords.append( (ship.xPos,ship.yPos) )
    mid = midPoint(shipCoords)
    
    for y in range (len(g.MINIMAP)):
        for x in range (len(g.MINIMAP[0])):
            g.MINIDISP.blit( g.MINIMAP[y][x].image , (x*(g.MINISIZE+g.MINIPADDING) , y*(g.MINISIZE+g.MINIPADDING)))
            
    for ship in g.SHIPS:
        ship.updateDirArrow()
        g.MINIDISP.blit( ship.image.image , ( ((g.MXt//2) + (xdif(mid[0],ship.xPos))//100)*(g.MINISIZE+g.MINIPADDING) , ((g.MYt//2) + (ydif(mid[1],ship.yPos))//100)*(g.MINISIZE+g.MINIPADDING) ) )

                
def displayMinimap():
    g.SCREEN.blit(g.MINIDISP, (g.Xt*g.FONTSIZE//2 + 5, 2) )

def redraw(xPos,yPos,zPos,ship):
    displayMap(xPos, yPos,zPos, ship)
    makeMinimap()
    displayMinimap()
    UI.displayUI()
    pygame.display.update()
    
def distance(p1,p2):
    return math.sqrt( (p2[0] - p1[0])**2 + (p2[1] - p2[1])**2 )

def midPoint(points):
    xsum=ysum=0
    for i in range (len(points)):
        xsum += points[i][0]
        ysum += points[i][1]
    return ( (xsum // len(points) , ysum // len(points) ) )

def xdif(x1,x2):
    return x2 -x1

def ydif(y1,y2):
    return y2-y1

def printShips():
    for i  in range(len(g.SHIPS)):
        print(i, g.SHIPS[i].name)
        
def look(ship, startx = None,starty = None, startz = 0):

    g.CURSOR = entity.Entity(ship = ship, xPos = startx , yPos = starty, zPos = startz)
    displayMap(g.CURSOR.xDisp,g.CURSOR.yDisp,g.CURSOR.zPos,g.CURSOR.ship)
    while True:
        for newEvent in pygame.event.get():
            if newEvent.type == pygame.KEYDOWN:
                unicode = newEvent.unicode
                key = newEvent.key
                if key in [273,274,275,276]:
                    dir = g.CURSOR.chooseDir(key)
                    g.CURSOR.move(dir)
                elif unicode == "<":
                    g.CURSOR.ascend()  
                elif unicode == ">":
                    g.CURSOR.descend()
                elif unicode == " ":
                    g.CURSOR = None
                    return 0
                displayMap(g.CURSOR.xDisp,g.CURSOR.yDisp,g.CURSOR.zPos,g.CURSOR.ship)
                g.SCREEN.blit(g.CURSOR.tile.image, g.CURSOR.pos)
                pygame.display.update()
            