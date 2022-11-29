import pygame, sys
from settings import * 
from level import Level
from support import *

def fontWithSize(size):
	return pygame.font.Font('joystix\joystix monospace.ttf', size)

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)
background = import_image('ManjangGool/Image/background.png', (screen_width, screen_height))
bar = import_image('ManjangGool/Image/process_bar.png', (640,10))
icon = import_image('ManjangGool/Image/character/idle/0.png', (30,30))
score = 0
state = 'ready'
stateTimer = 0


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	
	screen.blit(background, (0,0))
 
	if state=='ready':
		level.run(state = 'ready')
		leftTime = (3-int(stateTimer/100))
		middleText = fontWithSize(50).render(f'{leftTime}', True, 'white')
		stateTimer += 1
		if stateTimer>=400:
			stateTimer = 0
			state = 'playing'
		middleRect = middleText.get_rect(center = (screen_width/2,screen_height/2))
		screen.blit(middleText, middleRect)
  
	if state == 'playing':
		level.run()
  
		scoreText = fontWithSize(20).render(f'Time {int(score/100)}:'+str(score%100).rjust(2,'0'), True, 'white')
		scoreRect = scoreText.get_rect(topleft = (15, 33))
		
		screen.blit(scoreText, scoreRect)
		screen.blit(bar, (200,40))
		screen.blit(icon, (int(200+level.process*(640/10600)),25))
	
		score += 1 

		if(level.player.sprite.rect.centery > screen_height+50):
			state = 'fail'
  
	if state == 'fail':
		level.run(state = 'fail')

		failText = fontWithSize(40).render(f'GameOver', True, 'white')
		failRect = failText.get_rect(center = (screen_width/2, screen_height/2))
		screen.blit(failText, failRect)
  
		subText = fontWithSize(10).render('press r to restart, h to go home', True, 'white')
		subRect = subText.get_rect(center = (screen_width/2, screen_height/2+40))
		screen.blit(subText, subRect)
  
		keys = pygame.key.get_pressed()

		if keys[pygame.K_r]:
			score = 0
			level = Level(level_map,screen)
			state='ready'
		if keys[pygame.K_h]:
			pass

  
		
	pygame.display.update()
	clock.tick(100)