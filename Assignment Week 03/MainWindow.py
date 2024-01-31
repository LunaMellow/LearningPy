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

# Pyglet imports
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

        # Store all the cows
        self.mushroom_cows = []

    # Mouse press event
    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            print("Cow spawned at:", x, y)
            new_cow = MushroomCow(init_pos=(x, y))
            self.mushroom_cows.append(new_cow)

    # On draw event
    def on_draw(self):

        # Window clear
        window.clear()

        # Draw background
        background_batch.draw()

        # Draws and updates the cows
        for cow in self.mushroom_cows:
            cow.Cow_Batch.draw()

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
    background = NewShape('rectangle', x=0, y=0, width=3820, height=2560, color=(20, 20, 20), batch=background_batch)

    # Fps
    fps_display = FPSDisplay(window)

    # Run the application
    run()
