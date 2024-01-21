"""

    Assignment Week 02
    -------------------
    Question 7b

    @brief   :  Pyglet shapes and batching
    @author  :  Luna Sofie Bergh
    @date    :  21-01-2024

    Menu Description

    A : Show different shapes
    O : Spawn 10000 circles
    C : Clear window

"""

# Math imports
from random import *

# Pyglet imports
from pyglet.app import *
from pyglet.window import *
from pyglet.graphics import *
from pyglet.shapes import *


# Initialize window-instance
class MainWindow(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.size = list(self.get_size())

        self.wx, self.wy = self.size[0], self.size[1]

        # Shape lists/arrays
        self.shapes_all = []
        self.shapes_circle = []

        # Batch Rendering
        self.batch = Batch()  # Shapes batch

        print("Started correctly")

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

    def on_key_press(self, symbol, modifiers):

        if symbol == key.A:
            new_circle = window.NewShape(shape_type='circle',
                                         x=100,
                                         y=100,
                                         batch=window.batch,
                                         radius=30,
                                         color=(255, 0, 0))
            window.shapes_all.append(new_circle.shape_instance)

            new_star = window.NewShape(shape_type='star',
                                       x=200,
                                       y=200,
                                       batch=window.batch,
                                       outer_radius=40,
                                       inner_radius=3,
                                       num_spikes=5,
                                       color=(0, 0, 255))
            window.shapes_all.append(new_star.shape_instance)

            new_rectangle = window.NewShape(shape_type='rectangle',
                                            x=300,
                                            y=300,
                                            batch=window.batch,
                                            width=50,
                                            height=100,
                                            color=(0, 255, 0))
            window.shapes_all.append(new_rectangle.shape_instance)

            new_line = window.NewShape(shape_type='line',
                                       x=400,
                                       y=400,
                                       batch=window.batch,
                                       x2=450,
                                       y2=450,
                                       color=(255, 255, 0))
            window.shapes_all.append(new_line.shape_instance)

            new_arc = window.NewShape(shape_type='arc',
                                      x=500,
                                      y=500,
                                      radius=30,
                                      color=(255, 0, 255),
                                      start_angle=0,
                                      batch=window.batch)
            window.shapes_all.append(new_arc)

            new_ellipse = window.NewShape(shape_type='ellipse',
                                          x=600,
                                          y=600,
                                          batch=window.batch,
                                          a=2,
                                          b=1,
                                          color=(128, 128, 128))
            window.shapes_all.append(new_ellipse)

        if symbol == key.O:
            while len(window.shapes_circle) < 10000:
                new_circle = window.NewShape('circle', randint(0, self.wx),
                                             randint(0, self.wy),
                                             radius=randint(1, 10),
                                             batch=window.batch,
                                             color=(randint(0, 255),
                                                    randint(0, 255),
                                                    randint(0, 255)))
                window.shapes_circle.append(new_circle.shape_instance)

        if symbol == key.C:
            window.shapes_all = []
            window.shapes_circle = []
            window.batch = Batch()

    def on_draw(self):

        # Window clear
        window.clear()

        # Batch draw
        window.batch.draw()


if __name__ == '__main__':
    # Window properties
    window = MainWindow(caption="BPROG - Luna Sofie Bergh", width=1280, height=720, resizable=True)
    window.set_minimum_size(width=400, height=300)
    window.set_mouse_visible(visible=True)
    run()
