'''
Created on May 1, 2013

@author: asjoberg
'''

import pygame, sys,traceback
import data as g
import interface as UI
import ship
import entity
import environ
import misc
import pickle
import loading
import component

class ShipBuilder():
    def __init__(self):
        pygame.init()
        pygame.event.set_allowed([pygame.KEYDOWN,pygame.QUIT])
        self.console = UI.MessageLog(2, 2+ g.Yt*g.FONTSIZE, g.Xt*g.FONTSIZE//2-2, g.FONTSIZE*6 -2,g.MSGSIZE)
        
        self.terrain_list = UI.ItemList(g.Xt*g.FONTSIZE//2 + 5, 5 ,500,1000, toAdd = g.ELIST)
        self.terrain_list.update_display()

        self.commands_list = UI.ItemList(g.Xt*g.FONTSIZE//2 + 5, 5 ,500,1000, toAdd = None)
        self.commands_list.update_display()
        
        self.component_list = UI.ItemList(g.Xt*g.FONTSIZE//2 + 5, 5 ,500,1000, toAdd = g.CLIST)
        self.component_list.update_display()
        
        self.modes = g.enum("TERRAIN" , "COMPONENT" , "LINK")
        self.mode = self.modes.TERRAIN
        
    def create_new_ship(self,width,height,zheight):
        self.ship = ship.Ship(-1)
        self.ship.init_blank_map(width, height, zheight)
    
    def main_loop(self):
        self.cursor = BuildCursor(self.ship)
        self.cursor.set_terrain_type(g.E.WALL1)
        
        while True:
            
            for newEvent in pygame.event.get():
                if newEvent.type == pygame.KEYDOWN:
                    unicode = newEvent.unicode
                    key = newEvent.key
                    print(key)
                    if key in [273,274,275,276]:
                        dir = self.cursor.chooseDir(key)
                        self.cursor.move(dir)
                    elif unicode == "<":
                        self.cursor.ascend()  
                    elif unicode == ">":
                        self.cursor.descend()
                    elif key == 13:
                        if self.mode == self.modes.TERRAIN:
                            self.cursor.place_terrain()
                        elif self.mode == self.modes.COMPONENT:
                            self.cursor.place_component()
                        elif self.mode == self.modes.LINK:
                            try:
                                self.cursor.link_component()
                            except:
                                self.console.logNow("No component there")
                    elif unicode == "t":
                        self.change_terrain_type()
                        self.set_mode(self.modes.TERRAIN)
                    elif unicode == "c":
                        self.change_component_type()
                        self.set_mode(self.modes.COMPONENT)
                    elif unicode == "l":
                        self.set_mode(self.modes.LINK)
                        self.logNow("Choose item you would like to link to a control panel")
                    elif unicode == "w":
                        self.save_ship()
                    elif unicode == " ":
                        self.cursor = None
                        return 0
                    elif unicode == "o":
                        self.load_ship()
                    misc.displayMap(self.cursor.xDisp,self.cursor.yDisp,self.cursor.zPos,self.ship)
                    g.SCREEN.blit(self.cursor.tile.image, self.cursor.pos)
                    self.commands_list.display()
                    pygame.display.update()
                    
    def change_terrain_type(self):
        self.terrain_list.display()
        while True:
            for newEvent in pygame.event.get():
                if newEvent.type == pygame.KEYDOWN:
                    unicode = newEvent.unicode
                    newType = self.terrain_list.get_value(unicode)
                    if newType:
                        self.cursor.set_terrain_type(eval("g.E." + str(newType)))
                        return
                    else:
                        self.console.logNow("Not a valid terrain type")
                        return
                    
    def change_component_type(self):
        self.component_list.display()
        while True:
            for newEvent in pygame.event.get():
                if newEvent.type == pygame.KEYDOWN:
                    unicode = newEvent.unicode
                    newType = self.component_list.get_value(unicode)
                    if newType:
                        self.cursor.set_component_type(eval("g.C." + str(newType)))
                        return
                    else:
                        self.console.logNow("Not a valid component type")
                        return
                    
    def set_mode(self,mode):
        self.mode = mode
                    
    def save_ship(self):
        shipName = self.console.prompt("Save ship as:")      
        if shipName == "":
            self.console.logNow("Cancelled saving")
        else:
            loading.save_ship(self.ship,shipName)

            
    def load_ship(self):
        
        filename = g.LOG.prompt("Load what file? ")
        try:
            self.ship = loading.load_ship(filename)
        except FileNotFoundError :
            g.LOG.logNow("File not found")
            
              
class BuildCursor(entity.Entity):
    def __init__(self,ship):
        super().__init__(ship = ship)
        self.terrain_type = None
        self.component_type = None
        self.link1 = None
        self.link2 = None
    
    def set_terrain_type(self,newType):
        self.terrain_type = newType
           
    def place_terrain(self):
        self.ship.map[self.zPos][self.yPos][self.xPos] = environ.Environ(self.terrain_type)
        
    def set_component_type(self,newType):
        self.component_type = newType  
        
    def place_component(self):
        self.ship.map[self.zPos][self.yPos][self.xPos].add_component(self.component_type)
        
    def link_component(self):
        if not self.link1: #Selecting first component
            self.link1 = self.ship.map[self.zPos][self.yPos][self.xPos].component
        elif not self.link2:#selecting second component
            self.link2 = self.ship.map[self.zPos][self.yPos][self.xPos].component
        
        if self.link1 and self.link2:
            self.link2.action.link
            
if __name__ == "__main__":
    sbuilder = ShipBuilder()
    sbuilder.create_new_ship(50, 25, 3)
    #sbuilder.load_ship()
    sbuilder.main_loop()
    