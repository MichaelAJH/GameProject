import pygame 
from support import *
import random

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,size):
		super().__init__()
		self.life = pos[0]
		self.image = import_image('ManjangGool/Image/tile.png', (size,size))
		self.rect = self.image.get_rect(topleft = pos)

	def update(self,x_shift):
		self.life -= 5
		if(self.life<0):
			self.rect.y += 4
		self.rect.x += x_shift