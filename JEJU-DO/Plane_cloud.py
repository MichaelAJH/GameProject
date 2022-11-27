import pygame, random
from support import import_image, move_out

class Cloud(pygame.sprite.Sprite):
    def __init__(self, pos, surface):
        super().__init__()
        self.n = random.randint(1,4)
        self.path = f'Plane\Images\cloud{self.n}.png'
        self.speed = -random.randrange(1,4)/2
        self.image = import_image(self.path, (120,30))
        self.display_surface = surface
        self.rect = self.image.get_rect(center = pos)

    def update(self):
        self.rect.x += self.speed
        if move_out(self, (1040, 640)):
            del self