import pygame, sys, random, time
from support import import_image
from star import Star

pygame.init()
screen = pygame.display.set_mode((1040, 640))
FPS = 30
fpsClock = pygame.time.Clock()
pier = import_image('Starclicker\Image\Pier.png', (1040,640))
got_it = import_image('Starclicker\Image\gotIt.png')
stars = {}
starCount,score, duration = 0,0,30
group = pygame.sprite.Group()
font = pygame.font.Font('joystix\joystix monospace.ttf',10)
bgm = pygame.mixer.Sound('Starclicker\star_music.wav')
click = pygame.mixer.Sound('Starclicker\\bling.wav')
t1 = time.time()

while True:
    bgm.play()
    dt = round(time.time() - t1, 5)
    if dt > duration:
        print(score)
        break
    pygame.mouse.set_visible(False)
    deleting = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            for star in stars.keys():
                if stars[star].clicked(mousepos):
                    click.play()
                    score += 1
                    stars[star].dead = True

    if random.randrange(0,40) == 0:
        starCount += 1
        stars[f'star{starCount}'] = Star((random.randrange(10,1030), random.randrange(10,450)), screen)
        group.add(stars[f'star{starCount}'])

    screen.blit(pier, (0,0))
    for star in stars.values():
        star.animate(0.4)
    for star in stars.keys():
        if stars[star].dead == True: deleting.append(star)
    for star in deleting:
        group.remove(stars[star])
        stars.__delitem__(star)

    print(score)
    scoreText = font.render(f'Score: {score}', True, 'white')
    scoreRect = scoreText.get_rect(topleft = (10, 10))
    timetText = font.render(f'Time: {dt} / {duration}', True, 'white')
    timeRect = timetText.get_rect(topleft = (10, 30))
    group.draw(screen)
    screen.blit(got_it, (list(pygame.mouse.get_pos())[0]-15, list(pygame.mouse.get_pos())[1]-15))
    screen.blit(scoreText, scoreRect)
    screen.blit(timetText, timeRect)
    fpsClock.tick(FPS)
    pygame.display.flip()