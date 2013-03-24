import pygame
pygame.init()

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

FONTNAME = "DwarfFortressVan.ttf"

global FONTSIZE
FONTSIZE = 24

global WALKABLES
WALKABLES = ["\u00B7",'\u00AA']

global Xt
Xt = 50

global Yt
Yt = Xt//2

global size, width, height
size = width, height = (Xt*FONTSIZE + 10, Yt*FONTSIZE + 5)

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
E = enum("SPACE","WALL1","FLOOR","CDOOR","ODOOR")

global S
S=enum("SHIP1","SHIP2")

global N
N = enum("CREWMAN","SLIME","NINJA")

global ENTS
ENTS = []



