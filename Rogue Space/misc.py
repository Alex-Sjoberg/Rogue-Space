'''
Created on Mar 10, 2013

@author: asjoberg
'''
import data as g
import entity


def displayMap(playerX,playerY):
##    debugMapDisplay()
    g.SCREEN.fill((0,0,0))
    for y in range(g.Yt):
        for x in range(g.Xt):
##            print (playerY, Yt//2, playerX)
            displayAt(playerX-g.Xt//2 +x, playerY-g.Yt//2 +y,x,y)

def displayAt(xTile,yTile,x,y):
##    print(yTile,xTile,x,y , )
    if isinstance(g.ENTS[yTile][xTile] , entity.Entity):
        g.SCREEN.blit(g.ENTS[yTile][xTile].image,(x*g.FONTSIZE//2,y*g.FONTSIZE))
    else:
        g.SCREEN.blit(g.playMap[yTile][xTile].image,(x*g.FONTSIZE//2,y*g.FONTSIZE))
    
def debugMapDisplay():
    for i in range (len(g.playMap)):
        print()
        for j in range(len(g.playMap[15])):
            print(g.playMap[i][j].char,end = '')
            
def checkMove(direction,x,y):
    
    if direction == "UP":
        if y == 0 or g.playMap[y-1][x].char not in g.WALKABLES:
            return False
    elif direction == "DOWN":
        if y == len(g.playMap) or g.playMap[y+1][x].char not in g.WALKABLES:
            return False
    elif direction == "LEFT":
        if x == 0 or g.playMap[y][x-1].char not in g.WALKABLES:
            return False
    elif direction == "RIGHT":
        if x == len(g.playMap[0]) or g.playMap[y][x+1].char not in g.WALKABLES:
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
