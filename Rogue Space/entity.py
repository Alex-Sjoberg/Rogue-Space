'''
Created on Mar 12, 2013

@author: asjoberg
'''
import misc
import data as g

class Entity():
    def __init__(self,ship = g.CURSHIP):
        self.ship = ship
        
    def attack(self,target):
        misc.log("Hi-yah!")
