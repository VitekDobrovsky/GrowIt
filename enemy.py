import pygame
from settings import *
from random import randint, choice

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # display
        self.image = pygame.Surface((50,50))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)

        # move
        self.velocity = pygame.math.Vector2()
        self.speed = 1
            # escape
        self.noticeRadius = 200
        self.collideBox = self.rect.inflate(25,25)

    def getDistance(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)

        distance = (player_vec - enemy_vec).magnitude()            

        return distance

    def getCollisionType(self, distance):
        type = None
        if self.collideBox.left <= 0:
            type = 'left'
        elif self.collideBox.right >= WIDTH:
            type = 'right'
            
        if self.collideBox.top <= 0:
            type = 'top'
        elif self.collideBox.bottom >= HEIGHT:
            type = 'bottom'
            
        if self.collideBox.top <= 0:
            if self.collideBox.left <= 0:
                type = 'top left'
            elif self.collideBox.right >= WIDTH:
                type = 'top right'
        elif self.collideBox.bottom >= HEIGHT:
            if self.collideBox.left <= 0:
                type = 'bottom left'
            elif self.collideBox.right >= WIDTH:
                type = 'bottom right'
            
        return type
    
    def escapePlayer(self, player):
        self.collideBox.center = self.rect.center
        distance = self.getDistance(player)
    
        collisionType = self.getCollisionType(distance)   
        
        if distance <= self.noticeRadius:
            if player.rect.x > self.rect.x:
                self.velocity.x = -1
            elif player.rect.x < self.rect.x:
                self.velocity.x = 1

            if player.rect.y > self.rect.y:
                self.velocity.y = -1
            elif player.rect.y < self.rect.y:
                self.velocity.y = 1

            if collisionType == 'left':
                self.velocity.x = 0
            elif collisionType == 'right':
                self.velocity.x = 0
            

            if collisionType == 'top':
                self.velocity.y = 0

            elif collisionType == 'bottom':
                self.velocity.y = 0

            if collisionType == 'top left':
                self.velocity = pygame.math.Vector2()
            elif collisionType == 'top right':
                self.velocity = pygame.math.Vector2()
            elif collisionType == 'bottom left':
                self.velocity = pygame.math.Vector2()
            elif collisionType == 'bottom right':
                self.velocity = pygame.math.Vector2()


        else:
            self.velocity = pygame.math.Vector2()
            
    def move(self, player):
        self.escapePlayer(player)

        # move
        self.rect.x += self.velocity.x * self.speed
        self.rect.y += self.velocity.y * self.speed

        # set movement mode
        

    def checkDeath(self, player):
        if player.rect.colliderect(self.rect):
            self.kill()

    def update(self, player):
        self.move(player)