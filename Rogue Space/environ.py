import pygame,inventory,item,tile,random
import component as comp
import data as g
from component import Component

class Environ():
    def __init__(self,type,bg=g.BLACK,fg = g.WHITE, inv = None, component = None, owner = None):
        
        self.inventory = inv
        self.type = type
        
        self.walkable = False
        self.component = component
        self.owner = owner
        
        if type == g.E.WALL1:
            char = "\u0114"
            bg = g.DGREY
        elif type == g.E.FLOOR:
            char = "\u002B"
            bg = g.GREY
            fg = g.BLACK
            self.walkable = True
            ##self.inventory = inventory.Inventory(self,item.Item(),item.Item())
        elif type == g.E.STRUP:
            char = "<"
            self.walkable = True
        elif type == g.E.STRDN:
            char = ">"        
            self.walkable = True
            
        elif type == g.E.SPACE:
            x = random.randrange(100)
            if x <= 90:
                char = " "
            elif x < 93:
                char = "."
            elif x < 96:
                char = ","
            elif x < 99:
                char = "'"
            else:
                char = "*"

        elif type == g.E.LASER:
            char = " "
            self.component = comp.Component(type = g.C.LASER,owner = owner)
        elif type == g.E.CTRLS:
            char = "\u002B"
            self.component = comp.Component(type = g.C.CONTROL,owner = owner)
        elif type == g.E.ENGNE:
            char = " "
            self.component = comp.Component(type = g.C.ENGINE,owner = owner)
        elif type == g.E.SNSOR:
            char = "\u002B"
            self.component = comp.Component(type = g.C.SENSOR,owner = owner)
        elif type == g.E.MANUV:
            char = " "
            self.component = comp.Component(type = g.C.MANEUVER,owner = owner)

        else:
            bg = (0,0,0)
            char = "?"
            
        self.tile = tile.Tile(character = char, bg = bg , fg = fg)
        
    def add_component(self,type):
        self.component = comp.Component(type = type , owner = self.owner)  
         
    def activate(self):
        if self.component:
            self.component.execute()
            
    def pre_pickle(self):
        self.tile.pre_pickle()
        if self.component:
            self.component.pre_pickle()
    
    def unpickle(self):
        self.tile.unpickle()
        if self.component:
            self.component.unpickle()
        



