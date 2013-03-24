'''
Created on Mar 21, 2013

@author: asjoberg
'''
import data as g

class Signal():
    def __init__(self,owner,target,type):
        self.type = type
        self.owner = owner
    
    def send(self):
        if self.type == g.SG.FIRE:
            self.target.fireable.fire()
        