import pygame, sys
from support import import_image
from plane import Plane

pygame.init()
screen = pygame.display.set_mode((1040, 640))
FPS = 30
fpsClock = pygame.time.Clock()
plane = Plane((100, 100), screen, (80, 40))
group = pygame.sprite.Group()
group.add(plane)
sky = import_image('Plane\Images\\background.png', (1040, 640))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(sky, (0,0))
    plane.apply_gravity()
    plane.update()
    group.draw(screen)

    pygame.display.flip()
    fpsClock.tick(FPS)