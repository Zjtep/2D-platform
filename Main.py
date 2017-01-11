# Pygame template - skeleton for a new pygame project
import pygame
import random
import pygame._view

TITLE = "PipedPipper"
WIDTH = 800
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

class Bullet(pygame.sprite.Sprite):
    def __init__(self, game,x,y,dir):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 5))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.top= x
        self.rect.left= y
        
        if dir == "right":
            self.speed_x = 7
        elif dir =="left":
            self.speed_x = -7
#         self.speed_x = 0
        self.speed_y = 0

            
    def check_collision(self):
#         if dir == 'x':
        hit_list = pygame.sprite.spritecollide(self, game.platforms, False)
        if hit_list:
            self.kill()
#         hit_list = pygame.sprite.spritecollide(self, game.enemys, False)
#         if hit_list:
#             print "Bullet killed"
#             self.kill()        
           
        
    def update(self):    
        self.rect.x += self.speed_x
#         self.check_collision('x')
        self.rect.y += self.speed_y
        self.check_collision()
        

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game,x,y):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.top= x
        self.rect.left= y
        self.speed_x = 2
#         self.speed_x = 0
        self.speed_y = 0

            
    def check_collision(self, dir):
        if dir == 'x':
            hit_list = pygame.sprite.spritecollide(self, game.platforms, False)
            if hit_list:
                if self.speed_x > 0:
                    self.rect.right = hit_list[0].rect.left
                    self.dir = 'left'
                elif self.speed_x < 0:
                    self.rect.left = hit_list[0].rect.right
                    self.dir = 'right'
                self.speed_x *= -1
        if dir == 'y':
            hit_list = pygame.sprite.spritecollide(self, game.platforms, False)
            if hit_list:
                if self.speed_y > 0:
                    self.rect.bottom = hit_list[0].rect.top
                elif self.speed_y < 0:
                    self.rect.top = hit_list[0].rect.bottom
                self.speed_y = 0            
#         hit_list = pygame.sprite.spritecollide(self, game.bullets, False)
#         if hit_list:
#             print "enemy killed"
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
        self.image = pygame.Surface((30, 40))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.top= WIDTH / 4 +2
        self.rect.left= HEIGHT/4 +250
        self.speed_x = 0
        self.speed_y = 0
        self.dir = "right"
        self.last = pygame.time.get_ticks()
        self.can_shoot=300
        
    def jump(self):
        self.rect.y += 2
        if self.rect.y > 0:
            hit_list = pygame.sprite.spritecollide(self, self.game.platforms, False)
                 
        self.rect.y -= 2
        if hit_list:
            self.speed_y = -15
            
    def shoot(self):
        
        if self.dir == "left":
            bullet = Bullet(self,self.rect.top+10,self.rect.left-10,self.dir)
            game.all_sprites.add(bullet)
            game.bullets.add(bullet)
        elif self.dir == "right":
            bullet = Bullet(self,self.rect.top+10,self.rect.left+30,self.dir)
            game.all_sprites.add(bullet)
            game.bullets.add(bullet)

        
            
    def check_collision(self, dir):
        if dir == 'x':
            hit_list = pygame.sprite.spritecollide(self, game.platforms, False)
            if hit_list:
                if self.speed_x > 0:
                    self.rect.right = hit_list[0].rect.left
                    self.dir = "left"
                elif self.speed_x < 0:
                    self.rect.left = hit_list[0].rect.right
                    self.dir = "right"
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
            self.dir = "left"
            self.speed_x = -5
        if keys_pressed[pygame.K_RIGHT]:
            self.dir = "right"
            self.speed_x = 5
        if keys_pressed[pygame.K_z]:
            self.jump()
            
        if keys_pressed[pygame.K_x]:
            now = pygame.time.get_ticks()
            if now - self.last >= self.can_shoot:
                self.last = now
                self.shoot()    
            
                
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
        self.enemys = pygame.sprite.Group()
        
        self.bullets = pygame.sprite.Group()
        bullet = Bullet(self,200,200,"right")
        self.all_sprites.add(bullet)
        self.bullets.add(bullet)
        

        bullet1 = Bullet(self,10,450,"right")
        self.all_sprites.add(bullet1)
        self.bullets.add(bullet1)
        
        self.player = Player(self)
        self.all_sprites.add(self.player)
        
        enemy = Enemy(self,200,300)
        self.all_sprites.add(enemy)
        self.enemys.add(enemy)
        
        enemy2 = Enemy(self,200,100)
        self.all_sprites.add(enemy2)
        self.enemys.add(enemy2)
#      (self, x, y, w, h):
        plat = Platform(0, HEIGHT - 10, WIDTH, 10)
        self.all_sprites.add(plat)
        self.platforms.add(plat)
        
        plat2 = Platform(300, 300, 100, 10)
        self.all_sprites.add(plat2)
        self.platforms.add(plat2)
        
        plat3 = Platform(0, HEIGHT-450, 10, 500)
        self.all_sprites.add(plat3)
        self.platforms.add(plat3)
        
        plat4 = Platform(200, HEIGHT-100, 20, 50)
        self.all_sprites.add(plat4)
        self.platforms.add(plat4)
        
        plat5 = Platform(WIDTH-10, HEIGHT-450, 10, 500)
        self.all_sprites.add(plat5)
        self.platforms.add(plat5)

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
        
        hits = pygame.sprite.groupcollide(self.enemys, self.bullets, True, True)
#         hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
#         if hits:
#             self.player.speed_y = 0
#             self.player.rect.bottom = hits[0].rect.top
    
    def draw(self):
         # Draw / render
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

game = Game()
while True:
  
    game.run()
    

