from os import walk
import pygame

def import_folder(path):
	surface_list = []

	for _,__,img_files in walk(path):
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)

	return surface_list

def import_image(path, scale = False, rotation = False):
    if not rotation:
        if scale:
            return pygame.transform.scale(pygame.image.load(path), scale)
        else:
            return pygame.image.load(path)
    else:
        if scale:
            return pygame.transform.rotate(pygame.transform.scale(pygame.image.load(path), scale), rotation)
        else:
            return pygame.transform.rotate(pygame.image.load(path), rotation)
