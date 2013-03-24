'''
Created on Mar 16, 2013

@author: asjoberg
'''

import queue,pygame,misc
import data as g

class Inventory():
    
    def __init__(self ,owner, *items):
        self.owner = owner

        self.letters1 = queue.PriorityQueue(26)
        self.letters2 = queue.PriorityQueue(26)
    
        for i in "abcdefghijklmnopqrstuvwxyz": 
            self.letters1.put(i)
        for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.letters2.put(i)
         
        self.usedLetters = []
        self.items = {}
        for item in items:
            self.addItem(item)
    
    def addItem(self,item):
        if not self.letters1.empty():
            newLetter = self.letters1.get()
            self.items[newLetter] = item
            self.usedLetters += list(newLetter)
            return True
        elif not self.letters2.empty():
            newLetter = self.letters2.get()
            self.items[newLetter] = item
            self.usedLetters += list(newLetter)
        else:
            return False
        
    def getItem(self,key):
        ret = self.items.pop(key)
        self.usedLetters.remove(key)
        if (len(self.items) == 0):
            self.owner.inventory = None
            
        return ret
    
    def peek(self):
        return self.items[self.usedLetters[0]]
        
      
    def getKeys(self):
        return self.items.keys()
    
    def examine(self):
        self.displayItems()
        
        while True:
            g.CLOCK.tick(60)
            for newEvent in pygame.event.get():
                if newEvent.type == pygame.KEYDOWN:
                    key = newEvent.unicode
                    if key in self.usedLetters:
                        self.items[key].displayDescription()
                        self.displayItems()
                    elif key ==" ":
                        return
                        
                        
    def displayItems(self):
        g.SCREEN.fill((0,0,0))
        keys = list(self.items.keys())
        keys.sort()
        startx = 10
        starty = 10
        xoffset = 0
        yoffset = 0
        for key in keys:
            misc.printText("- " + key, g.FONTNAME, g.FONTSIZE, startx + xoffset, starty + yoffset)
            misc.printText(self.items[key].name, g.FONTNAME, g.FONTSIZE, startx + xoffset + g.FONTSIZE, starty + yoffset)
            yoffset += g.FONTSIZE + 5
    
        pygame.display.update()