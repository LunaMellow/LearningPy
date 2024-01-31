"""

    > Particles
    -------------------
    @brief  :  Particles made from Pyglet shapes
    @author :  Luna Sofie Bergh

"""

# File Imports
from NewShape import NewShape

# Library Imports
from random import randint
from pyglet.graphics import Batch


class Circles:
    color1 = (255, 255, 255)

    def __init__(self):
        self.particle_batch = Batch()

        self.circle_x = randint(100, 1180)
        self.circle_y = randint(100, 620)

        self.circle = NewShape(
            shape_type='circle',
            x=self.circle_x,
            y=self.circle_y,
            radius=randint(5, 15),
            color=(randint(0, 255), randint(0, 255), randint(0, 255)),
            batch=self.particle_batch)

    def update(self, dt, window_width, window_height):
        self.circle.update(dt, window_width, window_height)


class Lines:
    color1 = (255, 255, 255)

    def __init__(self, window_height, start_outside=True):
        self.particle_batch = Batch()

        self.line_x = randint(100, 1180)
        self.line_y = randint(0, window_height)

        self.line_x = randint(100, 1180)
        self.line_y = randint(100, 620)

        self.line = NewShape(
            shape_type='line',
            x=self.line_x,
            y=self.line_y,
            x2=randint(self.line_x + 0, self.line_x + 50),
            y2=randint(self.line_y + 0, self.line_y + 50),
            width=4,
            color=(randint(0, 255), randint(0, 255), randint(0, 255)),
            batch=self.particle_batch
        )

    def update(self, dt, window_width, window_height):
        self.line.update(dt, window_width, window_height)