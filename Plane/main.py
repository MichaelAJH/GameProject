import pygame, sys, random
from support import import_image
from plane import Plane
from bird import Bird
from mechanisms import collide

pygame.init()
screen = pygame.display.set_mode((1040, 640))
FPS = 30
fpsClock = pygame.time.Clock()
plane = Plane((100, 100), screen, (80, 40))
birds = {}
birdCount = 2
birds['bird1'] = Bird((1100, 300), screen)
group = pygame.sprite.Group()
group.add(plane)
group.add(birds['bird1'])
sky = import_image('Plane\Images\\background.png', (1040, 640))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if random.randrange(0,60) == 0:
        birds[f'bird{birdCount}'] = Bird((1100, random.randrange(20, 600)), screen)
        group.add(birds[f'bird{birdCount}'])    
        birdCount += 1

    screen.blit(sky, (0,0))
    plane.apply_gravity()
    plane.update()
    for bird in birds.values():
        bird.animate(0.1)
        bird.update()
        if collide(plane, bird):
            pygame.quit()
            sys.exit()
    group.draw(screen)

    fpsClock.tick(FPS)
    pygame.display.flip()