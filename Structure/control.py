import pygame
from support import import_image

jeju = import_image('Structure\Images\시작화면 배경.jpg', (1040,640))

def scprint(text, screen, pos=(520,540), background=jeju, fontsize=22, font='freesansbold.ttf'):
    screen.blit(background, (0,0))
    Font = pygame.font.Font(font, fontsize)
    Text = Font.render(text, True, 'red', 'white')
    TextRect = Text.get_rect(center=pos)
    screen.blit(Text, TextRect)

class Button(pygame.sprite.Sprite):
    def __init__(self, size, pos, surface, text, fontsize= 32, font='joystix\joystix monospace.ttf', path='Structure\Images\\button_1.png'):
        super().__init__()
        self.image = import_image(path, size)
        self.rect = self.image.get_rect(center=pos)
        self.xl, self.yl = self.rect.topleft
        self.xt, self.yt = self.rect.bottomright
        self.text = text
        self.display_suface = surface
        self.font = pygame.font.Font(font, fontsize)
        self.isClicked = False
        self.click = pygame.mixer.Sound('music\clicked.mp3')

        self.Text = self.font.render(self.text, True, 'black')
        self.TextRect = self.Text.get_rect(center=pos)

    def clicked(self, mousepos, eType):
        if self.xl<=mousepos[0]<=self.xt and self.yl<=mousepos[1]<=self.yt and eType==pygame.MOUSEBUTTONDOWN:
            self.click.play()
            return True
    
    def update(self):
        self.display_suface.blit(self.Text, self.TextRect)


class Input(pygame.sprite.Sprite):
    def __init__(self, size, pos, surface, fontsize=16, font='freesansbold.ttf', path='Structure\Images\input.png'):
        super().__init__()
        self.image = import_image(path, size)
        self.pos = pos
        self.rect = self.image.get_rect(center=self.pos)
        self.xl, self.yl = self.rect.topleft
        self.xt, self.yt = self.rect.bottomright       
        self.display_surface = surface
        self.font = pygame.font.Font(font, fontsize)
        self.click = pygame.mixer.Sound('music\clicked.mp3')

    def clicked(self, mousepos, eType):
        if self.xl<=mousepos[0]<=self.xt and self.yl<=mousepos[1]<=self.yt and eType==pygame.MOUSEBUTTONDOWN:
            self.click.play()
            return True
    
    def update(self,text, surface):
        self.text = self.font.render(text, True, 'black')
        self.TextRect = self.text.get_rect(center=self.pos)
        surface.blit(self.text, self.TextRect)