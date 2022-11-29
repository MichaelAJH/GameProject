import pygame 
from support import *
import random

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,size):
		super().__init__()
		self.life = pos[0]
		self.image = import_image('../graphics/background/tile.png', (size,size))
		self.rect = self.image.get_rect(topleft = pos)

	def update(self,x_shift, time):
		if(time>self.life*10):
			self.rect.y += 2
		self.rect.x += x_shift