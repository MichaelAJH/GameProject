import pygame, math
from support import import_image, import_folder, import_folder_bypath

class Idle(pygame.sprite.Sprite):
    def __init__(self, pos, surface, size, path='Structure\Images\Character'):
        super().__init__()
        self.frame_index = 0
        self.move_index = 0
        self.animations = import_folder(path, size)
        print(self.animations)
        self.image = self.animations[round(self.frame_index)]
        self.rect = self.image.get_rect(bottomright = pos)
        self.display_surface = surface

    def animate(self, speed):
        self.animation_speed = speed
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animations):
            self.frame_index = 0
        self.image = self.animations[math.floor(self.frame_index)]

    def move(self, pos1=False, pos2=False, dur=1):
        dx, dy = (pos2[0]-pos1[0])/(dur*60), (pos2[1]-pos1[1])/(dur*60)
        if self.rect.bottomright[0]<=pos2[0] and pos2[0]<pos1[0] or self.rect.bottomright[0]>=pos2[0] and pos2[0]>=pos1[0]:
            return False
        else:
            Pos = list(self.rect.bottomright)
            Pos[0] += dx
            Pos[1] += dy
            self.rect.bottomright = tuple(Pos)
            print(self.rect.bottomright)
            return True