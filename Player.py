import pygame
import Projectile
import GameUtilities
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW= (255, 255, 0)
PURPLE= (255, 0, 255)

GRAVITY = 1



class Player(pygame.sprite.Sprite):
    def __init__(self, game,x,y):
#         x,y
#         top, left, bottom, right
#         topleft, bottomleft, topright, bottomright
#         midtop, midleft, midbottom, midright
#         center, centerx, centery
#         size, width, height
#         w,h
        pygame.sprite.Sprite.__init__(self)
        


        self.load_sprites()
        self.last_update = 0
        self.current_frame=0
        self.image = self.sprite_stand_right
#         self.image = pygame.Surface((30, 40))
#         self.image.fill(PURPLE)

        self.rect = self.image.get_rect()
        self.game = game
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.character_direction = "right"
        self.character_status ="idle"
        self.last = pygame.time.get_ticks()
        self.can_shoot=300
        
    def load_sprites(self):
        
        self.sprite_walk_right=[]
        self.sprite_walk_left=[]
        
#         sprite_sheet = GameUtilities.SpriteSheet("img/astroboy_sheet.png")
#         self.sprite_stand_right =sprite_sheet.get_image(2, 17, 29,41)
        sprite_sheet = GameUtilities.SpriteSheet("img/p3_spritesheet.png")
        self.sprite_stand_right =sprite_sheet.get_image(67, 196, 66,92)
        
        #idle stand left/right
        scale_x=int(self.sprite_stand_right.get_width())
        scale_y=int(self.sprite_stand_right.get_height())
        self.sprite_stand_right = pygame.transform.scale(self.sprite_stand_right,(scale_x,scale_y))

        self.sprite_stand_left= pygame.transform.flip(self.sprite_stand_right, True, False)
        
        #jumping
        self.sprite_jump_right =sprite_sheet.get_image(438, 93, 67,94)
        self.sprite_jump_left= pygame.transform.flip(self.sprite_jump_right, True, False)
        
        #walk left/right
#         for x in range (0,146,73):
        for x in range (0,288,73):    
            frame = sprite_sheet.get_image(x, 0, 72, 97)
            self.sprite_walk_right.append(frame)
            frame = pygame.transform.flip(frame, True, False)
            self.sprite_walk_left.append(frame)
    
    def animate_sprites(self):
#         pass

        now = pygame.time.get_ticks()
        
        if self.speed_x == 0 and not self.character_status=="jumping":
            self.character_status="idle"
        if self.speed_x != 0 and not self.character_status=="jumping":
            self.character_status = "walking"
#             print"we walking"
        if self.speed_y > 0 and not self.character_status=="jumping":
            self.character_status=="jumping"
        
        #if idle stop moving    
        if self.character_status=="idle":
                if self.character_direction == 'right':
                    self.image = self.sprite_stand_right
                else:
                    self.image = self.sprite_stand_left      
                         
        #if working start walking animation
        if self.speed_y != 0:
            if self.character_direction == 'right':
                self.image = self.sprite_jump_right
            else:
                self.image = self.sprite_jump_left   
        elif self.character_status == "walking" and not self.character_status=="jumping":
#         if self.speed_x != 0 and self.speed_y == 0:
            if now - self.last_update > 75:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % 4
                if self.character_direction == 'right':
                    self.image = self.sprite_walk_right[self.current_frame]
                else:
        
                    self.image = self.sprite_walk_left[self.current_frame]
        #if jumping
        
        
    
    def jump(self):
#         if self.character_direction == "left":
#             self.image = self.sprite_jump_left
#         elif self.character_direction == "right":
#             self.image = self.sprite_jump_right
            
        self.rect.y += 8
        if self.rect.y > 0:
            hit_list = pygame.sprite.spritecollide(self, self.game.platforms, False)
                 
        self.rect.y -= 8
        if hit_list:
            self.character_status == "jumping"
            self.speed_y = -20
            
    def shoot(self):
        
        if self.character_direction == "left":
            bullet = Projectile.Bullet(self,self.rect.top+5,self.rect.left-10,self.character_direction)
            self.game.all_sprites.add(bullet)
            self.game.bullets.add(bullet)
        elif self.character_direction == "right":
            bullet = Projectile.Bullet(self,self.rect.top+5,self.rect.left+30,self.character_direction)
            self.game.all_sprites.add(bullet)
            self.game.bullets.add(bullet)

        
            
    def check_collision(self, character_direction):
        if character_direction == 'x':
            hit_list = pygame.sprite.spritecollide(self, self.game.platforms, False)
            if hit_list:
                if self.speed_x > 0:
                    self.rect.right = hit_list[0].rect.left
#                     self.character_direction = "left"
                elif self.speed_x < 0:
                    self.rect.left = hit_list[0].rect.right
#                     self.character_direction = "right"
                self.speed_x *= -1
        if character_direction == 'y':
            hit_list = pygame.sprite.spritecollide(self, self.game.platforms, False)
            if hit_list:
                if self.speed_y > 0:
#                     self.character_status="jumping"
                    self.rect.bottom = hit_list[0].rect.top
                elif self.speed_y < 0:
                    self.rect.top = hit_list[0].rect.bottom
                self.speed_y = 0            
        
    def update(self):
        self.animate_sprites()
        self.speed_x = 0
        self.speed_y += GRAVITY
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.character_direction = "left"
#             self.image = self.sprite_stand_left
            self.speed_x = -15
        if keys_pressed[pygame.K_RIGHT]:
            self.character_direction = "right"
#             self.image = self.sprite_stand_right
            self.speed_x = 15
        if keys_pressed[pygame.K_z]:
#             helloo=hello.Bullet(self,self.rect.top+10,self.rect.left+30,self.character_direction)
#             game.all_sprites.add(helloo)
#             game.bullets.add(helloo)
            
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