# File Imports
from MushroomCow import MushroomCow

# Library Imports
from random import randint
from pyglet import *
from pyglet.app import *
from pyglet.window import *
from pyglet.graphics import *
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

    def update(self, dt, window_width, window_height):
        speed = 50  # Adjust the speed as needed
        self.x += self.direction[0] * speed * dt
        self.y += self.direction[1] * speed * dt

        # Wrap around horizontally
        self.x %= window_width

        # Wrap around vertically
        self.y %= window_height

        x, y = self.x, self.y
        self.shape_instance.x = x
        self.shape_instance.y = y


class Circles:
    color1 = (255, 255, 255)

    def __init__(self):
        self.particle_batch = Batch()

        self.circle_x = randint(100, 1180)
        self.circle_y = randint(100, 620)

        self.circle = NewShape(
            shape_type='circle',
            x=self.circle_x,
            y=self.circle_y,
            radius=randint(5, 15),
            color=(randint(0, 255), randint(0, 255), randint(0, 255)),
            batch=self.particle_batch)

    def update(self, dt, window_width, window_height):
        self.circle.update(dt, window_width, window_height)


class Lines:
    color1 = (255, 255, 255)

    def __init__(self, window_height, start_outside=True):
        self.particle_batch = Batch()

        self.line_x = randint(100, 1180)
        self.line_y = randint(0, window_height)

        self.line_x = randint(100, 1180)
        self.line_y = randint(100, 620)

        self.line = NewShape(
            shape_type='line',
            x=self.line_x,
            y=self.line_y,
            x2=randint(self.line_x + 0, self.line_x + 50),
            y2=randint(self.line_y + 0, self.line_y + 50),
            width=4,
            color=(randint(0, 255), randint(0, 255), randint(0, 255)),
            batch=self.particle_batch
        )

    def update(self, dt, window_width, window_height):
        self.line.update(dt, window_width, window_height)


class MainWindow(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window size
        self.size = list(self.get_size())
        self.wx, self.wy = self.size[0], self.size[1]

        # Store all the instances
        self.particles = []
        self.mushroom_cows = []

        for i in range(50):
            new_circle = Circles()
            self.particles.append(new_circle)

        for i in range(50):
            new_line = Lines(window_height=self.wy, start_outside=True)
            self.particles.append(new_line)

    def update(self, dt):
        for particle in self.particles:
            particle.update(dt, self.wx, self.wy)

    # Keyboard press event
    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            new_cow = MushroomCow(init_pos=(randint(100, 1180), randint(100, 620)))
            self.mushroom_cows.append(new_cow)

    def on_draw(self):

        # Window clear
        window.clear()

        # Draw background
        background_batch.draw()

        # Draw particles
        for particle in self.particles:
            particle.update(1 / 60, self.wx, self.wy)  # Call the update method for each particle
            particle.particle_batch.draw()

        # Draws and updates the cows
        for cow in self.mushroom_cows:
            cow.Cow_Batch.draw()

        # Draw fps for performance insights
        fps_display.draw()


if __name__ == '__main__':
    # Window properties
    window = MainWindow(caption="BPROG - Luna Sofie Bergh", width=1280, height=720, resizable=False)
    window.set_mouse_visible(visible=True)

    # Background
    background_batch = Batch()
    background = NewShape(
        shape_type='rectangle',
        x=0,
        y=0,
        width=3820,
        height=2560,
        color=(20, 20, 20),
        batch=background_batch
    )

    pyglet.clock.schedule(window.update)  # Add this line

    # Fps Display
    fps_display = FPSDisplay(window)

    # Run the application
    run()
