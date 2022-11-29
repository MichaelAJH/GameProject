import pygame, sys
from logger_xml import log_in, sign_in
from support import import_image
from control import Button, Input
from animation import Idle

pygame.init()
screen = pygame.display.set_mode((1040, 640))
FPS = 30
fpsClock = pygame.time.Clock()

jeju = import_image('Structure\Images\시작화면 배경.jpg', (1040,640))
font = pygame.font.Font('back-to-1982\BACKTO1982.TTF', 64)
title = font.render('Jeju-Do', True, 'white')
titleRect = title.get_rect(center=(520, 120))

sprites1 = pygame.sprite.Group()
id_input = Input((900, 55), (520, 250), screen)
ps_input = Input((900, 55), (520, 320), screen)
signIn_button = Button((400, 120), (250, 420), screen, 'Sign In')
logIn_button = Button((400, 120), (780, 420), screen, 'Log In')
sprites1.add(id_input, ps_input, signIn_button, logIn_button)
bgm = pygame.mixer.Sound('Structure\main_theme.wav')
player_id, password = '', ''
play = 'opening'

def opening():
    global jeju, font, title, titleRect, play, bgm, player_id, password, sprites1, id_input, ps_input, signIn_button, logIn_button
    bgm.play()
    while play=='opening':
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if id_input.clicked(mouse, event.type): mode = 'id'
            if ps_input.clicked(mouse, event.type): mode = 'ps'
            if event.type == pygame.KEYDOWN:
                if mode == 'id':
                    if event.key == pygame.K_BACKSPACE and len(player_id)>0:
                        player_id = player_id[:-1]
                    else:
                        player_id += event.unicode
                elif mode == 'ps':
                    if event.key == pygame.K_BACKSPACE and len(player_id)>0:
                        password = password[:-1]
                    else:
                        password += event.unicode
            if signIn_button.clicked(mouse, event.type):
                sign_in(player_id, password, jeju)
            if logIn_button.clicked(mouse, event.type):
                if log_in(player_id, password, jeju) == player_id:
                    play = 'logged in'
                    logged_in()

        screen.blit(jeju, (0,0))
        screen.blit(title, titleRect)
        sprites1.draw(screen)
        id_input.update(player_id, screen)
        ps_input.update(password, screen)
        signIn_button.update()
        logIn_button.update()

        fpsClock.tick(FPS)
        pygame.display.flip()

sprites2 = pygame.sprite.Group()
newG_button = Button((400, 90), (520, 300), screen, 'New Game')
history_button = Button((400, 90), (520, 420), screen, 'Game History')
logOut_button = Button((400, 90), (520, 540), screen, 'Log Out')
sprites2.add(newG_button, history_button, logOut_button)

def logged_in():
    global jeju, font, title, titleRect, play, bgm, sprites2, newG_button, history_button, logOut_button
    while play=='logged in':
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if newG_button.clicked(mouse, event.type):
                play = 'levels'
                levels()
            if history_button.clicked(mouse, event.type):
                play = 'search_history'
            if logOut_button.clicked(mouse, event.type):
                play = 'opening'
                opening()

        screen.blit(jeju, (0,0))
        screen.blit(title, titleRect)
        sprites2.draw(screen)
        for button in sprites2:
            button.update()
        
        fpsClock.tick(FPS)
        pygame.display.flip()

jeju_map = import_image('Structure\Images\\trace.png', (1040,640))
ico_plane = import_image('Structure\Images\icon_plane.png', (100,100))
ico_mjg = import_image('Structure\Images\icon_manjanggool.png', (80,80))
ico_star = import_image('Structure\Images\icon_star.png', (80,80))
ico_jsjl = import_image('Structure\Images\icon_jusangjullee.png', (80,80))
ico_sgl = import_image('Structure\Images\icon_sagaeli.png', (80,80))
paper = import_image('Structure\Images\paper.png', (300,350))
sprites3 = pygame.sprite.Group()
character = Idle((415, 165), screen, (60,60))
sprites3.add(character)

def levels(type = 'new'):
    global jeju_map, font, title, titleRect, play
    describtion_mode = 'hide'   # hide, up, show, down
    describtion_index = 0
    past, level = 0, 0
    icons = [ico_plane, ico_mjg, ico_star, ico_jsjl, ico_sgl]
    levels = [(415, 165), (770, 170), (725, 450), (415, 535), (240, 550)]
    leveldic = {0:'plane', 1:'manjanggool', 2:'starclicker', 3:'joosangjuli', 4:'sagaeli'}
    moving = False
    while play == 'levels':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                if character.clicked(pygame.mouse.get_pos()):
                    character.mode = 'wriggle'
            if event.type == pygame.KEYDOWN:
                if moving: pass
                else:
                    if event.key == pygame.K_a:
                        moving = True
                        past,level = level, (level-1)%len(levels)
                    elif event.key == pygame.K_d:
                        moving = True
                        past,level = level, (level+1)%len(levels)

        screen.blit(jeju_map, (0,0))
        for icon in icons:
            screen.blit(icon, (levels[icons.index(icon)][0]-40,levels[icons.index(icon)][1]-80))
        character.animate(0.2)
        if moving:
            moving = character.move(levels[past], levels[level])
        sprites3.draw(screen)
        # print(level, moving, character.rect.bottomright)
        screen.blit(paper, (740,290))
        fpsClock.tick(FPS)
        pygame.display.flip()

if __name__=='__main__':
    opening()