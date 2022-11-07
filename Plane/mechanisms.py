import pygame, random

def appear(probability, range):
    pass

def collide(sprite1, sprite2):
    if sprite1.rect.colliderect(sprite2.rect):
        return True
    else:
        return False

def move_out(sprite, range):
    if sprite.rect.x < -50 or sprite.rect.x > range[0]+200:
        return True
    if sprite.rect.y < -50 or sprite.rect.y > range[1]:
        return True
    else:
        return False