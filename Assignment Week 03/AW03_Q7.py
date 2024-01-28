"""

    Assignment Week 03
    -------------------
    Question 7

    @brief   :  Pyglet shape behaviour
    @author  :  Luna Sofie Bergh
    @date    :  28-01-2024

    Menu Description
    -------------------
    SPACE BAR : Switch between the questions

"""

# Math imports
from random import *

# Pyglet imports
from pyglet.app import *
from pyglet.window import *
from pyglet.graphics import *
from pyglet.shapes import *


class MainWindow(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window size
        self.size = list(self.get_size())
        self.wx, self.wy = self.size[0], self.size[1]

        # Shape lists/arrays
        self.shapes_all = []
        self.shapes_circle = []

        # Batch rendering
        self.batch = Batch()

        print("Started correctly")

    """
    
        > window.NewShape
        -------------------
        @brief  :  Draws new shapes using pyglet graphics
        
    """
    class NewShape:
        def __init__(self, shape_type, x, y, batch, **kwargs):

            if shape_type == 'circle':
                self.shape_instance = Circle(x=x, y=y, batch=batch, **kwargs)
            elif shape_type == 'star':
                self.shape_instance = Star(x=x, y=y, batch=batch, **kwargs)
            elif shape_type == 'rectangle':
                self.shape_instance = Rectangle(x=x, y=y, batch=batch, **kwargs)
            elif shape_type == 'line':
                self.shape_instance = Line(x=x, y=y, batch=batch, **kwargs)
            elif shape_type == 'arc':
                self.shape_instance = Arc(x=x, y=y, batch=batch, **kwargs)
            elif shape_type == 'ellipse':
                self.shape_instance = Ellipse(x=x, y=y, batch=batch, **kwargs)
            else:
                raise ValueError("Invalid shape type")

    def on_draw(self):

        # Window clear
        window.clear()

        # Batch draw
        window.batch.draw()


"""

    > __main__
    -------------------
    @brief  :  Initializes and sets properties for MainWindow
    
"""
if __name__ == '__main__':

    # Window properties
    window = MainWindow(caption="BPROG - Luna Sofie Bergh", width=1280, height=720, resizable=True)
    window.set_minimum_size(width=400, height=300)
    window.set_mouse_visible(visible=True)
    run()
