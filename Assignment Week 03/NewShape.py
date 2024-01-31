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

        self.collided = False  # Add this line to track collision status

    def update(self, dt):
        speed = 50  # Adjust the speed as needed
        self.x += self.direction[0] * speed * dt
        self.y += self.direction[1] * speed * dt

        x, y = self.x, self.y
        self.shape_instance.x = x
        self.shape_instance.y = y

    def check_collision(self, other_shape):
        # Add collision logic based on shape types
        if isinstance(other_shape, NewShape):
            distance = ((self.x - other_shape.x) ** 2 + (self.y - other_shape.y) ** 2) ** 0.5
            combined_radii = self.shape_instance.radius + other_shape.shape_instance.radius
            return distance <= combined_radii

    def handle_collision(self, other_shape):
        if not self.collided and not other_shape.collided:
            self.shape_instance.color = (255, 0, 0)
            other_shape.shape_instance.color = (255, 0, 0)
            print(f"Collision detected between {self.shape_instance.__class__.__name__}"
                  f" at ({self.x}, {self.y}) and {other_shape.shape_instance.__class__.__name__}"
                  f" at ({other_shape.x}, {other_shape.y})")

            self.collided = True
            other_shape.collided = True