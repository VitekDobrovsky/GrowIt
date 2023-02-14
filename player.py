import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        # display
        self.image = pygame.image.load('graphics/player/idle/1.png').convert_alpha()
        self.rect = self.image.get_rect(center=(WIDTH/2, HEIGHT/2))

        # move
        self.velocity = pygame.math.Vector2()
        self.speed = 2

        # animation
        self.status = 'idle'
        self.an_index = 0
        self.an_speed = 0.15
        self.an_frames = {
            'idle': [pygame.image.load('graphics/player/idle/1.png').convert_alpha(),
                    pygame.image.load('graphics/player/idle/2.png').convert_alpha(),
                    pygame.image.load('graphics/player/idle/3.png').convert_alpha(),
                    pygame.image.load('graphics/player/idle/3.png').convert_alpha(),
                    pygame.image.load('graphics/player/idle/2.png').convert_alpha(),
                    pygame.image.load('graphics/player/idle/1.png').convert_alpha()],
            'left': [pygame.image.load('graphics/player/left/1.png').convert_alpha(),
                    pygame.image.load('graphics/player/left/2.png').convert_alpha(),
                    pygame.image.load('graphics/player/left/3.png').convert_alpha(),
                    pygame.image.load('graphics/player/left/2.png').convert_alpha(),
                    pygame.image.load('graphics/player/left/1.png').convert_alpha()],
            'right': [pygame.image.load('graphics/player/right/1.png').convert_alpha(),
                    pygame.image.load('graphics/player/right/2.png').convert_alpha(),
                    pygame.image.load('graphics/player/right/3.png').convert_alpha(),
                    pygame.image.load('graphics/player/right/2.png').convert_alpha(),
                    pygame.image.load('graphics/player/right/1.png').convert_alpha()],
            'down': [pygame.image.load('graphics/player/down/1.png').convert_alpha(),
                    pygame.image.load('graphics/player/down/2.png').convert_alpha(),
                    pygame.image.load('graphics/player/down/3.png').convert_alpha(),
                    pygame.image.load('graphics/player/down/2.png').convert_alpha(),
                    pygame.image.load('graphics/player/down/1.png').convert_alpha()],
            'up': [pygame.image.load('graphics/player/up/1.png').convert_alpha(),
                    pygame.image.load('graphics/player/up/2.png').convert_alpha(),
                    pygame.image.load('graphics/player/up/3.png').convert_alpha(),
                    pygame.image.load('graphics/player/up/2.png').convert_alpha(),
                    pygame.image.load('graphics/player/up/1.png').convert_alpha()]}

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.velocity.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.velocity.y = 1
            self.status = 'down'
        else:
            self.velocity.y = 0
        if keys[pygame.K_RIGHT]:
            self.velocity.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.velocity.x = -1
            self.status = 'left'
        else:
            self.velocity.x = 0

        if self.velocity.x == 0 and self.velocity.y == 0:
            self.status = 'idle'

    def move(self):
        self.rect.x += self.velocity.x * self.speed
        self.rect.y += self.velocity.y * self.speed

    def animate(self):
        if self.an_index >= len(self.an_frames[self.status]) - 1:
            self.an_index = 0

        self.an_index = round(self.an_index, 1)
        self.an_index += self.an_speed
        self.image = self.an_frames[self.status][int(self.an_index)]

    def update(self):
        self.input()
        self.move()
        self.animate()