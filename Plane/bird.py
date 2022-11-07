import pygame, math, random
from support import import_folder
from mechanisms import move_out

class Bird(pygame.sprite.Sprite):
    def __init__(self, pos, surface):
        super().__init__()
        self.import_character_assets()
        self.speed = -4
        self.frame_index = 0
        self.image = self.animations[round(self.frame_index)]
        self.rect = self.image.get_rect(center = pos)
        self.display_surface = surface
    
    def import_character_assets(self):
        character_path = 'Plane\Images\\birds'
        self.animations = import_folder(character_path)
        print(self.animations)

    def animate(self, speed):
        self.animation_speed =speed
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animations):
            self.frame_index = 0
        self.image = self.animations[math.floor(self.frame_index)]
        self.rect.x += self.speed

    def update(self):
        if move_out(self, (1040, 640)):
            del self