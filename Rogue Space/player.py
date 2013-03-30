import data as g
import pygame,misc,entity,inventory,tile



class Player(entity.Entity):
    def __init__(self,x,y):
        
        self.tile = tile.Tile(character = "@")

            
        self.pos = self.tile.image.get_rect().move(g.Xt//2*(g.FONTSIZE//2),g.Yt//2*g.FONTSIZE)
        
        self.xPos = len(g.playMap[0])//2
        self.yPos = len(g.playMap)//2
        self.xDisp = self.xPos
        self.yDisp = self.yPos

        
        self.actionPoints = 0
        self.speed = 100
        g.SCREEN.blit(self.tile.image,self.pos)
        
        self.inventory = inventory.Inventory(self)

    def take_turn(self):
        misc.displayMap(self.xDisp,self.yDisp)
        while True:
            for newEvent in pygame.event.get():
    ##            print(newEvent.type)
                
                if newEvent.type == pygame.QUIT:
                    pygame.quit()
                                  
                elif newEvent.type == pygame.KEYDOWN:
    ##                print ("Key was" , newEvent.key)
                    if newEvent.unicode == 'q':
                        pygame.quit()
                        break
                    elif newEvent.unicode == '.':
                        return 50
                    elif newEvent.unicode == 'i':
                        self.inventory.examine()
                        misc.displayMap(self.xDisp,self.yDisp)
                        return 0
                    elif newEvent.unicode == ',':
                        if self.itemHere():
                            return self.getItems()
                        else:
                            misc.logNow("Nothing there")
                            return 0
                    elif newEvent.unicode == 'a':
                        misc.logNow("Which direction?")
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key in [273,274,275,276]:
                                        dir = self.chooseDir(event.key)
                                        if self.canActivate(dir,self.xPos,self.yPos):
                                            return self.activate(dir,self.xPos,self.yPos)
                                        else:
                                            misc.logNow("Can't activate that")
                                            return 0     
                                    else:
                                        misc.logNow("Invalid direction")
                                        return 0
                        
                    elif newEvent.key in [273,274,275,276]:
                        dir = self.chooseDir(newEvent.key)
                        t = misc.checkOccupied(dir,self.xPos,self.yPos)
                        if isinstance(t,entity.Entity):
                            self.attack(t)
                            return 200
                        elif self.move(dir):
                            return 100
                
                pygame.display.update()

    def canActivate(self,dir,x,y):
        try:    
            if dir == "UP":
                if y == 0 or not g.playMap[y-1][x].component.action:
                    return False
            elif dir == "DOWN":
                if y == len(g.playMap) or not g.playMap[y+1][x].component.action:
                    return False
            elif dir == "LEFT":
                if x == 0 or not g.playMap[y][x-1].component.action:
                    return False
            elif dir == "RIGHT":
                if x == len(g.playMap[0]) or not g.playMap[y][x+1].component.action:
                    return False
            return True
        except AttributeError:
            return False
    
    def activate(self,dir,x,y):
        if dir == "UP":
            return g.playMap[y-1][x].component.execute()
        elif dir == "DOWN":
            return g.playMap[y+1][x].component.execute()
        elif dir == "LEFT":
            return g.playMap[y][x-1].component.execute()
        elif dir == "RIGHT":
            return g.playMap[y][x+1].component.execute()
        
    def move(self,direction):
        if not misc.checkMove(direction,self.xPos,self.yPos):
            misc.logNow("Can't move there")
            return False
        g.SCREEN.fill((0,0,0),self.pos)
        g.SCREEN.blit(g.playMap[self.yPos][self.xPos].tile.image , self.pos)
        g.ENTS[self.yPos][self.xPos] = None
        
        if direction == "UP":
            if self.onEdge("y",-1):
                self.pos=self.pos.move(0,-g.FONTSIZE)
                self.yPos-=1
            else:
                self.yPos-=1
                self.yDisp-=1
                #misc.displayMap(self.xDisp,self.yDisp)

        elif direction == "DOWN":
            if self.onEdge("y",+1):
                self.pos=self.pos.move(0,g.FONTSIZE)
                self.yPos+=1
            else:
                self.yPos+=1
                self.yDisp+=1
                #misc.displayMap(self.xDisp,self.yDisp)
            
        elif direction == "LEFT":
            if self.onEdge("x",-1):
                self.xPos-=1
                self.pos=self.pos.move(-g.FONTSIZE//2,0)
            else:
                self.xPos-=1
                self.xDisp-=1
                #misc.displayMap(self.xDisp,self.yDisp)
            
        elif direction == "RIGHT":
            if self.onEdge("x",+1):
                self.xPos+=1
                self.pos=self.pos.move(g.FONTSIZE//2,0)
            else:
                self.xPos+=1
                self.xDisp+=1
                #misc.displayMap(self.xDisp,self.yDisp)
        g.ENTS[self.yPos][self.xPos] = self
        g.SCREEN.blit(self.tile.image, self.pos)

        return True
    def itemHere(self):
        if g.playMap[self.yPos][self.xPos].inventory:
            return True
        return False
    
    def getItems(self):
        if not self.inventory.isFull():
            tileInv = g.playMap[self.yPos][self.xPos].inventory
            for key in list(tileInv.getKeys()):
                if not self.inventory.isFull():
                    self.inventory.addItem(tileInv.getItem(key))
            return 100
        else:
            misc.logNow("Inventory is full")
            return 0
        
    def onEdge(self,axis,direct):
        if axis == "x":
            if ((self.xPos - g.Xt//2) <= 0 or (self.xPos +g.Xt//2) >= len(g.playMap[0])) and ((self.xPos - g.Xt//2 +direct) <= 0 or (self.xPos +g.Xt//2 +direct) >= len(g.playMap[0])):
                return True
            return False
        else:
            if ((self.yPos -g.Yt//2) <= 0 or (self.yPos + g.Yt//2 ) >= len(g.playMap)-1) and ((self.yPos -g.Yt//2+direct) <= 0 or (self.yPos + g.Yt//2 + direct) >= len(g.playMap)-1):
                return True
            return False

    def chooseDir(self,key):
        if key == 273:
            dir = "UP"
        elif key == 274:
            dir = "DOWN"
        elif key == 276:
            dir = "LEFT"
        elif key == 275:
            dir = "RIGHT"
        return dir