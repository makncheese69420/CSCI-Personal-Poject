from typing import Any
import pygame
# Coding in the enemies
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('frog_soldier.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (x,y))

    def update(self, direction):
        self.rect.x += direction