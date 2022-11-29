import pygame, math
from support import import_folder, import_image

class Idle(pygame.sprite.Sprite):
    def __init__(self, pos, surface, size, path_idle='Structure\Images\Player_Idle', path_walking='Structure\Images\Character walking', path_clicked='Structure\Images\Character Map balzacc'):
        super().__init__()
        self.mode = 'idle'
        self.direction = 0
        self.frame_index = {'idle':0, 'walk':0, 'wriggle':0}
        self.move_index = 0
        self.animations = {'idle':import_folder(path_idle,size), 'walk':import_folder(path_walking,size), 'wriggle':import_folder(path_clicked,size)}
        print(self.animations)
        self.image = self.animations['idle'][round(self.frame_index['idle'])]
        self.rect = self.image.get_rect(bottomright = pos)
        self.display_surface = surface

    def animate(self, speed):
        self.animation_speed = speed
        self.frame_index[self.mode] += self.animation_speed
        if self.frame_index[self.mode] >= len(self.animations[self.mode]):
            self.frame_index[self.mode] = 0
            if self.mode == 'wriggle':
                self.mode == 'idle'
        self.image = pygame.transform.rotate(self.animations[self.mode][math.floor(self.frame_index[self.mode])], self.direction)

    def clicked(self, mousepos):
        if self.rect.topleft[0]<=mousepos[0]<=self.rect.bottomright[0] and self.rect.topleft[1]<=mousepos[1]<=self.rect.bottomright[1]:
            # print('clicked')
            return True
        else: return False

    def move(self, pos1=False, pos2=False, dur=1):
        dx, dy = (pos2[0]-pos1[0])/(dur*60), (pos2[1]-pos1[1])/(dur*60)
        self.direction = -math.degrees(math.atan(dy/dx))
        if dx <= 0:
            self.direction += 180
        if self.mode == 'wriggle':
            self.animate(0.2)
        if self.move_index == dur*60:
            self.move_index = 0
            self.mode = 'idle'
            return False
        else:
            self.mode = 'walk'
            Pos = list(self.rect.bottomright)
            Pos[0] += dx
            Pos[1] += dy
            self.rect.bottomright = tuple(Pos)
            # print(self.rect.bottomright)
            self.move_index += 1
            return True

class Describtion(pygame.sprite.Sprite):
    def __init__(self, surface, size=(300,350), path='Structure\Images\paper.png'):
        super().__init__()
        self.frame_index = {'up':0, 'down':0}
        self.image = import_image(path, size)
        self.rect = self.image.get_rect(bottomleft = (1040,640))
        self.mode = 'hide'
        self.id = 0
        self.dic = {0:'plane', 1:'manjanggool', 2:'starclicker', 3:'joosangjuli', 4:'sagaeli'}
        self.display_surface = surface
    def animate(self, speed):
        if self.mode == 'hide':
            self.rect.topright = (1040,640)
        elif self.mode == 'show':
            self.rect.bottomright = (1040,640)
        elif self.mode == 'up':
            self.animation_speed = speed
            self.frame_index[self.mode] += self.animation_speed
            if self.frame_index[self.mode] >= 10:
                self.frame_index[self.mode] = 0
                self.mode = 'show'
            self.rect.bottomright = self.frame_index[]
            