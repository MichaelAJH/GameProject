import pygame, sys

pygame.init()
screen = pygame.display.set_mode((960, 640))
clock = pygame.time.Clock()
sky = pygame.image.load('Plane\Images\\background.png')
sky = pygame.transform.scale(sky, (1040, 640))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    screen.blit(sky, (0,0))
    clock.tick(30)
    pygame.display.flip()