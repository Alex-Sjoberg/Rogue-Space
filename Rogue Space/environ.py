class Environ():
    def __init__(self,char,bg=(0,0,0),fg = (255,255,255)):
        self.char = char
        if char == "\u0114":
            bg = (100,100,100)
        elif char == "\u00B7":
            bg = (140,140,140)
            fg = (0,0,0)
        else:
            bg = (0,0,0)
        self.bg = bg
        fontObj = pygame.font.Font(FONTNAME,FONTSIZE).render(char,False,fg,bg)
        self.image = Surface((FONTSIZE//2,FONTSIZE))
        self.image.fill(bg)
        self.image.blit(fontObj,(0,0),(0,0,FONTSIZE//2,FONTSIZE))


