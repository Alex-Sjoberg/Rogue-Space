'''
Created on May 3, 2013

@author: asjoberg
'''
import pickle

## Unpickles a ship from a file and returns it
def load_ship(filename):
    shipfile = open(filename,"rb")
    ship = pickle.load(shipfile)
    ship.unpickle() 
    shipfile.close()
    return ship