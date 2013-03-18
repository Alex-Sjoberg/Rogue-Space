'''
Created on Mar 17, 2013

@author: asjoberg
'''
import pygame
import data as g

class Tile():
    def __init__(self,character = "?", bg = (0,0,0) , fg = (255,255,255)):
        self.char = character
        
        fontObj = pygame.font.Font(g.FONTNAME,g.FONTSIZE).render(self.char,False,fg,bg)
        self.image = pygame.Surface((g.FONTSIZE//2,g.FONTSIZE))
        self.image.fill(bg)
        self.image.blit(fontObj,(0,0),(0,0,g.FONTSIZE//2,g.FONTSIZE))
        