import pygame, sys, random
from support import import_image
from plane import Plane
from bird import Bird
from cloud import Cloud
from mechanisms import collide

pygame.init()
screen = pygame.display.set_mode((1040, 640))
FPS = 30
fpsClock = pygame.time.Clock()
plane = Plane((100, 100), screen, (90, 45))
birds, clouds = {}, {}
birdCount, cloudCount = 2, 2
birds['bird1'] = Bird((1100, 300), screen)
clouds['cloud1'] = Cloud((1000, 250), screen)
group = pygame.sprite.Group()
group.add(plane, birds['bird1'], clouds['cloud1'])
sky = import_image('Images\\background.png', (1040, 640))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if random.randrange(0,120) == 0:
        clouds[f'cloud{cloudCount}'] = Cloud((1100, random.randrange(200, 400)), screen)
        group.add(clouds[f'cloud{cloudCount}'])    
        cloudCount += 1
        print(clouds)
  
    if random.randrange(0,60) == 0:
        birds[f'bird{birdCount}'] = Bird((1100, random.randrange(20, 600)), screen)
        group.add(birds[f'bird{birdCount}'])    
        birdCount += 1

    screen.blit(sky, (0,0))
    for bird in birds.values():
        bird.animate(0.5)
        bird.update()
        if collide(plane, bird):
            pygame.quit()
            sys.exit()
    for cloud in clouds.values():
        cloud.update()
    plane.apply_gravity()
    plane.update()
    group.draw(screen)

    fpsClock.tick(FPS)
    pygame.display.flip()