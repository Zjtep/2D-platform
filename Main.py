# Pygame template - skeleton for a new pygame project
import pygame
import random

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
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.top= WIDTH / 4 +2
        self.rect.left= HEIGHT/4 +250
        self.vx = 0
        self.vy = 0
    def jump(self):
        self.rect.y += 2
        hits = pygame.sprite.spritecollide(self, self.game.plats, False)
        self.rect.y -= 2
        if hits:
            self.vy = -20
        
    def update(self):
        self.vx = 0
        self.vy += GRAVITY
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.vx = -5
        if keys_pressed[pygame.K_RIGHT]:
            self.vx = 5
        if keys_pressed[pygame.K_SPACE]:
                self.jump()
                
        self.rect.x += self.vx
        self.rect.y += self.vy


class Game:
# initialize pygame and create window
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("PipedPipper")
        self.clock = pygame.time.Clock()
  
        
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.plats = pygame.sprite.Group()
        
        self.player = Player(self)
        self.all_sprites.add(self.player)
        
#      (self, x, y, w, h):
        plat = Platform(0, HEIGHT - 40, WIDTH, 40)
        self.all_sprites.add(plat)
        self.plats.add(plat)
        
        plat2 = Platform(300, 300, 100, 40)
        self.all_sprites.add(plat2)
        self.plats.add(plat2)

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
        
        hits = pygame.sprite.spritecollide(self.player, self.plats, False)
        if hits:
            self.player.vy = 0
            self.player.rect.bottom = hits[0].rect.top
    
    def draw(self):
         # Draw / render
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

game = Game()
while True:
  
    game.run()
    

