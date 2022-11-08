import pygame, sys
from support import import_image
from mechanisms import move_out

class Plane(pygame.sprite.Sprite):
    def __init__(self, pos, surface, scale = False):
        super().__init__()
        self.scale = scale
        self.image = import_image('Images\plane.png', scale)
        self.rect = self.image.get_rect(topleft = pos)
        self.display_surface = surface

        self.direction = [0,0]
        self.jump_speed = -7
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
        self.angle = -1.5*self.direction[1]
        self.image = import_image('Images\plane.png', self.scale, self.angle)
        if move_out(self, (1040, 640)):
            pygame.quit()
            sys.exit()