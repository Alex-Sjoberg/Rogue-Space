'''
Created on Mar 17, 2013

@author: asjoberg
'''

import pygame,math
import data as g

## TODO split minimap tile from main map tile. Needs to get rid of all this heading and arrow conditional stuff
class Tile():
    def __init__(self,character = "?", bg = (0,0,0) , fg = (255,255,255) ,  fontsize = g.FONTSIZE ,  heading = None , minimap = False):
        
        self.char = character
        self.fontsize = fontsize
        self.bg = bg
        self.fg = fg
        
        #need to remove
        self.minimap = minimap
        self.heading = heading
        
        self.init_image(minimap,heading)

        
    def updateArrow(self,heading):
        self.arrow = DirArrow(heading)
        self.image.fill(self.bg)
        self.image.blit(self.arrow.image , (0,0) )
        self.image.blit(self.fontObj, (self.xmid-self.halfFontXLen,self.ymid-self.halfFontYLen))
        
    def pre_pickle(self):
        self.image = None
    
    def unpickle(self):
        self.init_image(self.minimap, self.heading)
    
    def init_image(self,minimap,heading):
        self.fontObj = pygame.font.Font(g.FONTNAME,self.fontsize).render(self.char,False,self.fg,self.bg)
        
        if minimap or heading:
            self.image = pygame.Surface( (self.fontsize+g.MINIPADDING,self.fontsize+g.MINIPADDING) )
        else:
            self.image = pygame.Surface((self.fontsize//2,self.fontsize))

        self.image.fill(self.bg)
        
        #TODO Heading bad
        if heading:
            self.arrow = DirArrow(heading)
            self.image.blit(self.arrow.image , (0,0))
            
            self.xmid = self.image.get_width()//2
            self.ymid = self.image.get_height()//2
            
            self.halfFontXLen = self.fontObj.get_width()//2
            self.halfFontYLen = self.fontObj.get_height()//2
            
            self.image.blit(self.fontObj,(self.xmid-self.halfFontXLen,self.ymid-self.halfFontYLen))
            
        else:
            self.image.blit(self.fontObj,(0,0),(0,0,self.fontsize//2,self.fontsize))
        
class DirArrow():
    def __init__(self, dir, fontsize = g.MINISIZE):
        self.image = pygame.Surface((fontsize+g.MINIPADDING,fontsize+g.MINIPADDING))
        
        dx = math.cos(math.radians(dir))
        dy = math.sin(math.radians(dir))
        
        xmid = self.image.get_width()//2
        ymid = self.image.get_height()//2
        
        pygame.draw.line(self.image, g.RED, (xmid, ymid),  (xmid + dx*10000 , ymid - dy*10000),  3)
        
        pygame.draw.circle(self.image, g.BLACK, (xmid,ymid), (fontsize + 3)//2, 0)
