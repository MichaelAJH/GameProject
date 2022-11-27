import pygame, sys, random
from support import import_image
from star import Star

pygame.init()
screen = pygame.display.set_mode((1040, 640))
FPS = 30
fpsClock = pygame.time.Clock()
pier = import_image('Starclicker\Image\Pier.png', (1040,640))
stars = {}
starCount = 0
group = pygame.sprite.Group()

while True:
    deleting = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            for star in stars.keys():
                if stars[star].clicked(mousepos):
                    deleting.append(star)

    if random.randrange(0,5) == 0:
        starCount += 1
        stars[f'star{starCount}'] = Star((random.randrange(10,1030), random.randrange(10,630)), screen)
        group.add(stars[f'star{starCount}'])

    screen.blit(pier, (0,0))
    for star in stars.values():
        star.animate(0.5)
    for star in deleting:
        stars.__delitem__(star)
    group.draw(screen)
    fpsClock.tick(FPS)
    pygame.display.flip()