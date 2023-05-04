import pygame
import sys
from random import choice
from player import Player
from enemy import Enemy
from bullet import Bullet

class Game:  # Setting up game 
    def __init__(self):  
        player_1 = Player((screen_length/ 2,screen_height), screen_length, 5)
        self.player = pygame.sprite.GroupSingle(player_1)

        #Player health and score setup
        self.health = 3
        self.health_display = pygame.image.load('bossWalking_01.png').convert_alpha()
        self.health_x_position = screen_length - (self.health_display.get_size()[0]* 2 + 20)

        self.enemies = pygame.sprite.Group()
        self.enemy_setup(rows = 6, columns = 8)
        self.enemy_direction = 1
        self.enemy_bullets = pygame.sprite.Group()


    def enemy_setup(self, rows, columns, x_offset= 70, y_offset= 100, x_distance = 60, y_distance = 48):
        for row_index, row in enumerate(range(rows)):
            for column_index, coloumn in enumerate(range(columns)):
                x = column_index * x_distance + x_offset
                y = row_index * y_distance + y_offset
                enemy_sprite = Enemy(x,y)
                self.enemies.add(enemy_sprite)

    def enemy_place_checker(self): # makes sure enemies dont escape the screen
        enemy_positions = self.enemies.sprites()
        for enemy in enemy_positions:
            if enemy.rect.right >= screen_length:
                self.enemy_direction = -1
                self.march_down(1)
            elif enemy.rect.left <= 0:
                self.enemy_direction = 1
                self.march_down(1)

    def march_down(self, distance):
        if self.enemies:
            for enemy in self.enemies.sprites():
                enemy.rect.y += distance


    def enemy_attack(self):# Enemies shooting thier lasers
        if self.enemies.sprites():
            random_enemy = choice(self.enemies.sprites())
            enemy_shot = Bullet(random_enemy.rect.center,screen_height, 6)
            self.enemy_bullets.add(enemy_shot)

    def collisions(self):
        # player bullets
        if self.player.sprite.bullets:
            for bullet in self.player.sprite.bullets:
                if pygame.sprite.spritecollide(bullet, self.enemies, True):
                    bullet.kill()
        # Enemy bullets
        if self.enemy_bullets:
            for bullet in self.enemy_bullets:
                if pygame.sprite.spritecollide(bullet,self.player, False):
                    bullet.kill()
                    self.health -= 1
                    if self.health <= 0:
                        pygame.quit()
                        sys.exit()

    def health_display_ui(self): #UI for health
        for health in range(self.health - 1): # 2, 1, 0 lives left but you dont die at 0
            x = self.health_x_position + (health * self.health_display.get_size()[0] + 10)
            screen.blit(self.health_display,(x,8))

    def victory_message(self):
        if not self.enemies.sprites():
            victory_screech = self.font.render('You Win!, You can go home now')
            victory_banner = victory_screech.get_rect(center = (screen_length / 2, screen_height/2))
            screen.blit(victory_screech, victory_banner)

    def run(self):  # Where stuff is being drawn to the screen
        self.player.update()
        
        self.enemies.update(self.enemy_direction)
        self.enemy_place_checker()
        self.enemy_bullets.update()


        self.player.draw(screen)
        self.player.sprite.bullets.draw(screen)
        self.enemies.draw(screen)
        self.enemy_bullets.draw(screen)

        self.collisions()
        self.health_display_ui()
        self.victory_message()

if __name__ == '__main__':  #Creating Driver code
    pygame.init()
    screen_length = 600
    screen_height = 600

    screen = pygame.display.set_mode((screen_length, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    Enemy_guns = pygame.USEREVENT + 1
    pygame.time.set_timer(Enemy_guns, 800)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == Enemy_guns:
                game.enemy_attack()
        
        screen.fill((30,30,30))

        game.run()

        pygame.display.flip()
        clock.tick(60) # Setting framerate