import pygame
pygame.init()

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

FONTNAME = "DwarfFortressVan.ttf"

global CURSHIP
CURSHIP = None

global SHIPS
SHIPS = []

global CURSOR
CURSOR = None

global PLAYER
PLAYER = None

global FONTSIZE
FONTSIZE = 32

global MSGSIZE
MSGSIZE = 20

global MINISIZE
MINISIZE = 14

global MINIPADDING
MINIPADDING = 10

global Xt
Xt = 50

global Yt
Yt = Xt//2

global MXt
MXt = 25

global MYt
MYt = 25

global size, width, height
size = width, height = (Xt*FONTSIZE + 10, Yt*FONTSIZE + FONTSIZE *6)

global SCREEN
SCREEN = pygame.display.set_mode(size)

global CLOCK
CLOCK = pygame.time.Clock()

global MWIDTH
MWIDTH=0

global MHEIGHT
MHEIGHT=0

global playMap
playMap = []

global E
E = enum("SPACE","WALL1","FLOOR","CDOOR","ODOOR","LASER","CTRLS","ENGNE","SNSOR","MANUV")

global S
S=enum("SHIP1","SHIP2")

global N
N = enum("CREWMAN","SLIME","NINJA")

global C
C = enum("LASER","CONTROL","TELEPAD","ENGINE","SENSOR","MANEUVER")

global SG
SG = enum("FIRE")

global ENTS
ENTS = []

global BLACK
BLACK = (0,0,0)

global GREY
GREY = (140,140,140)

global WHITE
WHITE = (255,255,255)

global DGREY
DGREY = (100,100,100)

global RED
RED = (255,0,0)

global ORANGE
ORANGE = (100,100,0)

#global COMPLIST
#COMPLIST = []
'''
global MHISTORY
MHISTORY = []

global MPENDING
MPENDING = []

global LOGDISP
LOGDISP = pygame.Surface( ((Xt*FONTSIZE)//2 - 2 , FONTSIZE*6 - 2) )
'''
import interface

global LOG
LOG = interface.MessageLog(2, 2+ Yt*FONTSIZE, Xt*FONTSIZE//2-2, FONTSIZE*6 -2,MSGSIZE)

import tile

global MINIMAP
MINIMAP = [  [tile.Tile(character = ".",fontsize = MINISIZE, minimap = True) for i in range (MXt)] for i in range (MYt) ]

global MINIDISP
MINIDISP = pygame.Surface( (MXt*(MINISIZE+MINIPADDING) , MYt*(MINISIZE+MINIPADDING))  )

global MAPDISP
MAPDISP = pygame.Surface((Xt * FONTSIZE , Yt * FONTSIZE))




