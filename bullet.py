#coding the bullet
import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position,ylimit, speed ):
        super().__init__()
        self.image = pygame.Surface((4,20))
        self.image.fill('yellow')
        self.rect = self.image.get_rect(center = position)
        self.speed = speed
        self.ylimit = ylimit

    def destroy(self): # Destroys the bullet sprite when it leaves the screen
        if self.rect.y <= -50 or self.rect.y >= self.ylimit + 50:
            self.kill()
    
    def update(self):
        self.rect.y += self.speed
        self.destroy()