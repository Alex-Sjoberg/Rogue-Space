import pygame, sys,traceback
import data as g
import ship
import player
import misc
import gameTime
import npc

pygame.init()


def main():
    misc.initMinimap()
    timer = gameTime.Timer();
    g.CURSHIP = pShip = ship.Ship(4)
    eship1 = ship.Ship(2)
    eship2 = ship.Ship(1)
    #g.ENTS = [[None for i in range(g.MWIDTH)] for j in range(g.MHEIGHT)]
    
    misc.log("Welcome to Rogue Space!")
    #misc.log("This should be the second message to be displayed and it should be way too long so it is on multiple linesaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaSO MANY LINES THAT IT NEEDS TWO WHOLE SCREENS!!!!!!! WHOOOOOAAAAAA NO WAY MAN!!!!! THATS SO COOL! I KNOW RIGHT ISNT IT SO COLL I HAVE TO PAD THIS STUPID STRING OS MUCH!!!!!!!!!!!!!!!!!!!!")
    
    p = player.Player(g.MWIDTH//2,g.MHEIGHT//2,ship = pShip)
    matey = npc.NPC(g.N.CREWMAN,23,17,eship1)
    pShip.entMap[p.yPos][p.xPos] = p
    timer.register(p)
    timer.register(matey)
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
