'''
Created on Mar 12, 2013

@author: asjoberg
'''
from collections import deque

class Timer():
    
    def __init__(self):
        self.timedObjects = deque()


    def register(self,obj):
        self.timedObjects.append(obj)
        obj.action_points = 0

    def release(self,obj):
        self.timedObjects.remove(obj)
    
    def tick(self):
        if len(self.timedObjects) > 0:
            obj = self.timedObjects[0]
            self.timedObjects.rotate()
            obj.action_points += obj.speed
            while obj.action_points > 0:
                obj.action_points -= obj.take_turn()