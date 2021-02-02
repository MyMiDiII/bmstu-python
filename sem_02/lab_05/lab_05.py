'''
    Лабораторная работа №5
    "Анимация с помощью pygame"
'''

import pygame
import os

FPS = 50
WIN_H = 1005
WIN_W = 1920
SHIFT = 8

pygame.init()

now = pygame.display.set_mode((WIN_W, WIN_H))
pygame.display.set_caption('SPACE')

clock = pygame.time.Clock()

bg = pygame.image.load(os.path.join('images', 'bg.jpg'))

moon = pygame.image.load(os.path.join('images',
                         'moon.png')).convert_alpha()
moon = pygame.transform.scale(moon, (400, 400))
moon_mask = pygame.mask.from_surface(moon)
new_moon = moon
moon_pos = [1300, 100]
moon_size = 400

ship = pygame.image.load(os.path.join('images',
                        'spaceship.png'))
ship = pygame.transform.scale(ship, (500, 300))
new_ship = ship
ship_pos = [-500, 750]
turn = 30

laser = pygame.image.load(os.path.join('images',
                          'laser_one.png')).convert_alpha()
laser = pygame.transform.scale(laser, (49, 10))
new_laser = laser
laser_mask = pygame.mask.from_surface(new_laser)
laser_pos = [650, 600]
LASER_TURN = 25

offset1 = (int(moon_pos[0] - laser_pos[0]), int(moon_pos[1] - laser_pos[1]))
offset2 = (int(moon_pos[0] - ship_pos[0]), int(moon_pos[1] - ship_pos[1]))

step = 0

play = True
while play:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            play = False

    if ship_pos[0] > 1920:
        step = 0
        moon_pos = [1300, 100]
        new_moon = pygame.transform.scale(moon, (400, 400))
        moon_size = 400
        ship_pos = [-500, 750]
        turn = 30
        new_laser = laser
        laser_pos = [650, 600]
        offset1 = (int(moon_pos[0] - laser_pos[0]),
                   int(moon_pos[1] - laser_pos[1]))
        offset2 = (int(moon_pos[0] - ship_pos[0]),
                   int(moon_pos[1] - ship_pos[1]))
        pygame.time.delay(2000)

    now.blit(bg, (0,0))
    if step == 1:
        now.blit(new_laser, laser_pos)
    now.blit(new_ship, ship_pos)
    now.blit(new_moon, moon_pos)

    #ship move
    new_ship = pygame.transform.rotate(ship, turn)

    ship_pos[0] += 5
    ship_pos[1] -= 2

    if step > 1:
        ship_pos[0] += 3
        ship_pos[1] -= 1
    if step == 4:
        moon_pos[0] += 8
        moon_pos[1] -= 3

    if step == 0 and ship_pos[0] > 202:
        step = 1

    if turn > 0:
        turn -= 0.08

    if (step == 1 and 
        laser_mask.overlap_area(moon_mask, offset1) > 0):
        step = 2

    if step == 1:
        #laser move
        new_laser = pygame.transform.rotate(laser, LASER_TURN)
        laser_pos[0] += 12
        laser_pos[1] -= 3
        offset1 = (int(moon_pos[0] - laser_pos[0]), int(moon_pos[1] - laser_pos[1]))

    if step == 2:
        #moon move
        moon_size -= SHIFT
        moon_pos[0] += SHIFT // 2
        moon_pos[1] += SHIFT // 2

        if moon_size < 30:
            step = 3
        else:
            new_moon = pygame.transform.scale(moon, (moon_size, moon_size))

    if (step == 3 and
        int(moon_pos[0] - ship_pos[0]) <= 465):
        step = 4

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
