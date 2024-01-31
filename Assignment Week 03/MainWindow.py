"""

    Assignment Week 03
    -------------------
    Question 7
    @brief   :  Pyglet shape behaviour
    @author  :  Luna Sofie Bergh
    @date    :  29-01-2024

    Please go to my github to see my strong
    dedication to this and my overall progress:
    https://github.com/LunaMellow/LearningPy

    PS
    -------------------
    I spent an ungodly amount of time on this
    cow and structure. Hope you guys appreciate
    my effort and dedication to making something
    really cool! Even tho I might not have everything
    correct and missing collisions, I will add it soon.

    I have spent most of my time tinkering with code
    structure, logic for the classes, function and
    modules that I have made. I went in with the
    intention of not just trying to pass the assignment
    but instead focus on how I can build a solid structure
    to use in the entire semester going forwards. So I
    might not have done everything the task asked me to,
    but I have learnt so incredibly much by learning pyglet
    this way, and just tinkering to find the best possible
    structure. Thank you for reading, I won't give up! :)

    Menu Description
    -------------------
    SPACE BAR : Spawn multiple cows for task B

"""

# File Imports
from MushroomCow import MushroomCow
from NewShape import NewShape
from Particles import Circles, Lines

# Library Imports
from random import randint
from pyglet import *
from pyglet.app import *
from pyglet.window import *
from pyglet.graphics import *


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
