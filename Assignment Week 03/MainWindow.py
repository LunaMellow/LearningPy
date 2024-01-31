"""

    Assignment Week 03
    -------------------
    Question 7

    @brief   :  Pyglet shape behaviour
    @author  :  Luna Sofie Bergh
    @date    :  29-01-2024

    Menu Description
    -------------------
    SPACE BAR : Switch between the questions

    PS
    -------------------
    I spent an ungodly amount of time on this
    cow and structure. Hope you guys appreciate
    my effort and dedication to making something
    really cool!

"""

# File Imports
from NewShape import NewShape
from MushroomCow import MushroomCow

# Library Imports
from random import randint
from pyglet import *
from pyglet.app import *
from pyglet.window import *
from pyglet.graphics import *


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
            radius=randint(5, 25),
            color=self.color1,
            batch=self.particle_batch)

    def update(self, dt):
        self.circle.update(dt)

    def check_collision(self, other_shape):
        # Implement collision logic for circles
        if isinstance(other_shape, Circles):
            distance = ((self.circle_x - other_shape.circle_x) ** 2 + (
                    self.circle_y - other_shape.circle_y) ** 2) ** 0.5
            combined_radii = self.circle.shape_instance.radius + other_shape.circle.shape_instance.radius
            result = distance <= combined_radii
            if result:
                print(f"Collision detected between Circles at ({self.circle_x}, {self.circle_y}) "
                      f"and ({other_shape.circle_x}, {other_shape.circle_y})")
            return result
        return False

    def handle_collision(self, other_shape):
        # Handle collision logic for circles
        self.circle.shape_instance.color = (255, 0, 0)
        other_shape.circle.shape_instance.color = (255, 0, 0)
        print(
            f"Collision detected between Circles at ({self.circle_x}, {self.circle_y}) and ({other_shape.circle_x}, {other_shape.circle_y})")


class Lines:
    color1 = (255, 255, 255)

    def __init__(self):
        self.particle_batch = Batch()

        self.line_x = randint(100, 1180)
        self.line_y = randint(100, 620)

        self.line = NewShape(
            shape_type='line',
            x=self.line_x,
            y=self.line_y,
            x2=randint(self.line_x + 50, self.line_x + 150),
            y2=randint(self.line_y + 50, self.line_y + 150),
            width=4,
            color=self.color1,
            batch=self.particle_batch
        )

    def update(self, dt):
        self.line.update(dt)

    def check_collision(self, other_shape):
        # Implement collision logic for lines
        if isinstance(other_shape, Lines):
            # Example: Check if the bounding boxes overlap
            result = (
                    self.line_x < other_shape.line_x + other_shape.line.shape_instance.x2 and
                    self.line_x + self.line.shape_instance.x2 > other_shape.line_x and
                    self.line_y < other_shape.line_y + other_shape.line.shape_instance.y2 and
                    self.line_y + self.line.shape_instance.y2 > other_shape.line_y
            )
            if result:
                print(f"Collision detected between Line at ({self.line_x}, {self.line_y}) "
                      f"and Line at ({other_shape.line_x}, {other_shape.line_y})")
            return result
        return False

    def handle_collision(self, other_shape):
        # Handle collision logic for lines
        self.line.shape_instance.color = (255, 0, 0)
        other_shape.line.shape_instance.color = (255, 0, 0)
        print(f"Collision detected between Line at ({self.line_x}, {self.line_y}) and Line at ({other_shape.line_x}, {other_shape.line_y})")


class MainWindow(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window size
        self.size = list(self.get_size())
        self.wx, self.wy = self.size[0], self.size[1]

        # Store all the instances
        self.particles = []
        self.mushroom_cows = []

        for i in range(10):
            new_circle = Circles()
            self.particles.append(new_circle)

        for i in range(10):
            new_line = Lines()
            self.particles.append(new_line)

    def update(self, dt):
        print("Updating particles...")
        self.update_all_particles(dt)

    def update_all_particles(self, dt):
        for i, particle1 in enumerate(self.particles):
            for j, particle2 in enumerate(self.particles):
                if i != j and particle1.check_collision(particle2):
                    print(f"Potential collision detected between particles {i} and {j}")
                    particle1.handle_collision(particle2)
                    particle2.handle_collision(particle1)
        for particle in self.particles:
            particle.update(dt)

    # Mouse press event
    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            print("Cow:", x, y)
            new_cow = MushroomCow(init_pos=(x, y))
            self.mushroom_cows.append(new_cow)

    def on_draw(self):
        print("Drawing window...")

        # Window clear
        window.clear()

        # Draw background
        background_batch.draw()

        # Draws and updates the cows
        for cow in self.mushroom_cows:
            cow.Cow_Batch.draw()

        # Draw particles
        for particle in self.particles:
            particle.update(1 / 60)  # Call the update method for each particle
            particle.particle_batch.draw()

        # Draw fps for performance insights
        fps_display.draw()


"""

    > __main__
    -------------------
    @brief  :  Sets properties for MainWindow
    
"""
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
