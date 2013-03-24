import pygame,inventory,item,tile
import component as comp
import data as g

class Environ():
    def __init__(self,type,bg=g.BLACK,fg = g.WHITE, inv = None, component = None):
        
        self.inventory = inv
        self.type = type
        self.bg = bg
        self.fg = fg
        self.walkable = False
        self.component = component
        if type == g.E.WALL1:
            self.char = "\u0114"
            self.bg = g.DGREY
        elif type == g.E.FLOOR:
            self.char = "\u002B"
            self.bg = g.GREY
            self.fg = g.BLACK
            self.walkable = True
            ##self.inventory = inventory.Inventory(self,item.Item(),item.Item())
        elif type == g.E.SPACE:
            self.char = "."
        elif type == g.E.LASER:
            self.char = "\u002B"
            self.component = comp.Component(type = g.C.LASER)
        elif type == g.E.CTRLS:
            self.char = "\u002B"
            self.component = comp.Component(type = g.C.CONTROL, fireable = comp.Fireable)
        else:
            self.bg = (0,0,0)
            self.char = "?"
                   
        self.tile = tile.Tile(character = self.char , bg = self.bg , fg = self.fg)
        
    def activate(self):
        if self.component:
            self.component.execute()
        



