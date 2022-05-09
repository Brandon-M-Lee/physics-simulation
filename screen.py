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
 
screen = pygame.display.set_mode((SCREEN_WD, SCREEN_HT), 0, 32)
clock = pygame.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(screen)

space = make_space()

floor = 10

for i in range(floor-1):
    print(i)
    body, poly = make_box()
    add_box(space, body, poly)

body, poly = make_box((floor-1)*3)
body.apply_force_at_local_point((0, 5), (0, 300))

timeStep = 1.0 / 60
 
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