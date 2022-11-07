import pygame, sys, random
from support import import_folder
from bird import Bird
from mechanisms import appear

pygame.init()
screen = pygame.display.set_mode((960, 640))
clock = pygame.time.Clock()
sky = pygame.image.load('Plane\Images\\background.png')
sky = pygame.transform.scale(sky, (1040, 640))

birds = {}
birdCount = 2
birds['bird1'] = Bird((1100, 300), screen)
group = pygame.sprite.Group()
group.add(birds['bird1'])

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
    for bird in birds.values():
        bird.animate(0.1)
        bird.update()
    group.draw(screen)

    clock.tick(30)
    pygame.display.flip()