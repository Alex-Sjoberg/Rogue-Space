'''
Created on Mar 21, 2013

@author: asjoberg
'''

import pygame
import tile
import data as g
import misc

class Component():
    def __init__(self,type, *action):
        
        action = list(action)        
        if type == g.C.LASER:
            self.char = "\u0142"
            self.action = Fire(self)
            self.name = "Laser"
            
        elif type == g.C.CONTROL:
            self.char = "\u011f"
            self.action = ActMenu(action)
            self.name = "Control console"
            
        elif type == g.C.ENGINE:
            self.char = "\u00cb"
            self.action = Engine()
            self.name = "Engine"
                
        self.type = type    
        self.tile = tile.Tile(character = self.char)
        
    def execute(self,actionNum = 0):
        return self.action.execute(actionNum)
       

class CAction():
    def __init__(self):
        self.description = "Do nothing"
        self.linkedActions = []
        
    def execute(self,actionNum = 0):
        misc.log("That didn't seem to do anything")
        return 50
    
    def link(self,target,actionNum = 0,description = "Do something"):
        print("CAction linking")
        self.action = Signal(self,target,actionNum,description)
        
            
class Fire(CAction):
    def __init__(self,owner,description = "Fire this weapon"):
        self.owner = owner
        self.description = description
        
    def execute(self,actionNum = 0):
        if actionNum == 0:
            misc.log("I'm firin the laser")
            return 50
        else:
            misc.log("I'm firing the laser heroically")
            return 50
                
class Engine():
    def __init__(self):
        pass
        
    def execute(self,actionNum = 0, *params):
        misc.log("engining")

        return 50
                
class ActMenu(CAction):
    def __init__(self,actions):
        self.actions = actions
        
    def execute(self,actionNum = 0):
        if len (self.actions) == 0:
            misc.log("Its not working!")
            return 0
        if len(self.actions) == 1:
            return self.actions[0].execute()
        else: ##display menu of possible actions
            g.SCREEN.fill((0,0,0))
            startx = 10
            starty = 10
            xoffset = 0
            yoffset = 0
            for i in range (len(self.actions)):
                if yoffset >= 19 * (g.FONTSIZE+5):
                    yoffset = 0
                    xoffset += (32 * (g.FONTSIZE//2)) + 5
                misc.printText("- " + str(i), g.FONTNAME, g.FONTSIZE, startx + xoffset, starty + yoffset)
                description = self.actions[i].description
                if len(description) > 30:
                    description = description [:-3] + "..."
                misc.printText(description, g.FONTNAME, g.FONTSIZE, startx + xoffset + g.FONTSIZE, starty + yoffset)
                yoffset += g.FONTSIZE + 5
        
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.unicode == " ":
                            return 0
                        elif event.unicode in "1023456789":
                            return self.actions[int(event.unicode)].execute()
        
    def link(self,target,actionNum = 0,description = "Do something"):
        self.actions.append(Signal(self,target,actionNum,description = description))
        print(self.actions)
        
class Signal(CAction):
    def __init__(self,owner,target,actionNum = 0,description = "Do something"):
        self.owner = owner
        self.target = target
        self.actionNum = actionNum
        self.description = description
    
    def execute(self,*params):
        return self.target.execute(self.actionNum, *params)
    
class MultiAction(CAction):
    def __init__(self,*actions):
        self.actions = list(actions)
        
    def execute(self,actionNum = 0, description = "Do multiple somethings",*params):
        actTime = 0
        for i in range(len(self.actions)):
            actTime += self.actions[i].execute(actionNum)
        return actTime//len(self.actions)
            
    def addAction(self,action):
        self.actions.append(action)
        
    
        