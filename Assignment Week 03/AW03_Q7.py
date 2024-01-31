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

# Math imports
from math import *
from random import *

# Pyglet imports
from pyglet import *
from pyglet.app import *
from pyglet.window import *
from pyglet.graphics import *
from pyglet.shapes import *
from pyglet.math import *


#########################################################
#                                                       #
#         MAT3 HAD ISSUES, THIS IS FROM CHATGPT         #
#                                                       #
#########################################################

"""

    > Mat3
    -------------------
    @brief  :  Mat3 Python Library Helper

"""
class Mat3:
    def __init__(self, data=None):
        if data is None:
            self.data = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        else:
            self.data = data

    def __matmul__(self, other):
        result = Mat3([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]

        return result

    def transform_point(self, x, y):
        transformed_x = self.data[0][0] * x + self.data[0][1] * y + self.data[0][2]
        transformed_y = self.data[1][0] * x + self.data[1][1] * y + self.data[1][2]

        return transformed_x, transformed_y

    def translate(self, dx, dy):
        translation_matrix = Mat3([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
        return translation_matrix @ self

    def rotate(self, theta):
        cos_theta = cos(theta)
        sin_theta = sin(theta)

        rotation_matrix = Mat3([[cos_theta, -sin_theta, 0], [sin_theta, cos_theta, 0], [0, 0, 1]])
        return rotation_matrix @ self

    def scale(self, sx, sy):
        scaling_matrix = Mat3([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
        return scaling_matrix @ self


"""

    > NewShape
    -------------------
    @brief  :  Creates pyglet shapes

"""
class NewShape:
    # Shape Dictionary Map
    SHAPE_MAP = {
        'circle': Circle,
        'star': Star,
        'rectangle': Rectangle,
        'line': Line,
        'arc': Arc,
        'ellipse': Ellipse,
    }

    def __init__(self, shape_type, x, y, batch, **kwargs):
        # Check if given shape is in our shape dictionary
        if shape_type not in self.SHAPE_MAP:
            raise ValueError("Invalid shape type")

        # Creates shape instance based on shape_type provided
        shape_class = self.SHAPE_MAP[shape_type]
        self.x = x  # Add x attribute to store the x position
        self.y = y  # Add y attribute to store the y position
        self.shape_instance = shape_class(x=0, y=0, batch=batch, **kwargs)


"""

    > MushroomCow
    -------------------
    @brief  :  Cow :-)

"""
class MushroomCow:

    #########################################################
    #                                                       #
    #       THIS IS WHERE ALL THE COW PIXELS ARE STORED     #
    #                                                       #
    #########################################################

    # Store all the head colors for the cow
    head_colors = [
        [(152, 18, 19, 255), (160, 16, 17, 255), (160, 16, 17, 255), (164, 164, 164, 255),
         (164, 164, 164, 255), (164, 164, 164, 255), (150, 150, 150, 255), (160, 16, 17, 255)],
        [(152, 18, 19, 255), (160, 16, 17, 255), (160, 16, 17, 255), (164, 164, 164, 255),
         (164, 164, 164, 255), (164, 164, 164, 255), (150, 150, 150, 255), (152, 18, 19, 255)],
        [(0, 0, 0, 255), (0, 0, 0, 255), (160, 16, 17, 255), (150, 150, 150, 255),
         (164, 164, 164, 255), (160, 16, 17, 255), (0, 0, 0, 255), (0, 0, 0, 255)],
        [(0, 0, 0, 255), (0, 0, 0, 255), (160, 16, 17, 255), (150, 150, 150, 255),
         (160, 16, 17, 255), (160, 16, 17, 255), (0, 0, 0, 255), (0, 0, 0, 255)],
        [(160, 16, 17, 255), (160, 16, 17, 255), (160, 16, 17, 255), (160, 16, 17, 255),
         (160, 16, 17, 255), (160, 16, 17, 255), (160, 16, 17, 255), (160, 16, 17, 255)],
        [(152, 18, 19, 255), (160, 16, 17, 255), (176, 176, 176, 255), (176, 176, 176, 255),
         (176, 176, 176, 255), (176, 176, 176, 255), (152, 18, 19, 255), (160, 16, 17, 255)],
        [(152, 18, 19, 255), (176, 176, 176, 255), (0, 0, 0, 255), (95, 95, 95, 255),
         (95, 95, 95, 255), (0, 0, 0, 255), (176, 176, 176, 255), (152, 18, 19, 255)],
        [(152, 18, 19, 255), (160, 160, 160, 255), (95, 95, 95, 255), (73, 73, 73, 255),
         (73, 73, 73, 255), (95, 95, 95, 255), (176, 176, 176, 255), (152, 18, 19, 255)]
    ]

    # Store all the body colors for the cow
    body_colors = [
        [(115, 115, 115), (142, 13, 14), (142, 13, 14), (150, 14, 16), (120, 8, 9), (135, 11, 13), (150, 14, 16),
         (143, 143, 143), (135, 135, 135), (123, 123, 123), (123, 123, 123), (123, 123, 123), (130, 14, 16),
         (142, 13, 14), (131, 12, 13), (131, 12, 13), (131, 12, 13), (115, 12, 13)],
        [(142, 13, 14), (150, 14, 16), (150, 14, 16), (142, 13, 14), (120, 8, 9), (135, 11, 13), (150, 14, 16),
         (150, 14, 16), (160, 160, 160), (160, 160, 160), (143, 143, 143), (150, 14, 16), (150, 14, 16),
         (150, 14, 16), (150, 14, 16), (150, 14, 16), (150, 14, 16), (135, 14, 16)],
        [(150, 14, 16), (150, 14, 16), (150, 14, 16), (150, 14, 16), (120, 8, 9), (135, 11, 13), (150, 14, 16),
         (150, 14, 16), (150, 14, 16), (150, 14, 16), (160, 160, 160), (160, 160, 160), (160, 160, 160),
         (160, 160, 160), (160, 160, 160), (160, 160, 160), (160, 160, 160), (135, 14, 16)],
        [(150, 14, 16), (150, 14, 16), (150, 14, 16), (150, 14, 16), (120, 8, 9), (135, 11, 13), (150, 14, 16),
         (150, 14, 16), (150, 14, 16), (143, 143, 143), (160, 160, 160), (143, 143, 143), (150, 14, 16),
         (150, 14, 16), (150, 14, 16), (142, 13, 14), (131, 12, 13), (115, 12, 13)],
        [(143, 143, 143), (142, 13, 14), (142, 13, 14), (150, 14, 16), (120, 8, 9), (135, 11, 13), (142, 13, 14),
         (150, 14, 16), (142, 13, 14), (150, 14, 16), (142, 13, 14), (143, 143, 143), (150, 14, 16), (150, 14, 16),
         (150, 14, 16), (142, 13, 14), (131, 12, 13), (115, 12, 13)],
        [(115, 115, 115), (142, 13, 14), (150, 14, 16), (150, 14, 16), (120, 8, 9), (135, 11, 13), (150, 14, 16),
         (142, 13, 14), (150, 14, 16), (142, 13, 14), (143, 143, 143), (150, 14, 16), (150, 14, 16), (150, 14, 16),
         (142, 13, 14), (142, 13, 14), (142, 13, 14), (115, 12, 13)],
        [(120, 8, 9), (120, 8, 9), (120, 8, 9), (120, 8, 9), (120, 8, 9), (135, 11, 13), (150, 14, 16),
         (142, 13, 14), (150, 14, 16), (142, 13, 14), (142, 13, 14), (160, 160, 160), (160, 160, 160),
         (143, 143, 143), (150, 14, 16), (142, 13, 14), (142, 13, 14), (115, 12, 13)],
        [(135, 11, 13), (135, 11, 13), (135, 11, 13), (135, 11, 13), (135, 11, 13), (160, 160, 160),
         (160, 160, 160), (143, 143, 143), (150, 14, 16), (150, 14, 16), (150, 14, 16), (150, 14, 16),
         (150, 14, 16), (142, 13, 14), (142, 13, 14), (142, 13, 14), (131, 12, 13), (115, 12, 13)],
        [(142, 13, 14), (142, 13, 14), (142, 13, 14), (142, 13, 14), (142, 13, 14), (142, 13, 14), (115, 115, 115),
         (143, 143, 143), (143, 143, 143), (143, 143, 143), (115, 115, 115), (143, 143, 143), (131, 12, 13),
         (131, 12, 13), (131, 12, 13), (131, 12, 13), (131, 12, 13), (115, 12, 13)],
        [(142, 13, 14), (142, 13, 14), (142, 13, 14), (160, 160, 160), (143, 143, 143), (115, 115, 115),
         (143, 143, 143), (143, 143, 143), (143, 143, 143), (115, 115, 115), (143, 143, 143), (131, 12, 13),
         (131, 12, 13), (131, 12, 13), (131, 12, 13), (131, 12, 13), (131, 12, 13), (115, 12, 13)],
        [(131, 12, 13), (131, 12, 13), (131, 12, 13), (131, 12, 13), (116, 11, 13), (116, 11, 13), (116, 11, 13),
         (116, 11, 13), (116, 11, 13), (116, 11, 13), (116, 11, 13), (116, 11, 13), (131, 12, 13),
         (131, 12, 13), (131, 12, 13), (131, 12, 13), (116, 11, 13), (116, 11, 13)],
    ]

    back_legs_colors = [
        [(76, 9, 8), (82, 7, 9), (80, 9, 8), (78, 8, 9)],
        [(81, 9, 8), (79, 8, 9), (83, 7, 9), (80, 8, 9)],
        [(80, 7, 9), (82, 9, 8), (79, 9, 8), (78, 8, 9)],
        [(79, 8, 9), (81, 8, 9), (77, 9, 8), (83, 8, 9)],
        [(82, 8, 9), (78, 9, 8), (81, 7, 9), (79, 7, 9)],
        [(79, 9, 8), (82, 7, 9), (80, 8, 9), (78, 9, 8)],
        [(81, 7, 9), (79, 8, 9), (83, 9, 8), (80, 8, 9)],
        [(80, 8, 9), (82, 7, 9), (79, 9, 8), (78, 8, 9)],
        [(79, 8, 9), (81, 9, 8), (77, 9, 8), (83, 8, 9)],
        [(82, 8, 9), (78, 9, 8), (81, 7, 9), (79, 7, 9)],
        [(79, 9, 8), (82, 7, 9), (80, 8, 9), (78, 9, 8)],
        [(81, 7, 9), (79, 8, 9), (83, 9, 8), (80, 8, 9)],
        [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
    ]

    front_legs_colors = [
        [(131, 12, 13), (131, 12, 13), (131, 12, 13), (120, 12, 13)],
        [(145, 16, 14), (141, 14, 16), (149, 12, 16), (120, 12, 13)],
        [(145, 16, 14), (147, 16, 14), (141, 16, 14), (120, 12, 13)],
        [(145, 16, 14), (145, 14, 16), (137, 16, 14), (120, 12, 13)],
        [(145, 16, 14), (140, 16, 14), (145, 12, 16), (120, 12, 13)],
        [(103, 103, 103), (147, 12, 16), (144, 14, 16), (120, 12, 13)],
        [(128, 128, 128), (141, 14, 16), (149, 16, 14), (120, 12, 13)],
        [(128, 128, 128), (147, 12, 16), (141, 16, 14), (120, 12, 13)],
        [(103, 103, 103), (145, 16, 14), (137, 16, 14), (120, 12, 13)],
        [(103, 103, 103), (140, 16, 14), (145, 12, 16), (120, 12, 13)],
        [(141, 16, 14), (147, 12, 16), (144, 14, 16), (120, 12, 13)],
        [(145, 12, 16), (141, 14, 16), (149, 16, 14), (120, 12, 13)],
        [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
    ]

    mushroom_colors = [
        [(0, 0, 0, 0), (0, 0, 0, 0), (150, 14, 16), (0, 0, 0, 0), (0, 0, 0, 0)],
        [(0, 0, 0, 0), (150, 14, 16), (141, 14, 16), (150, 14, 16), (0, 0, 0, 0)],
        [(150, 14, 16), (145, 16, 14), (180, 16, 14), (144, 14, 16), (150, 14, 16)],
        [(160, 14, 16), (190, 12, 13), (200, 12, 13), (190, 12, 13), (160, 14, 16)],
        [(0, 0, 0, 0), (0, 0, 0, 0), (110, 110, 110), (0, 0, 0, 0), (0, 0, 0, 0)],
        [(0, 0, 0, 0), (0, 0, 0, 0), (143, 143, 143), (0, 0, 0, 0), (0, 0, 0, 0)]
    ]

    ear_colors = [
        [(136, 136, 136), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (136, 136, 136)],
        [(97, 97, 97), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (97, 97, 97)],
        [(64, 64, 64), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (64, 64, 64)]

    ]

    # Cow batch
    Cow_Batch = Batch()

    # Initiate Cow instance
    def __init__(self, init_pos):

        # Pixel size
        p = 10

        # Store all cow parts
        self.Cow_Parts = []

        # 2D vector position of the Cow
        self.position = Vec2(*init_pos)

        ##########################################################
        #                                                        #
        #       THIS IS WHERE WE CREATE PIXELS FROM THE MAPS     #
        #                                                        #
        ##########################################################

        # Mushroom
        for i, line in enumerate(self.mushroom_colors):
            for j, color in enumerate(line):
                self.Cow_Parts.append(NewShape(
                    shape_type='rectangle',
                    x=(self.position.x + 120) + p * j,
                    y=(self.position.y + 40) - p * i,
                    width=p,
                    height=p,
                    color=color,
                    batch=self.Cow_Batch)
                )

        # Backlegs front
        for i, line in enumerate(self.back_legs_colors):
            for j, color in enumerate(line):
                self.Cow_Parts.append(NewShape(
                    shape_type='rectangle',
                    x=(self.position.x + 60) + p * j,
                    y=(self.position.y - 100) - p * i,
                    width=p,
                    height=p,
                    color=color,
                    batch=self.Cow_Batch)
                )

        # Backlegs back
        for i, line in enumerate(self.back_legs_colors):
            for j, color in enumerate(line):
                self.Cow_Parts.append(NewShape(
                    shape_type='rectangle',
                    x=(self.position.x + 180) + p * j,
                    y=(self.position.y - 100) - p * i,
                    width=p,
                    height=p,
                    color=color,
                    batch=self.Cow_Batch)
                )

        # Frontlegs front
        for i, line in enumerate(self.front_legs_colors):
            for j, color in enumerate(line):
                self.Cow_Parts.append(NewShape(
                    shape_type='rectangle',
                    x=(self.position.x + 40) + p * j,
                    y=(self.position.y - 100) - p * i,
                    width=p,
                    height=p,
                    color=color,
                    batch=self.Cow_Batch)
                )

        # Frontlegs back
        for i, line in enumerate(self.front_legs_colors):
            for j, color in enumerate(line):
                self.Cow_Parts.append(NewShape(
                    shape_type='rectangle',
                    x=(self.position.x + 160) + p * j,
                    y=(self.position.y - 100) - p * i,
                    width=p,
                    height=p,
                    color=color,
                    batch=self.Cow_Batch)
                )

        # Body
        for i, line in enumerate(self.body_colors):
            for j, color in enumerate(line):
                self.Cow_Parts.append(NewShape(
                    shape_type='rectangle',
                    x=(self.position.x + 40) + p * j,
                    y=(self.position.y - 20) - p * i,
                    width=p,
                    height=p,
                    color=color,
                    batch=self.Cow_Batch)
                )

        # Head
        for i, line in enumerate(self.head_colors):
            for j, color in enumerate(line):
                self.Cow_Parts.append(NewShape(
                    shape_type='rectangle',
                    x=self.position.x + p * j,
                    y=self.position.y - p * i,
                    width=p,
                    height=p,
                    color=color,
                    batch=self.Cow_Batch)
                )

        # Ears
        for i, line in enumerate(self.ear_colors):
            for j, color in enumerate(line):
                self.Cow_Parts.append(NewShape(
                    shape_type='rectangle',
                    x=(self.position.x - 10) + p * j,
                    y=(self.position.y + 10) - p * i,
                    width=p,
                    height=p,
                    color=color,
                    batch=self.Cow_Batch)
                )

        #########################################################
        #                                                       #
        #  THIS IS WHERE ALL THE MATRICE TRANSFORMATION STARTS  #
        #   THIS IS DONE BY CHATGPT BECUAUSE I NEEDED TO GAIN   #
        #           SOME FORM OF UNDERSTANDING FIRST            #
        #                                                       #
        #########################################################

        self.translation_matrix = Mat3()
        self.rotation_matrix = Mat3()
        self.scaling_matrix = Mat3()
        self.combined_matrix = Mat3()

    def update_cow(self, dt):

        # Translate the cow
        self.translation_matrix = self.translation_matrix.translate(100 * dt, 100 * dt)

        # Rotate the cow
        self.rotation_matrix = self.rotation_matrix.rotate(0.1)  # Replace 0.1 with your desired rotation angle

        # Scale the cow
        self.scaling_matrix = self.scaling_matrix.scale(1.01, 1.01)

        # Combine all transformations
        self.combined_matrix = self.translation_matrix @ self.rotation_matrix @ self.scaling_matrix

        # Apply transformations to each shape
        for shape in self.Cow_Parts:
            # Get the transformed position using the new apply_transformation method
            transformed_position = self.combined_matrix.transform_point(shape.x, shape.y)
            # Update the shape's position with the transformed position
            shape.shape_instance.x, shape.shape_instance.y = transformed_position


"""

    > MainWindow
    -------------------
    @brief  :  Initializes the main window

"""
class MainWindow(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window size
        self.size = list(self.get_size())
        self.wx, self.wy = self.size[0], self.size[1]

        # Store all the cows
        self.mushroom_cows = []

        # Starting checkpoint
        print("\nStarted correctly")

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            new_cow = MushroomCow(init_pos=(x-75, y+50))
            self.mushroom_cows.append(new_cow)

    def on_draw(self):
        # Window clear
        window.clear()

        # Draw background
        background_batch.draw()

        # Draws and updates the cows
        for cow in self.mushroom_cows:
            cow.update_cow(1 / 60)
            cow.Cow_Batch.draw()

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

    fps_display = FPSDisplay(window)

    run()
