"""

    > NewShape
    -------------------
    @brief  :  Creates pyglet shapes
    @author :  Luna Sofie Bergh

"""

# Library Imports
from pyglet.shapes import *
from random import uniform

class NewShape:
    SHAPE_MAP = {
        'circle': Circle,
        'star': Star,
        'rectangle': Rectangle,
        'line': Line,
        'arc': Arc,
        'ellipse': Ellipse,
    }

    def __init__(self, shape_type, x, y, batch, **kwargs):
        if shape_type not in self.SHAPE_MAP:
            raise ValueError("Invalid shape type")

        shape_class = self.SHAPE_MAP[shape_type]
        self.x = x
        self.y = y
        self.direction = (uniform(-1, 1), uniform(-1, 1))  # Random direction
        self.shape_instance = shape_class(x=self.x, y=self.y, batch=batch, **kwargs)

    def update(self, dt):
        speed = 50  # Adjust the speed as needed
        self.x += self.direction[0] * speed * dt
        self.y += self.direction[1] * speed * dt

        x, y = self.x, self.y
        self.shape_instance.x = x
        self.shape_instance.y = y