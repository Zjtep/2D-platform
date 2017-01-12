import pygame
import GameUtilities
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW= (255, 255, 0)
PURPLE= (255, 0, 255)
GRAVITY = 1

class BasicMob(pygame.sprite.Sprite):
    def __init__(self, game,x,y):

        pygame.sprite.Sprite.__init__(self)
    
        sprite_sheet = GameUtilities.SpriteSheet("img/enemies_spritesheet.png")
        self.slime_sprite_left =sprite_sheet.get_image(52, 125, 50,28)
       
        scale_x=self.slime_sprite_left.get_width()/2
        scale_y=self.slime_sprite_left.get_height()/2
#         self.slime_sprite_left = pygame.transform.scale(self.slime_sprite_left,(scale_x,scale_y))
        self.slime_sprite_right= pygame.transform.flip(self.slime_sprite_left, True, False)
        
        self.image = self.slime_sprite_right
                
#         self.image = pygame.Surface((30, 40))
#         self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 2
#         self.speed_x = 0
        self.speed_y = 0

            
    def check_collision(self, dir):
        if dir == 'x':
            hit_list = pygame.sprite.spritecollide(self, self.game.platforms, False)
            if hit_list:
                if self.speed_x > 0:
                    self.rect.right = hit_list[0].rect.left
                    self.image = self.slime_sprite_left
                    self.dir = 'left'
                elif self.speed_x < 0:
                    self.rect.left = hit_list[0].rect.right
                    self.image = self.slime_sprite_right
                    
                    self.dir = 'right'
                self.speed_x *= -1
        if dir == 'y':
            hit_list = pygame.sprite.spritecollide(self, self.game.platforms, False)
            if hit_list:
                if self.speed_y > 0:
                    self.rect.bottom = hit_list[0].rect.top
                elif self.speed_y < 0:
                    self.rect.top = hit_list[0].rect.bottom
                self.speed_y = 0            
#         hit_list = pygame.sprite.spritecollide(self, game.bullets, False)
#         if hit_list:
#             print "BasicMob killed"
#             self.kill()
        
    def update(self):
      
        self.speed_y += GRAVITY
#         keys_pressed = pygame.key.get_pressed()
#         if keys_pressed[pygame.K_LEFT]:
#             self.speed_x = -5
#         if keys_pressed[pygame.K_RIGHT]:
#             self.speed_x = 5
#         if keys_pressed[pygame.K_SPACE]:
#                 self.jump()
                
        self.rect.x += self.speed_x
        self.check_collision('x')
        self.rect.y += self.speed_y
        self.check_collision('y')