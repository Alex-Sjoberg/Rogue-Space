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
                        playing = False
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
                            print("Nothing there")
                            return 0
                    elif newEvent.key in [273,274,275,276]:
                        if newEvent.key == 273:
                            dir = "UP"
                        elif newEvent.key == 274:
                            dir = "DOWN"
                        elif newEvent.key == 276:
                            dir = "LEFT"
                        elif newEvent.key == 275:
                            dir = "RIGHT"

                        t = misc.checkOccupied(dir,self.xPos,self.yPos)
                        if isinstance(t,entity.Entity):
                            self.attack(t)
                            return 200
                        elif self.move(dir):
                            return 100
                
                pygame.display.update()
                return 0

    def move(self,direction):
        if not misc.checkMove(direction,self.xPos,self.yPos):
            print("Can't move there, sorry")
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
                misc.displayMap(self.xDisp,self.yDisp)

        elif direction == "DOWN":
            if self.onEdge("y",+1):
                self.pos=self.pos.move(0,g.FONTSIZE)
                self.yPos+=1
            else:
                self.yPos+=1
                self.yDisp+=1
                misc.displayMap(self.xDisp,self.yDisp)
            
        elif direction == "LEFT":
            if self.onEdge("x",-1):
                self.xPos-=1
                self.pos=self.pos.move(-g.FONTSIZE//2,0)
            else:
                self.xPos-=1
                self.xDisp-=1
                misc.displayMap(self.xDisp,self.yDisp)
            
        elif direction == "RIGHT":
            if self.onEdge("x",+1):
                self.xPos+=1
                self.pos=self.pos.move(g.FONTSIZE//2,0)
            else:
                self.xPos+=1
                self.xDisp+=1
                misc.displayMap(self.xDisp,self.yDisp)
        g.ENTS[self.yPos][self.xPos] = self
        g.SCREEN.blit(self.tile.image, self.pos)

        return True
    def itemHere(self):
        if g.playMap[self.yPos][self.xPos].inventory:
            return True
        return False
    
    def getItems(self):
        tileInv = g.playMap[self.yPos][self.xPos].inventory
        for key in list(tileInv.getKeys()):
            self.inventory.addItem(tileInv.getItem(key))
        return 100
        
    def onEdge(self,axis,direct):
        if axis == "x":
            if ((self.xPos - g.Xt//2) <= 0 or (self.xPos +g.Xt//2) >= len(g.playMap[0])) and ((self.xPos - g.Xt//2 +direct) <= 0 or (self.xPos +g.Xt//2 +direct) >= len(g.playMap[0])):
                return True
            return False
        else:
            if ((self.yPos -g.Yt//2) <= 0 or (self.yPos + g.Yt//2 ) >= len(g.playMap)-1) and ((self.yPos -g.Yt//2+direct) <= 0 or (self.yPos + g.Yt//2 + direct) >= len(g.playMap)-1):
                return True
            return False

