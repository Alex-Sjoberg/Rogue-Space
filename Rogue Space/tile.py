'''
Created on Mar 17, 2013

@author: asjoberg
'''

import pygame,math,random
import data as g



class Tile():
    def __init__(self,character = "?", bg = (0,0,0) , fg = (255,255,255) ,  fontsize = g.FONTSIZE ,  heading = None , minimap = False):
        
        self.char = character
        self.fontsize = fontsize
        self.fontObj = pygame.font.Font(g.FONTNAME,fontsize).render(self.char,False,fg,bg)
        
        if minimap or heading:
            self.image = pygame.Surface( (fontsize+g.MINIPADDING,fontsize+g.MINIPADDING) )
        else:
            self.image = pygame.Surface((fontsize//2,fontsize))

        self.bg= bg
        self.image.fill(self.bg)
        
        if heading:
            self.arrow = DirArrow(heading)
            self.image.blit(self.arrow.image , (0,0))
            
            self.xmid = self.image.get_width()//2
            self.ymid = self.image.get_height()//2
            
            self.halfFontXLen = self.fontObj.get_width()//2
            self.halfFontYLen = self.fontObj.get_height()//2
            
            self.image.blit(self.fontObj,(self.xmid-self.halfFontXLen,self.ymid-self.halfFontYLen))
            
        else:
            self.image.blit(self.fontObj,(0,0),(0,0,fontsize//2,fontsize))
        
    def updateArrow(self,heading):
        self.arrow = DirArrow(heading)
        self.image.fill(self.bg)
        self.image.blit(self.arrow.image , (0,0) )
        self.image.blit(self.fontObj, (self.xmid-self.halfFontXLen,self.ymid-self.halfFontYLen))
        
class DirArrow():
    def __init__(self, dir, fontsize = g.MINISIZE):
        self.image = pygame.Surface((fontsize+g.MINIPADDING,fontsize+g.MINIPADDING))
        
        dx = math.cos(math.radians(dir))
        dy = math.sin(math.radians(dir))
        
        xmid = self.image.get_width()//2
        ymid = self.image.get_height()//2
        
        pygame.draw.line(self.image, g.RED, (xmid, ymid),  (xmid + dx*10000 , ymid - dy*10000),  3)
        
        pygame.draw.circle(self.image, g.BLACK, (xmid,ymid), (fontsize + 3)//2, 0)
