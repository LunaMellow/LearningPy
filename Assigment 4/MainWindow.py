"""

    Assigment 4
    -------------------
    Question 5

    @brief   :  Pyglet interpolation
    @author  :  Luna Sofie Bergh
    @date    :  16-02-2024

"""

# Library Imports
import math
from pyglet import *
from pyglet.app import *
from pyglet.window import *
from pyglet.graphics import *
from pyglet.clock import *


class MainWindow(Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Batch
        self.batch = Batch()

        # Window size
        self.width, self.height = self.get_size()

        # Interpolation parameters
        self.size_t = 0
        self.color_t = 0
        self.smooth_t = 0

        # Top 4 balls
        self.ball_red =     shapes.Circle(x=20, y=self.height - 30,  radius=20, segments=50, color=(255, 0, 0),   batch=self.batch)
        self.ball_yellow =  shapes.Circle(x=20, y=self.height - 80,  radius=20, segments=50, color=(255, 255, 0), batch=self.batch)
        self.ball_green =   shapes.Circle(x=20, y=self.height - 130, radius=20, segments=50, color=(0, 255, 0),   batch=self.batch)
        self.ball_blue =    shapes.Circle(x=20, y=self.height - 180, radius=20, segments=50, color=(0, 0, 255),   batch=self.batch)

        # Bottom 3 balls
        self.ball_size =    shapes.Circle(x=50,  y=self.height - 300, radius=50, segments=100, color=(255, 0, 0), batch=self.batch)
        self.ball_color =   shapes.Circle(x=150, y=self.height - 300, radius=50, segments=100, color=(255, 0, 0), batch=self.batch)
        self.ball_smooth =  shapes.Circle(x=250, y=self.height - 300, radius=50, segments=100, color=(0, 255, 0), batch=self.batch)

    def update_size(self, dt):
        self.size_t += dt * 0.25
        t = (self.size_t % 2) / 1
        if t <= 1:
            self.ball_size.radius = t * t * (3 - 2 * t) * 50
        else:
            t = 2 - t
            self.ball_size.radius = (t * t * (3 - 2 * t)) * 50

    def update_color(self, dt):
        self.color_t += dt * 0.25
        t = (self.color_t % 2) / 1

        if t <= 1:
            smoothstep = t * t * (3 - 2 * t)
            red = int((1 - smoothstep) * 255)
            green = int(smoothstep * 255)
        else:
            t = 2 - t
            smoothstep = t * t * (3 - 2 * t)
            red = int((1 - smoothstep) * 255)
            green = int(smoothstep * 255)

        self.ball_color.color = (red, green, 0)

    def update_smoothstep(self, dt):
        self.smooth_t += dt * 0.25
        t = (self.smooth_t % 2) / 1
        if t <= 1:
            self.ball_smooth.radius = t * t * (3 - 2 * t) * 50
            smoothstep = t * t * (3 - 2 * t)
            red = int((1 - smoothstep) * 255)
            green = int(smoothstep * 255)
        else:
            t = 2 - t
            self.ball_smooth.radius = (t * t * (3 - 2 * t)) * 50
            smoothstep = t * t * (3 - 2 * t)
            red = int((1 - smoothstep) * 255)
            green = int(smoothstep * 255)
        self.ball_smooth.color = (red, green, 0)


    def on_draw(self):

        # Clear and draw fps
        window.clear()
        fps_display.draw()

        # Draw all balls
        self.batch.draw()


if __name__ == '__main__':

    # Window properties
    window = MainWindow(caption="BPROG - Luna Sofie Bergh", width=500, height=500, resizable=False)
    window.set_mouse_visible(visible=True)
    fps_display = FPSDisplay(window)

    # Update functions
    schedule_interval(window.update_size, 1 / 60)
    schedule_interval(window.update_color, 1 / 60)
    schedule_interval(window.update_smoothstep, 1 / 60)

    # Run the application
    run()
