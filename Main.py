# Pygame template - skeleton for a new pygame project
import pygame
import random
import pygame._view
# import hello
import Projectile
import Enemy
import Player

TITLE = "PipedPipper"
WIN_WIDTH = 800
WIN_HEIGHT = 600
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


class Game:
# initialize pygame and create window
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
#         self.platform_list = []
        
    def new(self):
                
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        
        
        x = y = 0
        map01 = [
            "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
            "P                                P",
            "P                                P",
            "P                                P",
            "P                                P",
            "P                 PP             P",
            "P                      PPPPP     P",
            "P   PP       P                   P",
            "P                                P",
            "P                PPPPP           P",
            "PPE                              P",
            "PPP       PPPPP                  P",
            "PPPP                     PPPPPPPPP",
            "PPPPP                            P",
            "PPPPPPP E                        P",
            "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
        # build the level
        for row in map01:
            for col in row:
                if col == "P":
                    p = Platform(x, y,32,32)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
#                     self.platform_list.append(p)
                    
                if col == "E":
                    e = Enemy.BasicMob(self,x,y)
                    self.all_sprites.add(e)
                    self.enemys.add(e)
#                     self.platform_list.append(e)
                    
                x += 32
            y += 32
            x = 0        
              
#         bullet = Projectile.Bullet(self,200,200,"right")
#         self.all_sprites.add(bullet)
#         self.bullets.add(bullet)
        

#         bullet1 = Projectile.Bullet(self,10,450,"right")
#         self.all_sprites.add(bullet1)
#         self.bullets.add(bullet1)
        
        self.player1 = Player.Player(self,50,50)
        self.all_sprites.add(self.player1)
        
#         enemy1 = Enemy.BasicMob(self,200,300)
#         self.all_sprites.add(enemy1)
#         self.enemys.add(enemy1)
#         
#         enemy2 = Enemy.BasicMob(self,200,100)
#         self.all_sprites.add(enemy2)
#         self.enemys.add(enemy2)
#      (self, x, y, w, h):
#         plat = Platform(0, WIN_HEIGHT - 10, WIN_WIDTH, 10)
#         self.all_sprites.add(plat)
#         self.platforms.add(plat)
#         
#         plat2 = Platform(300, 300, 100, 10)
#         self.all_sprites.add(plat2)
#         self.platforms.add(plat2)
#         
#         plat3 = Platform(0, WIN_HEIGHT-450, 10, 500)
#         self.all_sprites.add(plat3)
#         self.platforms.add(plat3)
#         
#         plat4 = Platform(200, WIN_HEIGHT-100, 20, 50)
#         self.all_sprites.add(plat4)
#         self.platforms.add(plat4)
#         
#         plat5 = Platform(WIN_WIDTH-10, WIN_HEIGHT-450, 10, 500)
#         self.all_sprites.add(plat5)
#         self.platforms.add(plat5)

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
        hits = pygame.sprite.groupcollide(self.platforms, self.bullets, False, True)
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
    

