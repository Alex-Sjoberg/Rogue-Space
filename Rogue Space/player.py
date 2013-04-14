import data as g
import pygame,misc,entity,inventory,tile


class Player(entity.Entity):
    def __init__(self,x,y,ship):
        super().__init__(ship = ship)
        self.tile = tile.Tile(character = "@")

            
       # self.pos = self.tile.image.get_rect().move(g.Xt//2*(g.FONTSIZE//2),g.Yt//2*g.FONTSIZE)
        
        self.xPos = len(self.ship.map[0])//2
        self.yPos = len(self.ship.map)//2


        
        self.actionPoints = 0
        self.speed = 100
       # g.SCREEN.blit(self.tile.image,self.pos)
        
        self.inventory = inventory.Inventory(self)
    def take_turn(self):
        misc.displayMap(self.xDisp,self.yDisp,self.ship)
        misc.makeMinimap()
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
                        misc.displayMap(self.xDisp,self.yDisp,self.ship)
                        return 0
                    elif newEvent.unicode == ',':
                        if self.itemHere():
                            return self.getItems()
                        else:
                            misc.logNow("Nothing there")
                            return 0
                    elif newEvent.unicode == "x":
                        return misc.look(self.ship,self.xDisp,self.yDisp)
                        
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
                        t = misc.checkOccupied(dir,self.xPos,self.yPos,self.ship)
                        if isinstance(t,entity.Entity):
                            self.attack(t)
                            return 200
                        elif self.move(dir):
                            return 100
                
                pygame.display.update()

    def canActivate(self,dir,x,y):
        try:    
            if dir == "UP":
                if y == 0 or not self.ship.map[y-1][x].component.action:
                    return False
            elif dir == "DOWN":
                if y == len(self.ship.map) or not self.ship.map[y+1][x].component.action:
                    return False
            elif dir == "LEFT":
                if x == 0 or not self.ship.map[y][x-1].component.action:
                    return False
            elif dir == "RIGHT":
                if x == len(self.ship.map[0]) or not self.ship.map[y][x+1].component.action:
                    return False
            return True
        except AttributeError:
            return False
    
    def activate(self,dir,x,y):
        if dir == "UP":
            return self.ship.map[y-1][x].component.execute()
        elif dir == "DOWN":
            return self.ship.map[y+1][x].component.execute()
        elif dir == "LEFT":
            return self.ship.map[y][x-1].component.execute()
        elif dir == "RIGHT":
            return self.ship.map[y][x+1].component.execute()
        
        
    def move(self,direction):
            if not misc.checkMove(direction,self.xPos,self.yPos,self.ship):
                misc.logNow("Can't move there")
                return False
            self.ship.entMap[self.yPos][self.xPos] = None
            
            
            super().move(direction)
            '''        
            g.SCREEN.fill((0,0,0),self.pos)
            g.SCREEN.blit(self.ship.map[self.yPos][self.xPos].tile.image , self.pos)
            
            if direction == "UP":
                if self.onEdge("y",-1):
                    self.pos=self.pos.move(0,-g.FONTSIZE)
                    self.yPos-=1
                else:
                    self.yPos-=1
                    self.yDisp-=1
    
            elif direction == "DOWN":
                if self.onEdge("y",+1):
                    self.pos=self.pos.move(0,g.FONTSIZE)
                    self.yPos+=1
                else:
                    self.yPos+=1
                    self.yDisp+=1
                
            elif direction == "LEFT":
                if self.onEdge("x",-1):
                    self.xPos-=1
                    self.pos=self.pos.move(-g.FONTSIZE//2,0)
                else:
                    self.xPos-=1
                    self.xDisp-=1
                
            elif direction == "RIGHT":
                if self.onEdge("x",+1):
                    self.xPos+=1
                    self.pos=self.pos.move(g.FONTSIZE//2,0)
                else:
                    self.xPos+=1
                    self.xDisp+=1
                   
            g.SCREEN.blit(self.tile.image, self.pos)
            '''
        
            self.ship.entMap[self.yPos][self.xPos] = self
            return True 
           
    def itemHere(self):
        if self.ship.map[self.yPos][self.xPos].inventory:
            return True
        return False
    
    def getItems(self):
        if not self.inventory.isFull():
            tileInv = self.ship.map[self.yPos][self.xPos].inventory
            for key in list(tileInv.getKeys()):
                if not self.inventory.isFull():
                    self.inventory.addItem(tileInv.getItem(key))
            return 100
        else:
            misc.logNow("Inventory is full")
            return 0
        


