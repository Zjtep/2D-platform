import pygame

class SpriteSheet:
    """Utility class to load and parse spritesheets"""
    def __init__(self,filename):
       self.sheet = pygame.image.load(filename).convert()

    def get_image(self, x, y, width, height):

        SPRITE_START_X=x  
        SPRITE_START_Y=y
        SPRIT_SIZE_X=width
        SPRIT_SIZE_Y=height
        
        self.sheet.set_clip(pygame.Rect(SPRITE_START_X, SPRITE_START_Y, SPRIT_SIZE_X, SPRIT_SIZE_Y)) #Locate the sprite you want
        draw_me = self.sheet.subsurface(self.sheet.get_clip()) #Extract the sprite you want
        
        color = self.sheet.get_at((0,0)) #we get the color of the upper-left corner pixel
        draw_me.set_colorkey(color)
#         draw_me.set_colorkey([0, 0, 0]) #Make that shit transparent
        
        return draw_me