import sys, pygame
from const import *
from func import *
from personne import *
from param import *

def run():
    pygame.init()
    pygame.font.init()


    screen = pygame.display.set_mode(size)
    screen.fill((255,255,255))
    drawAxis(screen)
    drawFig(screen)
    tot = totalPers(screen)
    i=0
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if i < nbPersonne:
                        tot.split()
        pygame.display.flip()
