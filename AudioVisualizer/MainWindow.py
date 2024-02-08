from pyglet import *
from pyglet.window import *
from pyglet.graphics import *
from random import *

class MainWindow(Window):
    CIRCLE_RADIUS = 10
    NUM_CIRCLES = 100
    MAX_VELOCITY = 100

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window size
        self.size = list(self.get_size())
        self.wx, self.wy = self.size[0], self.size[1]

        self.batch = Batch()

        self.circles = [pyglet.shapes.Circle(
            x=randint(50, self.wx - 50),
            y=randint(50, self.wy - 50),
            radius=self.CIRCLE_RADIUS,
            color=(randint(125, 175), randint(25, 75), randint(100, 255)),
            batch=self.batch,

        )
            for _ in range(self.NUM_CIRCLES)
        ]

    def on_draw(self):
        # Window clear
        window.clear()

        # Draw fps for performance insights
        fps_display.draw()

        self.batch.draw()

    # Function to update circle positions
    def update(self, dt):
        try:
            for circle in self.circles:
                # Calculate random velocity
                velocity_x = uniform(-self.MAX_VELOCITY, self.MAX_VELOCITY)
                velocity_y = uniform(-self.MAX_VELOCITY, self.MAX_VELOCITY)
                # Update circle position
                circle.x += velocity_x * dt
                circle.y += velocity_y * dt
                # Wrap around the window edges
                if circle.x < 0:
                    circle.x = self.wx
                elif circle.x > self.wx:
                    circle.x = 0
                if circle.y < 0:
                    circle.y = self.wy
                elif circle.y > self.wy:
                    circle.y = 0
        except Exception as e:
            print("Error:", e)


if __name__ == '__main__':
    # Window properties
    window = MainWindow(caption="Moving Circles", width=800, height=600, resizable=False)

    # Fps Display
    fps_display = FPSDisplay(window)

    # Run the application
    pyglet.clock.schedule_interval(window.update, 1 / 60)
    pyglet.app.run()
