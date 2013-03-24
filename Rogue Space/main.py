import pygame, sys,traceback
import data as g
import ship
import player
import misc
import gameTime
import npc

pygame.init()



def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

def main():
    playing = True
    timer = gameTime.Timer();
    pShip = ship.Ship(3)
    g.ENTS = [[None for i in range(g.MWIDTH)] for j in range(g.MHEIGHT)]
    misc.displayMap(g.MWIDTH//2,g.MHEIGHT//2)
    p = player.Player(g.MWIDTH//2,g.MHEIGHT//2)
    matey = npc.NPC(g.N.CREWMAN,23,17)
    g.ENTS[p.yPos][p.xPos] = p
    timer.register(p)
    timer.register(matey)
    pygame.display.update()
    
    while playing:
        
        timer.tick()
        g.CLOCK.tick(60)


try:
    main()
except Exception as e:
    tb = sys.exc_info()[2]
    traceback.print_exception(e.__class__, e, tb)
finally:
    pygame.quit()
