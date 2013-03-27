import pygame, sys,traceback
import data as g
import ship
import player
import misc
import gameTime
import npc

pygame.init()



def main():
    timer = gameTime.Timer();
    pShip = ship.Ship(4)
    g.ENTS = [[None for i in range(g.MWIDTH)] for j in range(g.MHEIGHT)]
    misc.displayMap(g.MWIDTH//2,g.MHEIGHT//2)
    misc.log("Welcome to Rogue Space!")
    misc.displayUI()
    p = player.Player(g.MWIDTH//2,g.MHEIGHT//2)
    matey = npc.NPC(g.N.CREWMAN,23,17)
    g.ENTS[p.yPos][p.xPos] = p
    timer.register(p)
    timer.register(matey)
    pygame.display.update()
    
    while True:
        
        timer.tick()
        g.CLOCK.tick(60)


try:
    main()
except Exception as e:
    tb = sys.exc_info()[2]
    traceback.print_exception(e.__class__, e, tb)
finally:
    pygame.quit()
