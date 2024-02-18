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
from pyglet.shapes import *


class MainWindow(Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Batch
        self.batch = Batch()

        # Window size
        self.width, self.height = self.get_size()

        # Interpolation parameters
        self.red_position_t = 0
        self.yellow_position_t = 0
        self.green_position_t = 0
        self.blue_position_t = 0
        self.size_t = 0
        self.color_t = 0
        self.smooth_t = 0
        self.magenta_t = 0

        # Top 4 balls
        self.ball_red =    Circle(x=20, y=self.height - 30,  radius=20, segments=50, color=(255, 0, 0),   batch=self.batch)
        self.ball_yellow = Circle(x=20, y=self.height - 80,  radius=20, segments=50, color=(255, 255, 0), batch=self.batch)
        self.ball_green =  Circle(x=20, y=self.height - 130, radius=20, segments=50, color=(0, 255, 0),   batch=self.batch)
        self.ball_blue =   Circle(x=20, y=self.height - 180, radius=20, segments=50, color=(0, 0, 255),   batch=self.batch)

        # Bottom 3 balls
        self.ball_size =   Circle(x=50,  y=self.height - 300, radius=50, segments=100, color=(255, 0, 0), batch=self.batch)
        self.ball_color =  Circle(x=150, y=self.height - 300, radius=50, segments=100, color=(255, 0, 0), batch=self.batch)
        self.ball_smooth = Circle(x=250, y=self.height - 300, radius=50, segments=100, color=(0, 255, 0), batch=self.batch)

        # Magenta balls
        self.magenta_balls = [Circle(x=500, y=100, radius=10, color=(255, 0, 255), batch=self.batch) for _ in range(10)]
        self.magenta_control_points = [(500, self.height - 100), (250, self.height - 500), (20, self.height - 350)]

    def update_red_position(self, dt):
        self.red_position_t += dt
        t = self.red_position_t % 4
        self.ball_red.x = 20 + t * (230 - 20) / 5
        if t >= 5:
            self.red_position_t = 0

    def update_yellow_position(self, dt):
        self.yellow_position_t += dt
        t = self.yellow_position_t % 4
        if t <= 2:
            self.ball_yellow.x = 20 + t * (230 - 20) / 2
        else:
            t = 4 - t
            self.ball_yellow.x = 20 + t * (230 - 20) / 2

    def update_green_position(self, dt):
        self.green_position_t += dt
        t = (self.green_position_t % 4) / 2
        if t <= 1:
            # Check log for details of the formulas
            smoothstep = t * t * (3 - 2 * t)
            self.ball_green.x = 20 + smoothstep * (230 - 20)
        else:
            t = 2 - t
            # Check log for details of the formulas
            smoothstep = t * t * (3 - 2 * t)
            self.ball_green.x = 20 + smoothstep * (230 - 20)

    def update_blue_position(self, dt):
        self.blue_position_t += dt
        t = self.blue_position_t % 10
        if t <= 5:
            cubic = t ** 3
            self.ball_blue.x = 20 + cubic * (230 - 20) / (5 ** 3)
        else:
            t -= 5
            cubic = t ** 3
            self.ball_blue.x = 230 - cubic * (230 - 20) / (5 ** 3)

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
            # Check log for details of the formulas
            smoothstep = t * t * (3 - 2 * t)
            red = int((1 - smoothstep) * 255)
            green = int(smoothstep * 255)
        else:
            t = 2 - t
            # Check log for details of the formulas
            smoothstep = t * t * (3 - 2 * t)
            red = int((1 - smoothstep) * 255)
            green = int(smoothstep * 255)

        self.ball_color.color = (red, green, 0)

    def update_smoothstep(self, dt):
        self.smooth_t += dt
        t = self.smooth_t % 4

        if t <= 2:
            radius = 50 - t / 2 * 25
            yellow = int(t / 2 * 255)
        else:
            radius = 25 + (t - 2) / 2 * 25
            yellow = int((4 - t) / 2 * 255)

        self.ball_smooth.radius = radius
        self.ball_smooth.color = (yellow, 255, 0)

    # The bezier curve magenta balls were helped by chatgpt,
    # please look at the log for more information.
    def update_magenta(self, dt):
        # Define total traversal time and number of intervals
        total_time = 2

        num_intervals = 10
        self.magenta_t += dt * 0.5 / total_time

        # Update each magenta ball's position along the curve
        for i, ball in enumerate(self.magenta_balls):
            t = (self.magenta_t + i * 0.2) % 1
            magenta_curve_point = self.quadratic_bezier(self.magenta_control_points, t)
            ball.position = magenta_curve_point

    # Check log for details of the formula
    def quadratic_bezier(self, control_points, t):
        p0, p1, p2 = control_points
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        return x, y

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
    schedule_interval(window.update_red_position, 1 / 60)
    schedule_interval(window.update_yellow_position, 1 / 60)
    schedule_interval(window.update_green_position, 1 / 60)
    schedule_interval(window.update_blue_position, 1 / 60)
    schedule_interval(window.update_magenta, 1 / 60)

    # Run the application
    run()
