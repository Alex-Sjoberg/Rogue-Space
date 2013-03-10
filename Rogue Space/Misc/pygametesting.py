import pygame , sys , traceback
import pygame.font
from pygame import *
pygame.init()
pygame.font.init()

def main():
    size = width , height = 1000, 1000
    speed = [2,2]
    black = 0,0,0

    screen = pygame.display.set_mode((1000,1000))
    clock = pygame.time.Clock()
    ball = pygame.image.load("ball.gif")
    myFont = pygame.font.Font("DwarfFortressVan.ttf",36)

    adventurer = myFont.render('\u00A9' , False , (255,255,255) , (0,0,255))
    adrect = adventurer.get_rect()
    while True:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type in (QUIT , KEYDOWN):
                pygame.quit()
            elif event.type == K_LEFT:
                adrect.speed[0] = 0

        adrect = adrect.move(speed)
        print(adrect, adventurer.get_rect())
        if adrect.left < 0 or adrect.right > width:
                speed[0] = -speed[0]
        if adrect.top < 0 or adrect.bottom > height:
                speed[1] = -speed[1]


        screen.fill(black)
        screen.blit(adventurer,adrect)
        pygame.display.flip()
    
try:
    main()
except Exception as e:
    tb = sys.exc_info()[2]
    traceback.print_exception(e.__class__, e, tb)
finally:
    pygame.quit()
##
##def main():
##    print("main")
##
##class Adventurer:
##    def __init__(self,char,height,speed):
