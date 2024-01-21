#############################################
#                                           #
#   BMA1020 - Mathematics for Programming   #
#                                           #
#   @author - LunaMellow                    #
#                                           #
#############################################

# SHAPES
######################################################################################################
# circle = Circle(300, 300, 50, color=(255, 255, 255), batch=batch)  # Red circle
# triangle = Triangle(500, 300, 400, 400, 300, 400, color=(0, 255, 0), batch=batch)  # Green triangle
# square = Rectangle(100, 100, 200, 200, color=(0, 0, 255), batch=batch)  # Blue square
# rectangle = Rectangle(300, 100, 200, 100, color=(255, 255, 0), batch=batch)  # Yellow rectangle
# line = Line(100, 500, 200, 500, width=5, color=(255, 0, 255), batch=batch)  # Magenta line
# star = Star(500, 500, 60, 40, num_spikes=5, color=(0, 255, 255), batch=batch)  # Cyan star
# arc = Arc(700, 300, 100, color=(255, 165, 0), batch=batch)  # Orange arc
# ellipse = Ellipse(900, 300, 50, 100, color=(128, 0, 128), batch=batch)  # Purple ellipse
# sector = Sector(700, 500, 100, color=(139, 69, 19), batch=batch)  # Brown sector


# Math imports
from math import *
from random import *
from sympy import *

# Pyglet imports
from pyglet.app import *
from pyglet.window import *
from pyglet.graphics import *
from pyglet.clock import *
from pyglet.shapes import *


# Create window
class MainWindow(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.batch = Batch()
        self.circle = Circle(x=640, y=360, radius=50, color=(50, 225, 30), batch=self.batch)

        self.directions = {'left': False, 'right': False, 'up': False, 'down': False}
        self.speed = 5

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        if symbol == key.LEFT:
            self.directions['left'] = True
        if symbol == key.RIGHT:
            self.directions['right'] = True
        if symbol == key.UP:
            self.directions['up'] = True
        if symbol == key.DOWN:
            self.directions['down'] = True

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        if symbol == key.LEFT:
            self.directions['left'] = False
        if symbol == key.RIGHT:
            self.directions['right'] = False
        if symbol == key.UP:
            self.directions['up'] = False
        if symbol == key.DOWN:
            self.directions['down'] = False

    def on_draw(self) -> None:
        self.clear()
        self.batch.draw()

    def update(self, dt: float) -> None:
        if self.directions['left']:
            self.circle.x -= self.speed
        if self.directions['right']:
            self.circle.x += self.speed
        if self.directions['up']:
            self.circle.y += self.speed
        if self.directions['down']:
            self.circle.y -= self.speed


if __name__ == '__main__':
    window = MainWindow(caption="BPROG - Luna Sofie Bergh", width=1280, height=720, resizable=True)
    window.set_minimum_size(width=400, height=300)
    window.set_mouse_visible(visible=True)
    schedule_interval(window.update, 1 / 60)
    run()
