import pygame
from support import import_image

class Plane(pygame.sprite.Sprite):
    def __init__(self, pos, surface, scale = False):
        super().__init__()
        self.image = import_image('Plane\Images\plane.png', scale)
        self.rect = self.image.get_rect(topleft = pos)
        self.display_surface = surface

        self.direction = [0,0]
        self.jump_speed = -6
        self.gravity = 0.6

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.jump()

    def apply_gravity(self):
        self.direction[1] += self.gravity
        self.rect.y += self.direction[1]

    def jump(self):
        self.direction[1] = self.jump_speed

    def update(self):
        self.get_input()