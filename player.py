import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite): #Creates the player character
    def __init__(self, postiton, xlimit, speed): #Setting character position
        super().__init__()
        self.image = pygame.image.load('BossWalking_01.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = postiton)
        self.speed = speed
        self.max_x_limit = xlimit
        self.loaded = True
        self.bullet_time = 0
        self.reload_time = 600
        self.bullets = pygame.sprite.Group()

    
    def player_input(self): # Obtaining character movement.
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.loaded: #Creating relaod time
            self.fire_gun()
            self.loaded = False
            self.bullet_time = pygame.time.get_ticks()

    def reload(self): # Allowing the player to shoot after reload time
        if not self.loaded:
            current_time = pygame.time.get_ticks()
            if current_time - self.bullet_time >= self.reload_time:
                self.loaded = True

    
    def fire_gun(self): # From extra bullet file, bullet instansializaed
        self.bullets.add(Bullet(self.rect.center, self.rect.bottom, -9))

    def limit(self): # Setting limit so player cant go off screen
        if self.rect.left <=0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_limit:
            self.rect.right = self.max_x_limit

    
    def update(self): # updates everything about the player
        self.player_input()
        self.limit()
        self.reload()
        self.bullets.update()
