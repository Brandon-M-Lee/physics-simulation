import pymunk
import pygame

def make_space():
    space = pymunk.Space()
    space.gravity = 0, 98

    ground = pymunk.Body(body_type=pymunk.Body.STATIC)
    ground.color = (255, 0, 0)
    ground.position = 0, 0
    ground_shape = pymunk.Segment(ground, (0, 800), (800, 800), 10)
    ground_shape.friction = 0.5
    space.add(ground, ground_shape)

    return space
 
def make_box(y, width):
    body = pymunk.Body(4.705*10**7, 1254*10**6)
    body.position = (100, y)
    poly = pymunk.Poly.create_box(body, (width, 30))
    poly.friction = 0.7
    return body, poly

def add_box(space, body, poly):
    space.add(body, poly)