import pygame
pygame.init()

display = pygame.display.setmode((800,600))
framerate_clock = pygame.time.Clock()

while True:
    display.fill(0,0,0)

    framerate_clock.tick(60)
    pygame.display.update