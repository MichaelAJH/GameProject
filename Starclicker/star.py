import pygame, math
from support import import_folder

class Star(pygame.sprite.Sprite):
    def __init__(self, pos, surface):
        super().__init__()
        self.frame_index = 0
        self.animations = import_folder('Starclicker\Image\Star')
        self.image = self.animations[0]
        self.rect = self.image.get_rect(center = pos)
        self.dead = False

    def animate(self, speed):
        self.animation_speed = speed
        self.frame_index += self.animation_speed
        if self.frame_index > 26:
            self.dead = True
        else:
            self.image = self.animations[math.floor(self.frame_index)]

    def clicked(self, mousepos):
        if self.rect.topleft[0]<=mousepos[0]<=self.rect.bottomright[0] and self.rect.topleft[1]<=mousepos[1]<=self.rect.bottomright[1]:
            print('clicked')
            return self.rect.center
        else: return False

    def update(self, mousepos):
        if self.clicked(mousepos):
            del self