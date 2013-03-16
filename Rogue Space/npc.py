'''
Created on Mar 10, 2013

@author: asjoberg
'''
import data as g
import pygame,misc,entity

class NPC(entity.Entity):
    def __init__(self,Ntype,xPos,yPos):
        self.Ntype = Ntype
        self.xPos = xPos
        self.yPos = yPos
        self.action_points = 0
        
        g.ENTS[yPos][xPos] = self
        
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
            
        fontObj = pygame.font.Font(g.FONTNAME,g.FONTSIZE).render(self.char,False,fg,bg)
        self.image = pygame.Surface((g.FONTSIZE//2,g.FONTSIZE))
        self.image.fill(bg)
        self.image.blit(fontObj,(0,0),(0,0,g.FONTSIZE//2,g.FONTSIZE))

    def take_turn(self):
        if self.move("RIGHT"):
            return 100
        else:
            return 100
        
    def move(self,direction):
        
        if misc.checkMove(direction,self.xPos,self.yPos):
            g.ENTS[self.yPos][self.xPos] = None
            
            if direction == "RIGHT":
                self.xPos+=1
            elif direction == "LEFT":
                self.xPos-=1
            elif direction == "UP":
                self.yPos-=1
            elif direction == "DOWN":
                self.yPos+=1

            g.ENTS[self.yPos][self.xPos] = self
            return True
        
        return False
