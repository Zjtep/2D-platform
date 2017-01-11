import pygame
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW= (255, 255, 0)
PURPLE= (255, 0, 255)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, game,x,y,dir):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 5))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.top= x
        self.rect.left= y
        #g
        if dir == "right":
            self.speed_x = 12
        elif dir =="left":
            self.speed_x = -12
#         self.speed_x = 0
        self.speed_y = 0

            
    def check_collision(self):
        pass
           
    def update(self):    
        self.rect.x += self.speed_x
#         self.check_collision('x')
        self.rect.y += self.speed_y
        self.check_collision()