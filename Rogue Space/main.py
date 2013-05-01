import pygame, sys,traceback
import data as g
import interface as UI
import ship
import player
import misc
import gameTime
import npc

pygame.init()
pygame.event.set_allowed([pygame.KEYDOWN,pygame.QUIT])


def main():
    playing = True
    timer = gameTime.Timer();
    g.CURSHIP = pShip = ship.Ship(3,heading = 45)
    eShip1 = ship.Ship(3, x=105)
    eShip2 = ship.Ship(1, y=95)
    misc.printShips()
    misc.makeMinimap()
    
    g.LOG.logNow("Welcome to Rogue Space!")
    #misc.log("This should be the second message to be displayed and it should be way too long so it is on multiple linesaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaSO MANY LINES THAT IT NEEDS TWO WHOLE SCREENS!!!!!!! WHOOOOOAAAAAA NO WAY MAN!!!!! THATS SO COOL! I KNOW RIGHT ISNT IT SO COLL I HAVE TO PAD THIS STUPID STRING OS MUCH!!!!!!!!!!!!!!!!!!!!")
    
    g.PLAYER = p = player.Player(g.MWIDTH//2,g.MHEIGHT//2,0,ship = pShip)
    matey = npc.NPC(g.N.CREWMAN,23,17,0,eShip1)
    pShip.entMap[p.zPos][p.yPos][p.xPos] = p
    
    timer.register(p)
    timer.register(matey)
    timer.register(pShip)
    timer.register(eShip1)
    timer.register(eShip2)
    
    pygame.display.update()
  
    while True:
        
        timer.tick()
        g.CLOCK.tick(30)


try:
    main()
except Exception as e:
    tb = sys.exc_info()[2]
    traceback.print_exception(e.__class__, e, tb)
finally:
    pygame.quit()
