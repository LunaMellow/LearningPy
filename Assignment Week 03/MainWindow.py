"""

    Assignment Week 03
    -------------------
    Question 7

    @brief   :  Pyglet shape behaviour
    @author  :  Luna Sofie Bergh
    @date    :  29-01-2024

    Please go to my GitHub to see my strong
    dedication to this and my overall progress:
    https://github.com/LunaMellow/LearningPy
    https://github.com/LunaMellow/LearningPy/commits/main/

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
    to use in the entire semester going forwards.

    So I might not have done everything the task asked me to,
    but I have learnt so incredibly much by learning pyglet
    this way, and just tinkering to find the best possible
    structure. I tried collisions on my own, with chatgpt,
    with all the sources I could find, but I couldn't find
    a way to do it yet with the structure I created. But
    that's part of programming, eventually when I do find
    out how, I will be incredibly educated in how to implement
    it into such a structure. It will be amazing in the end,
    but even after working up to 10 hours a day with this,
    it wasn't enough for me to finish everything.

    Thank you for reading, but don't u worry. I won't give up! :)

    Menu Description
    -------------------
    SPACE BAR : Spawn multiple cows for task B

"""

# File Imports
from MushroomCow import MushroomCow     # My mushroom cow module
from NewShape import NewShape           # My NewShape module
from Particles import Circles, Lines    # My Particle module

# Library Imports
from random import *
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

        # Store all the shapes
        self.particles = []
        self.mushroom_cows = []

        # Draw all the circles
        for i in range(50):
            new_circle = Circles()
            self.particles.append(new_circle)

        # Draw all the lines
        for i in range(50):
            new_line = Lines(window_height=self.wy, start_outside=True)
            self.particles.append(new_line)

    # Update the particles
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
            particle.update(1 / 60, self.wx, self.wy)
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

    # Updates
    pyglet.clock.schedule(window.update)

    # Fps Display
    fps_display = FPSDisplay(window)

    # Run the application
    run()
