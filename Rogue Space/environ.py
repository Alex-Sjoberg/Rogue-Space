import pygame
import data as g

class Environ():
    def __init__(self,type,bg=(0,0,0),fg = (255,255,255)):
        self.type = type
        if type == g.E.WALL1:
            self.char = "\u0114"
            bg = (100,100,100)
        elif type == g.E.FLOOR:
            self.char = "\u00B7"
            bg = (140,140,140)
            fg = (0,0,0)
        elif type == g.E.SPACE:
            self.char = "."
        else:
            bg = (0,0,0)
            self.char = "?"
        self.bg = bg       
        fontObj = pygame.font.Font(g.FONTNAME,g.FONTSIZE).render(self.char,False,fg,bg)
        self.image = pygame.Surface((g.FONTSIZE//2,g.FONTSIZE))
        self.image.fill(bg)
        self.image.blit(fontObj,(0,0),(0,0,g.FONTSIZE//2,g.FONTSIZE))


