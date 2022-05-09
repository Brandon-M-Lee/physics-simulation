import pymunk
import pygame

def make_space():
    space = pymunk.Space()
    space.gravity = 0, 9.8

    ground = pymunk.Body(body_type=pymunk.Body.STATIC)
    ground.color = (255, 0, 0)
    ground.position = 0, 0
    
    ground_shape = pymunk.Segment(ground, (0, 800), (800, 800), 10)
    space.add(ground, ground_shape)

    return space
 
def make_box(y=400):
    body = pymunk.Body(5, 50)
    body.position == (400, y)
    poly = pymunk.Poly.create_box(body, (30, 30))
    poly.friction = 0
    return body, poly

def add_box(space, body, poly):
    space.add(body, poly)