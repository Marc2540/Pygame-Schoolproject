import pygame

class Player():
    def __init__(self, x, y):
        self.player_x = x
        self.player_y = y
        self.health = 100
        self.current_weapon = None
        self.player_picture = pygame.image.load('player.png')
        self.speed = 10

    def movement(self, direction):
        if direction == 'left':
            self.player_x -= self.speed
            if self.player_x <= 0:
                self.player_x = 0
        elif direction == 'right':
            self.player_x += self.speed
            if (self.player_x + pygame.Surface.get_width(self.player_picture)) >=854:
                self.player_x = (854 - pygame.Surface.get_width(self.player_picture))
        elif direction == 'up':
            self.player_y -= self.speed
            if self.player_y <= 0:
                self.player_y = 0
        elif direction == 'down':
            self.player_y += self.speed
            if (self.player_y + pygame.Surface.get_height(self.player_picture)) >= 480:
                self.player_y = (480 - pygame.Surface.get_height(self.player_picture))

    def collision(self):
        pass

    def attacking(self):
        pass

class Weapon():
    def __init__(self):
        pass