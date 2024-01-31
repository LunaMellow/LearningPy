"""

    > NewShape
    -------------------
    @brief  :  Creates pyglet shapes
    @author :  Luna Sofie Bergh

"""

# Library Imports
from pyglet.shapes import *


class NewShape:

    # Shape Dictionary Map
    SHAPE_MAP = {
        'circle': Circle,
        'star': Star,
        'rectangle': Rectangle,
        'line': Line,
        'arc': Arc,
        'ellipse': Ellipse,
    }

    def __init__(self, shape_type, x, y, batch, **kwargs):
        # Check if given shape is in our shape dictionary
        if shape_type not in self.SHAPE_MAP:
            raise ValueError("Invalid shape type")

        # Creates shape instance based on shape_type provided
        shape_class = self.SHAPE_MAP[shape_type]
        self.x = x
        self.y = y
        self.shape_instance = shape_class(x=self.x, y=self.y, batch=batch, **kwargs)

