# Library Imports
from random import *
from pyglet import *
from pyglet.app import *
from pyglet.window import *
from pyglet.graphics import *


class MainWindow(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Keyboard press event
    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            app.exit()

    def on_draw(self):

        # Window clear
        window.clear()

        # Draw fps for performance insights
        fps_display.draw()


if __name__ == '__main__':

    # Window properties
    window = MainWindow(caption="BPROG - Luna Sofie Bergh", width=1280, height=720, resizable=True)

    # Fps Display
    fps_display = FPSDisplay(window)

    # Run the application
    run()
