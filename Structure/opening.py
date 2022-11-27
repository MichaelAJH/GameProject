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
player_id, password = '', ''
play = 'opening'

def opening():
    global jeju, font, title, titleRect, play, player_id, password, sprites1, id_input, ps_input, signIn_button, logIn_button
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
    global jeju, font, title, titleRect, play, sprites2, newG_button, history_button, logOut_button
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
sprites3 = pygame.sprite.Group()
character_idle = Idle((250, 555), screen, (60,60))
sprites3.add(character_idle)

def levels(type = 'new'):
    global jeju_map, font, title, titleRect, play
    past, level = 0, 0
    levels = [(250,555), (330,400), (420,444), (600,600)]
    moving = False
    while play == 'levels':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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
        character_idle.animate(0.2)
        if moving:
            moving = character_idle.move(levels[past], levels[level])
        sprites3.draw(screen)
        # screen.blit(character_idle.image, character_idle.rect.bottomright)
        print(level, moving, character_idle.rect.bottomright)
        fpsClock.tick(FPS)
        pygame.display.flip()

if __name__=='__main__':
    opening()