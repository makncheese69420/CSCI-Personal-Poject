import pygame
class Player(pygame.sprite.Sprite): #Creates the player character
    def __init__(self, postiton, xlimit, speed): #Setting character position
        super().__init__()
        self.image = pygame.image.load('BossWalking_01.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = postiton)
        self.speed = speed
        self.max_x_limit = xlimit
    
    def player_input(self): # Obtaining character movement.
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

    def limit(self): # Setting limit so player cant go off screen
        if self.rect.left <=0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_limit:
            self.rect.right = self.max_x_limit

    
    def update(self): # updates player position via input
        self.player_input()
        self.limit()