# Library Imports
from pyglet import *
from pyglet.app import *
from pyglet.window import *
from pyglet.graphics import *


class MainWindow(Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Batch
        self.batch = Batch()

        # Window size
        self.width, self.height = self.get_size()

        # Top 4 circles
        self.red_ball =     shapes.Circle(x=20, y=self.height - 30,  radius=20, segments=50, color=(255, 0, 0),   batch=self.batch)
        self.yellow_ball =  shapes.Circle(x=20, y=self.height - 80,  radius=20, segments=50, color=(255, 255, 0), batch=self.batch)
        self.green_ball =   shapes.Circle(x=20, y=self.height - 130, radius=20, segments=50, color=(0, 255, 0),   batch=self.batch)
        self.blue_ball =    shapes.Circle(x=20, y=self.height - 180, radius=20, segments=50, color=(0, 0, 255),   batch=self.batch)

        # Bottom 3 circles
        self.size_ball =    shapes.Circle(x=50,  y=self.height - 300, radius=50, segments=100, color=(255, 0, 0), batch=self.batch)
        self.color_ball =   shapes.Circle(x=150, y=self.height - 300, radius=50, segments=100, color=(255, 0, 0), batch=self.batch)
        self.smooth_ball =  shapes.Circle(x=250, y=self.height - 300, radius=50, segments=100, color=(0, 255, 0), batch=self.batch)

    def on_draw(self):

        # Clear and draw fps
        window.clear()
        fps_display.draw()

        # Draw all shapes
        self.batch.draw()


if __name__ == '__main__':

    # Window properties
    window = MainWindow(caption="BPROG - Luna Sofie Bergh", width=500, height=500, resizable=False)
    window.set_mouse_visible(visible=True)
    fps_display = FPSDisplay(window)

    # Run the application
    run()
