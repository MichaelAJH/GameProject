# 1- import module
import pygame
import random

# 2- reset game variables
    # 2.1- game screen
pygame.init()
screen = pygame.display.set_mode((960, 640))
    # 2.2- time variables
FPS = 30
fpsClock = pygame.time.Clock()
    # 2.3 image variables
def load_image(path, width = False, height = False):
    if width and height:
        return pygame.transform.scale(pygame.image.load(path), (width, height))
    else:
        return pygame.image.load(path)
plane = load_image('Images\plane.png')
cloud = load_image('Images\cloud.png')
sky = load_image('Images\\background.png', 960, 640)
# bird = 
    # 2.4 movement variables
g = 