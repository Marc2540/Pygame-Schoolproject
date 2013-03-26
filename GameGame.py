import pygame
import sys
import GamePlayer

#            R    G    B
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)

pygame.init()
pygame.display.set_caption("Pygame School Project")
clock = pygame.time.Clock()

background = pygame.image.load('background.png')


def run(screen):
    Player = GamePlayer.Player(854//2, 420)
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            Player.movement('left')
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            Player.movement('right')
        elif pygame.key.get_pressed()[pygame.K_UP]:
            Player.movement('up')
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            Player.movement('down')

        screen.fill(white)
        screen.blit(background, (0, 0))
        screen.blit(Player.player_picture, (Player.player_x, Player.player_y))

        #Update & fps
        pygame.display.flip()
        clock.tick(30)