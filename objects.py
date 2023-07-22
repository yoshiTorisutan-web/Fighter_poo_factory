import pygame
from config import PLAYER_SIZE, ENEMY_SIZE, WHITE, RED, GREEN

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load('images/archer.png')
        self.image = pygame.transform.scale(self.image, (PLAYER_SIZE, PLAYER_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def move(self, x, y):
        self.rect.move_ip(x, y)

class Enemy:
    def __init__(self, x, y, speed):
        self.image = pygame.image.load('images/enemy.png')
        self.image = pygame.transform.scale(self.image, (ENEMY_SIZE, ENEMY_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def move(self):
        self.rect.move_ip(0, self.speed)

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.image.load('images/arrow.png')
        self.image = pygame.transform.scale(self.image, (10, 20))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def move(self):
        self.rect.move_ip(0, -5)
