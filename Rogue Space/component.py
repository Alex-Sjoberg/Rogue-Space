'''
Created on Mar 21, 2013

@author: asjoberg
'''

import pygame
import tile
import data as g
import misc
import interface as UI
from abc import  ABCMeta , abstractmethod

#TODO WHy does action have more than one action? component should have more than one possible action
# not the action itself
# Whole component thing needs reworked
class Component():
    def __init__(self,type,owner = None, *action):
        self.owner = owner
        action = list(action)        
        if type == g.C.LASER:
            char = "\u0142"
            self.action = Fire(self)
            self.name = "Laser"
            
        elif type == g.C.CONTROL:
            char = "\u011f"
            self.action = ActMenu(action)
            self.name = "Control console"
            
        elif type == g.C.ENGINE:
            char = "\u00cb"
            self.action = Engine()
            self.name = "Engine"
            self.power = 50
            
        elif type == g.C.SENSOR:
            char = "O"
            self.action = Sensor(self)
            self.name = "Sensor"
            
        elif type == g.C.MANEUVER:
            char = "\u0134"
            self.action = Maneuvering(self,owner = owner)
            self.name = "Maneuvering thruster"
            self.power = 10
            
        self.type = type    
        self.tile = tile.Tile(character = char)
        
    def execute(self,actionNum = 0):
        return self.action.execute(actionNum)
       
    def pre_pickle(self):
        self.tile.pre_pickle()
        
    def unpickle(self):
        self.tile.unpickle()
        
        
class CAction():
    def __init__(self):
        self.description = "Do nothing"
        self.linkedActions = []
        
    def execute(self,actionNum = 0):
        g.LOG.log("That didn't seem to do anything")
        return 50
    

        
            
class Fire(CAction):
    def __init__(self,owner,description = "Fire this weapon"):
        self.owner = owner
        self.description = description
        
    def execute(self,actionNum = 0):
        if actionNum == 0:
            g.LOG.log("I'm firin the laser")
            return 50
        else:
            g.LOG.log("I'm firing the laser heroically")
            return 50
                
class Engine():
    def __init__(self,owner = None):
        self.owner = owner
        
    def execute(self,actionNum = 0, *params):
        g.LOG.log("engining")
        g.CURSHIP.velocity += 50 ##PLACEHOLDER
        return 50
                
class ActMenu(CAction):
    def __init__(self, actions, owner = None):
        self.actions = actions
        self.owner = owner
        
    def execute(self,actionNum = 0):
        if len (self.actions) == 0:
            g.LOG.log("Its not working!")
            return 0
        if len(self.actions) == 1:
            return self.actions[0].execute()
        else: ##display menu of possible actions
            g.SCREEN.fill((0,0,0))
            startx = 10
            starty = 10
            xoffset = 0
            yoffset = 0
            #TODO replace with itemlist object - duplicate code
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
    def __init__(self,owner = None, target=None, actionNum = 0, description = "Do something"):
        self.owner = owner
        self.target = target
        self.actionNum = actionNum
        self.description = description
    
    def execute(self,*params):
        return self.target.execute(self.actionNum, *params)
    
class MultiAction(CAction):## for executing multiple component's actions with a single command
    def __init__(self,owner = None, *actions):
        self.actions = list(actions)
        
    def execute(self,actionNum = 0, description = "Do multiple somethings",*params):
        actTime = 0
        for i in range(len(self.actions)):
            actTime += self.actions[i].execute(actionNum)
        return actTime//len(self.actions)
            
    def addAction(self,action):
        action.owner = self.owner
        self.actions.append(action)
        
class Sensor(CAction):
    def __init__(self,owner = None,description = "Use the sensors"):
        self.owner = owner
        self.description = description
        
    def execute(self,actionNum = 0 , *params):
        toView = g.SHIPS[actionNum]
        misc.look(toView)
        pygame.display.update()
        return 10

class Maneuvering(CAction):
    def __init__(self, description = "Use the maneuvering thrusters", owner = g.CURSHIP):
        self.description = description
        self.owner = owner
        self.possible_actions = {"Set new heading":1}
        
    def execute(self,actionNum = 0,descrption = "Use the maneuvering thrusters",*params):
        try:
            newHeading = int(g.LOG.prompt("Enter new heading:"))
            if newHeading >= 0 and newHeading <360:
                self.owner.targetHeading = newHeading
                g.LOG.log("New heading set")
                return 100
            else:
                raise ValueError
        except ValueError:
            g.LOG.logNow("Invalid heading")
            return 0
    
class Interactable(object):
    __metaclass__ = ABCMeta
    
    
    @abstractmethod
    def execute_interaction(self):
        pass
    


