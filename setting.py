import pymunk

def make_space():
    space = pymunk.Space()
    space.gravity = 98, 0

    ground = pymunk.Body(body_type=pymunk.Body.STATIC)
    ground.position = 0, 0
    
    ground_shape = pymunk.Segment(ground, (-50, 0), (50, 0), 1)
    space.add(ground, ground_shape)

    return space
 
def make_box(y):
    body = pymunk.Body(5, 50)
    body.position == (-45, y)
    poly = pymunk.Poly.create_box(body, (3, 3))
    poly.friction = 0.5
    return body, poly

def add_box(space, body, poly):
    space.add(body, poly)