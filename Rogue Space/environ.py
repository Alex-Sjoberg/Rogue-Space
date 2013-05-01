import pygame,inventory,item,tile,random
import component as comp
import data as g

class Environ():
    def __init__(self,type,bg=g.BLACK,fg = g.WHITE, inv = None, component = None, owner = None):
        
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
        elif type == g.E.STRUP:
            self.char = "<"
            self.walkable = True
        elif type == g.E.STRDN:
            self.char = ">"        
            self.walkable = True
            
        elif type == g.E.SPACE:
            x = random.randrange(100)
            if x <= 90:
                self.char = " "
            elif x < 93:
                self.char = "."
            elif x < 96:
                self.char = ","
            elif x < 99:
                self.char = "'"
            else:
                self.char = "*"

        elif type == g.E.LASER:
            self.char = " "
            self.component = comp.Component(type = g.C.LASER,owner = owner)
        elif type == g.E.CTRLS:
            self.char = "\u002B"
            self.component = comp.Component(type = g.C.CONTROL,owner = owner)
        elif type == g.E.ENGNE:
            self.char = " "
            self.component = comp.Component(type = g.C.ENGINE,owner = owner)
        elif type == g.E.SNSOR:
            self.char = "\u002B"
            self.component = comp.Component(type = g.C.SENSOR,owner = owner)
        elif type == g.E.MANUV:
            self.char = " "
            self.component = comp.Component(type = g.C.MANEUVER,owner = owner)

        else:
            self.bg = (0,0,0)
            self.char = "?"
            
           
        self.tile = tile.Tile(character = self.char , bg = self.bg , fg = self.fg)
        
    def activate(self):
        if self.component:
            self.component.execute()
        



