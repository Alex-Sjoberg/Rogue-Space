'''
Created on Mar 17, 2013

@author: asjoberg
'''
import pygame
import data as g


class Tile():
    def __init__(self,character = "?", bg = (0,0,0) , fg = (255,255,255) ,  fontsize = g.FONTSIZE):
        self.char = character
        
        fontObj = pygame.font.Font(g.FONTNAME,fontsize).render(self.char,False,fg,bg)
        self.image = pygame.Surface((fontsize//2,fontsize))
        self.image.fill(bg)
        self.image.blit(fontObj,(0,0),(0,0,fontsize//2,fontsize))
        