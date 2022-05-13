import os
os.system('pip install -r requirements.txt')

import pymunk
from pygame.locals import *
import pygame
import pymunk.pygame_util

from setting import *

SCREEN_WD = 800
SCREEN_HT = 800
TARGET_FPS = 60

space = make_space() 
screen = pygame.display.set_mode((SCREEN_WD, SCREEN_HT), 0, 32)
clock = pygame.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(screen)
space.debug_draw(draw_options)

floor = 17
for i in range(floor):
    if i<3:
        width = 45
    else:
        width = 30
    y =  785 - (i * 30) -10
    body, poly = make_box(y, width)
    add_box(space, body, poly)

body.apply_impulse_at_world_point((0, 20*10**7), (100, 495))

timeStep = 1.0 / 120
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            continue
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
            continue
 
    screen.fill((255, 255, 255))
 
    space.debug_draw(draw_options)
 
    space.step(timeStep)
 
    pygame.display.flip()
    clock.tick(TARGET_FPS)
 
pygame.quit()