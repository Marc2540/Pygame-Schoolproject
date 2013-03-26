import pygame
import sys

from GameLevel import *
import GameMisc
 
#            R    G    B
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
 
pygame.init()

size = [854,480]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame School Project")
clock = pygame.time.Clock()

while True:

    GameMisc.game_state(screen)

#    for event in pygame.event.get(): # User did something
#        if event.type == pygame.QUIT: # If user clicked close
#            pygame.quit()
#            sys.exit()
    

    
    #Update & fps
#    pygame.display.flip()
#    clock.tick(30)
