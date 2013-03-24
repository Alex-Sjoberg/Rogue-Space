import pygame,inventory,item,tile
import data as g

class Environ():
    def __init__(self,type,bg=(0,0,0),fg = (255,255,255), inv = None):
        
        self.inventory = inv
        self.type = type
        if type == g.E.WALL1:
            self.char = "\u0114"
            bg = (100,100,100)
        elif type == g.E.FLOOR:
            self.char = "\u00B7"
            bg = (140,140,140)
            fg = (0,0,0)
            self.inventory = inventory.Inventory(self,item.Item())
        elif type == g.E.SPACE:
            self.char = "."
        else:
            bg = (0,0,0)
            self.char = "?"
                   
        self.tile = tile.Tile(character = self.char , bg = bg , fg = fg)



