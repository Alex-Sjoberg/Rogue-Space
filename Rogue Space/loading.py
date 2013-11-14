'''
Created on May 3, 2013

@author: asjoberg
'''
import pickle

## Unpickles a ship from a file and returns it
def load_ship(filename):
    shipfile = open("./ships/" + filename,"rb")
    ship = pickle.load(shipfile)
    ship.unpickle() 
    shipfile.close()
    return ship

def save_ship(ship, filename):
    outfile = open("./ships/"+ str(filename) + ".pkl", "wb")
    ship.pre_pickle()
    pickle.dump(ship,outfile,-1)
    ship.unpickle()
    outfile.close()