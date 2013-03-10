import pygame, sys,traceback
import data as g
import ship
import player
import environ



##FONTNAME = "DwarfFortressVan.ttf"
##FONTSIZE = 24
##WALKABLES = ["\u00B7",'\u00AA']
##Xt = 50
##Yt = Xt//2
##
##size = width, height = (Xt*FONTSIZE + 10, Yt*FONTSIZE + 5)
##pygame.init()
##pygame.font.init()
##
##SCREEN = pygame.display.set_mode(size)
##CLOCK = pygame.time.Clock()
##MWIDTH=0
##MHEIGHT=0
##playMap = []

g.initGlobals()


def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

def main():
    playing = True

    pShip = ship.Ship(2)
    print(MWIDTH,MHEIGHT)
    displayMap(MWIDTH//2,MHEIGHT//2)
##    print('*'*30)
    player = Player(MWIDTH//2,MHEIGHT//2)
    display.update()
    while playing:
        
        CLOCK.tick(60)
        for newEvent in pygame.event.get():
##            print(newEvent.type)
            
            if newEvent.type == QUIT:
                pygame.quit()
                              
            elif newEvent.type == KEYDOWN:
##                print ("Key was" , newEvent.key)
                if newEvent.unicode == 'q':
                    pygame.quit()
                    playing = False
                    break
                elif newEvent.key == 273:
                    player.move("UP")
                elif newEvent.key == 274:
                    player.move("DOWN")
                elif newEvent.key == 276:
                    player.move("LEFT")
                elif newEvent.key == 275:
                    player.move("RIGHT")
            pygame.display.update()
        
        

##def fillplayMap():
##    

def debugMapDisplay():
    for i in range (len(playMap)):
        print()
        for j in range(len(playMap[15])):
            print(playMap[i][j].char,end = '')
                  
def displayMap(playerX,playerY):
##    debugMapDisplay()
    SCREEN.fill((0,0,0))
    for y in range(Yt):
        for x in range(Xt):
##            print (playerY, Yt//2, playerX)
            displayAt(playerX-Xt//2 +x, playerY-Yt//2 +y,x,y)

def displayAt(xTile,yTile,x,y):
##    print(yTile,xTile,x,y , )
    SCREEN.blit(playMap[yTile][xTile].image,(x*FONTSIZE//2,y*FONTSIZE))



def checkMove(direction,x,y):
    
    if direction == "UP":
        if y == 0 or playMap[y-1][x].char not in WALKABLES:
            return False
    elif direction == "DOWN":
        if y == len(playMap) or playMap[y+1][x].char not in WALKABLES:
            return False
    elif direction == "LEFT":
        if x == 0 or playMap[y][x-1].char not in WALKABLES:
            return False
    elif direction == "RIGHT":
        if x == len(playMap[0]) or playMap[y][x+1].char not in WALKABLES:
            return False
    return True



          

class NPC():
    def __init__(self):
        print("Non-players!")

try:
    main()
except Exception as e:
    tb = sys.exc_info()[2]
    traceback.print_exception(e.__class__, e, tb)
finally:
    pygame.quit()
