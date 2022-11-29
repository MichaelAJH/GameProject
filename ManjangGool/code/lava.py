import pygame 
from support import import_folder
from settings import *

class Lava(pygame.sprite.Sprite):
	def __init__(self,pos):
		super().__init__()
		self.import_lava_assets()
		self.frame_index = 0
		self.animation_speed = 0.15
		self.image = self.animation[self.frame_index]
		self.image = pygame.transform.scale(self.image,(screen_width,30))
		self.rect = self.image.get_rect(bottomleft = pos)

	def import_lava_assets(self):
		lava_path = 'ManjangGool\graphics\\background\lava'
		self.animation = import_folder(lava_path)

	def animate(self):
		self.frame_index += self.animation_speed
		if self.frame_index >= len(self.animation):
			self.frame_index = 0

		self.image = self.animation[int(self.frame_index)]
		self.image = pygame.transform.scale(self.image,(screen_width,100))

	def update(self):
		self.animate()
		