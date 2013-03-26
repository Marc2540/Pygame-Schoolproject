import pygame
import sys

#            R    G    B
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)

pygame.init()
pygame.display.set_caption("Pygame School Project")
clock = pygame.time.Clock()

#assets
my_font=pygame.font.SysFont("Times New Roman",24)
background = pygame.image.load('background.png')
#game_title = pygame.image.load('game_title.png')
#play_button = pygame.image.load('game_run.png')
game_title = my_font.render('Game Title', True, black)
play_button = my_font.render('Start spil', True, black)


def run(screen):
    """Handles the main menu."""
    done = False

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = event.pos

                if event.button == 1: #left mouse button
                    if mousex in range((854//2)-(pygame.Surface.get_width(play_button)//2), (854//2)+(pygame.Surface.get_width(play_button)//2)) and mousey in range(480-100, 480-100+pygame.Surface.get_height(play_button)):
                        done = True

        screen.fill(white)
        screen.blit(background, (0, 0))
        screen.blit(game_title, ((854/2)-(pygame.Surface.get_width(game_title)/2), 100))
        screen.blit(play_button, ((854/2)-(pygame.Surface.get_width(play_button)/2),480-100))


        #Update & fps
        pygame.display.flip()
        clock.tick(5)