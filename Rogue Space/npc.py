'''
Created on Mar 10, 2013

@author: asjoberg
'''
import data as g
import pygame,misc,entity,tile

class NPC():
    def __init__(self,Ntype,xPos,yPos,zPos,ship):
        self.ship=ship
        self.Ntype = Ntype
        self.xPos = xPos
        self.yPos = yPos
        self.zPos = zPos
        self.action_points = 0
        
        self.ship.entMap[self.zPos][self.yPos][self.xPos] = self
        
        if Ntype == g.N.CREWMAN:
            self.friendly = True
            self.speed = 50
            self.char = "\u00A9"
            bg = (0,0,0)
            fg = (255,0,0)

        else:
            self.friendly = True
            self.speed = 100
            fg = (0,255,0)
            bg = (0,0,0)
            self.char = "?"
            
        self.bg = bg   
        self.fg = fg
        self.tile = tile.Tile(character = self.char,fg = self.fg, bg = self.bg) 
 

    def take_turn(self):
        if self.move("RIGHT"):
            return 100
        elif self.move("LEFT"):
            return 100
        else:
            return 100
        
    def move(self,direction):
        
        if misc.checkMove(direction,self.xPos,self.yPos,self.zPos,self.ship):
            self.ship.entMap[self.zPos][self.yPos][self.xPos] = None
            
            if direction == "RIGHT":
                self.xPos+=1
            elif direction == "LEFT":
                self.xPos-=1
            elif direction == "UP":
                self.yPos-=1
            elif direction == "DOWN":
                self.yPos+=1

            self.ship.entMap[self.zPos][self.yPos][self.xPos] = self
            return True
        
        return False
