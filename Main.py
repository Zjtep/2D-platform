# Pygame template - skeleton for a new pygame project
import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW= (255, 255, 0)

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
        self.rect.top= WIDTH / 4
        self.rect.left= HEIGHT/4
#         self.vx = 50
#         self.vy = 50
#         self.rect.centerx = WIDTH / 2
#         self.rect.bottom = HEIGHT - 350
    def update(self):
#         self.vx = 0
#         self.vy += 1  # GRAVITY
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys_pressed[pygame.K_RIGHT]:
            self.rect.x += 5
#         self.rect.x += self.vx
#         self.rect.y += self.vy
    


class Game:
# initialize pygame and create window
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("TerribleAria")
        self.clock = pygame.time.Clock()
  
        
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)

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
    
    def draw(self):
         # Draw / render
        self.screen.fill(GREEN)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

game = Game()
while True:
  
    game.run()
    

