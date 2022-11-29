import pygame, sys
from settings import * 
from level import Level
from support import *

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)
sky = import_image('ManjangGool\graphics\\background\\background.png', (screen_width, screen_height))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	if(level.player.sprite.rect.centery > screen_height+50):
		pygame.quit()
		sys.exit()
	
	screen.blit(sky, (0,0))
	level.run(pygame.time.get_ticks())
 

	pygame.display.update()
	clock.tick(60)