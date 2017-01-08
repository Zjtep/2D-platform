# Pygame template - skeleton for a new pygame project
import pygame
import random

TITLE = "PipedPipper"
WIDTH = 500
HEIGHT = 500
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW= (255, 255, 0)
PURPLE= (255, 0, 255)

GRAVITY = 1

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
#         x,y
#         top, left, bottom, right
#         topleft, bottomleft, topright, bottomright
#         midtop, midleft, midbottom, midright
#         center, centerx, centery
#         size, width, height
#         w,h

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 60))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.top= WIDTH / 4 +2
        self.rect.left= HEIGHT/4 +250
        self.speed_x = 0
        self.speed_y = 0
    def jump(self):
        self.rect.y += 2
        if self.rect.y > 0:
            hit_list = pygame.sprite.spritecollide(self, self.game.platforms, False)
                 
        self.rect.y -= 2
        if hit_list:
            self.speed_y = -20
            
    def check_collision(self, dir):
        if dir == 'x':
            hit_list = pygame.sprite.spritecollide(self, game.platforms, False)
            if hit_list:
                if self.speed_x > 0:
                    self.rect.right = hit_list[0].rect.left
                    self.dir = 'l'
                elif self.speed_x < 0:
                    self.rect.left = hit_list[0].rect.right
                    self.dir = 'r'
                self.speed_x *= -1
        if dir == 'y':
            hit_list = pygame.sprite.spritecollide(self, game.platforms, False)
            if hit_list:
                if self.speed_y > 0:
                    self.rect.bottom = hit_list[0].rect.top
                elif self.speed_y < 0:
                    self.rect.top = hit_list[0].rect.bottom
                self.speed_y = 0            
        
    def update(self):
        self.speed_x = 0
        self.speed_y += GRAVITY
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.speed_x = -5
        if keys_pressed[pygame.K_RIGHT]:
            self.speed_x = 5
        if keys_pressed[pygame.K_SPACE]:
                self.jump()
                
        self.rect.x += self.speed_x
        self.check_collision('x')
        self.rect.y += self.speed_y
        self.check_collision('y')

class Game:
# initialize pygame and create window
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
  
        
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        
        self.player = Player(self)
        self.all_sprites.add(self.player)
        
#      (self, x, y, w, h):
        plat = Platform(0, HEIGHT - 40, WIDTH, 40)
        self.all_sprites.add(plat)
        self.platforms.add(plat)
        
        plat2 = Platform(300, 300, 100, 40)
        self.all_sprites.add(plat2)
        self.platforms.add(plat2)
        
        plat3 = Platform(0, HEIGHT-450, 40, 500)
        self.all_sprites.add(plat3)
        self.platforms.add(plat3)
        
        plat4 = Platform(200, HEIGHT-150, 40, 100)
        self.all_sprites.add(plat4)
        self.platforms.add(plat4)

    def run(self):
        # Game loop
        self.running = True
        self.new()
        while self.running:
             self.clock.tick(FPS)
             self.events()
             self.update()
             self.draw()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()
   
    def update(self):
        self.all_sprites.update()
        
        hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            self.player.speed_y = 0
            self.player.rect.bottom = hits[0].rect.top
    
    def draw(self):
         # Draw / render
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

game = Game()
while True:
  
    game.run()
    

