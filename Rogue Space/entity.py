'''
Created on Mar 12, 2013

@author: asjoberg
'''
import misc,tile
import data as g

class Entity():
    def __init__(self,ship = g.CURSHIP,xPos = None , yPos = None):
        self.tile = tile.Tile(character = "X")
        self.ship = ship
        if xPos:
            self.xPos = xPos
        else:
            self.xPos = ship.width//2
        if yPos:
            self.yPos = yPos
        else:
            self.yPos = ship.height//2
        self.pos = self.tile.image.get_rect().move(g.Xt//2*(g.FONTSIZE//2),g.Yt//2*g.FONTSIZE)
        g.SCREEN.blit(self.tile.image,self.pos)
        self.xDisp = self.xPos
        self.yDisp = self.yPos
            
    def attack(self,target):
        misc.log("Hi-yah!")

    def move(self,direction):
        
            g.SCREEN.fill((0,0,0),self.pos)
            g.SCREEN.blit(self.ship.map[self.yPos][self.xPos].tile.image , self.pos)
            
            if direction == "UP":
                if self.yPos == 0:
                    misc.logNow("Can't move there")
                elif self.onEdge("y",-1):
                    self.pos=self.pos.move(0,-g.FONTSIZE)
                    self.yPos-=1                    
                else:
                    self.yPos-=1
                    self.yDisp-=1
    
            elif direction == "DOWN":
                if self.yPos == len(self.ship.map)-1:
                    misc.logNow("Can't move there")
                elif self.onEdge("y",+1):
                    self.pos=self.pos.move(0,g.FONTSIZE)
                    self.yPos+=1                    
                else:
                    self.yPos+=1
                    self.yDisp+=1
                
            elif direction == "LEFT":
                if self.xPos == 0:
                    misc.logNow("Can't move there")
                elif self.onEdge("x",-1):
                    self.xPos-=1
                    self.pos=self.pos.move(-g.FONTSIZE//2,0)                    
                else:
                    self.xPos-=1
                    self.xDisp-=1
                
            elif direction == "RIGHT":
                if self.xPos == len(self.ship.map[0])-1:
                    misc.logNow("Can't move there")  
                elif self.onEdge("x",+1):
                    self.xPos+=1
                    self.pos=self.pos.move(g.FONTSIZE//2,0)                    
                else:
                    self.xPos+=1
                    self.xDisp+=1
                   
            #g.SCREEN.blit(self.tile.image, self.pos)
            
    def chooseDir(self,key):
        if key == 273:
            dir = "UP"
        elif key == 274:
            dir = "DOWN"
        elif key == 276:
            dir = "LEFT"
        elif key == 275:
            dir = "RIGHT"
        return dir
    
    def onEdge(self,axis,direct):
        if axis == "x":
            if ((self.xPos - g.Xt//2) <= 0 or (self.xPos +g.Xt//2) >= len(self.ship.map[0])) and ((self.xPos - g.Xt//2 +direct) <= 0 or (self.xPos +g.Xt//2 +direct) >= len(self.ship.map[0])):
                return True
            return False
        else:
            if ((self.yPos -g.Yt//2) <= 0 or (self.yPos + g.Yt//2 ) >= len(self.ship.map)-1) and ((self.yPos -g.Yt//2+direct) <= 0 or (self.yPos + g.Yt//2 + direct) >= len(self.ship.map)-1):
                return True
            return False