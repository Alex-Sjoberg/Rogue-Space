class Player():
    def __init__(self,x,y):
        fontObj = pygame.font.Font(FONTNAME,FONTSIZE).render('@',False,(255,255,255),(0,0,0))
        self.image = Surface((FONTSIZE//2,FONTSIZE))
        self.image.blit(fontObj,(0,0),(0,0,FONTSIZE//2,FONTSIZE))
        self.pos = self.image.get_rect().move(Xt//2*(FONTSIZE//2),Yt//2*FONTSIZE)
        self.xPos = len(playMap[0])//2
        self.yPos = len(playMap)//2
        self.xDisp = self.xPos
        self.yDisp = self.yPos
        SCREEN.blit(self.image,self.pos)

    def move(self,direction):
        if not checkMove(direction,self.xPos,self.yPos):
            print("Can't move there, sorry")
            return False
        SCREEN.fill((0,0,0),self.pos)
        SCREEN.blit(playMap[self.yPos][self.xPos].image , self.pos)
        
        if direction == "UP":
            if self.onEdge("y",-1):
                self.pos=self.pos.move(0,-FONTSIZE)
                self.yPos-=1
            else:
                self.yPos-=1
                self.yDisp-=1
                displayMap(self.xDisp,self.yDisp)

        elif direction == "DOWN":
            if self.onEdge("y",+1):
                self.pos=self.pos.move(0,FONTSIZE)
                self.yPos+=1
            else:
                self.yPos+=1
                self.yDisp+=1
                displayMap(self.xDisp,self.yDisp)
            
        elif direction == "LEFT":
            if self.onEdge("x",-1):
                self.xPos-=1
                self.pos=self.pos.move(-FONTSIZE//2,0)
            else:
                self.xPos-=1
                self.xDisp-=1
                displayMap(self.xDisp,self.yDisp)
            
        elif direction == "RIGHT":
            if self.onEdge("x",+1):
                self.xPos+=1
                self.pos=self.pos.move(FONTSIZE//2,0)
            else:
                self.xPos+=1
                self.xDisp+=1
                displayMap(self.xDisp,self.yDisp)
        SCREEN.blit(self.image, self.pos)
##        print(self.image.get_rect() , self.pos)
##        print(self.xPos,self.yPos)
##        print(self.xDisp,self.yDisp)


        
    def onEdge(self,axis,direct):
        if axis == "x":
            if ((self.xPos - Xt//2) <= 0 or (self.xPos +Xt//2) >= len(playMap[0])) and ((self.xPos - Xt//2 +direct) <= 0 or (self.xPos +Xt//2 +direct) >= len(playMap[0])):
                return True
            return False
        else:
            print(((self.yPos +Yt//2) ,len(playMap)))
            if ((self.yPos -Yt//2) <= 0 or (self.yPos + Yt//2 ) >= len(playMap)-1) and ((self.yPos -Yt//2+direct) <= 0 or (self.yPos + Yt//2 + direct) >= len(playMap)-1):
                return True
            return False
