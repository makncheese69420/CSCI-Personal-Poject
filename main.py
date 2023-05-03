import pygame
import sys
from player import Player

class Game:  # Setting up game 
    def __init__(self): 
        player_1 = Player((screen_length/ 2,screen_height), screen_length, 5)
        self.player = pygame.sprite.GroupSingle(player_1)

    def run(self):
        self.player.update()
        self.player.draw(screen)

if __name__ == '__main__':  #Creating Driver code
    pygame.init()
    screen_length = 600
    screen_height = 600

    screen = pygame.display.set_mode((screen_length, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill((30,30,30))

        game.run()

        pygame.display.flip()
        clock.tick(60) # Setting framerate