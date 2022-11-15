import pygame, sys
# from player_log import sign_in, log_in
from logger_xml import log_in, sign_in
from support import import_image
from control import Button, Input

pygame.init()
screen = pygame.display.set_mode((1040, 640))
FPS = 30
fpsClock = pygame.time.Clock()

jeju = import_image('Structure\Images\시작화면 배경.jpg', (1040,640))
font = pygame.font.Font('back-to-1982\BACKTO1982.TTF', 64)
title = font.render('Jeju-Do', True, 'white')
titleRect = title.get_rect(center=(520, 120))

interactions = pygame.sprite.Group()
id_input = Input((900, 55), (520, 250), screen)
ps_input = Input((900, 55), (520, 320), screen)
signIn_button = Button((400, 120), (250, 420), screen, 'Sign In')
logIn_button = Button((400, 120), (780, 420), screen, 'Log In')
interactions.add(id_input, ps_input, signIn_button, logIn_button)
player_id, password = '', ''

while True:
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
            sign_in(player_id, password)
        if logIn_button.clicked(mouse, event.type):
            log_in(player_id, password)


    screen.blit(jeju, (0,0))
    screen.blit(title, titleRect)
    
    interactions.draw(screen)
    id_input.update(player_id, screen)
    ps_input.update(password, screen)
    signIn_button.update()
    logIn_button.update()

    fpsClock.tick(FPS)
    pygame.display.flip()