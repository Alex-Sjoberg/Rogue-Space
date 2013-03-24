'''
Created on Mar 21, 2013

@author: asjoberg
'''

import environ
import tile
import data as g
import signals

class Component():
    def __init__(self,type,signal = None ,fireable = None, tile = None):
        if type == g.C.LASER:
            self.char = "\u0142"
            
        elif type == g.C.CONTROL:
            self.char = "\u011f"
            self.usable = True
            self.signal = signals.Signal(type = g.SG.FIRE)
            
        self.tile = tile.Tile(character = self.char)
        
    def execute(self):
        if self.signal:
            self.signal.send()
       
class Fireable():
    def __init__(self,type):
        