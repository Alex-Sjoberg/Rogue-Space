'''
Created on Mar 17, 2013

@author: asjoberg
'''
import tile

class Item():
    def __init__(self,name = "Item", number = 1):
        self.number = number
        self.name = name
        self.description ="This is an object of some kind. You don't know what it is."
        self.tile = tile.Tile()
        
    def displayDescription(self):
        print(self.description)