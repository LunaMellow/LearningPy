"""

    > MushroomCow
    -------------------
    @brief  :  Pyglet Mushroom Cow from Minecraft
    @author :  Luna Sofie Bergh

"""

# File imports
from Mat3 import Mat3
from NewShape import NewShape

# Library Imports
from pyglet.graphics import *
from pyglet.math import *


class MushroomCow:

    #########################################################
    #                                                       #
    #       THIS IS WHERE ALL THE COW PIXELS ARE STORED     #
    #                                                       #
    #########################################################

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

    ##########################################################
    #                                                        #
    #       THIS IS WHERE WE CREATE PIXELS FROM THE MAPS     #
    #                                                        #
    ##########################################################
    # Create each body part line for line, pixel by pixel
    def create_part(self, shape_type, color_map, x_offset, y_offset, batch):
        # Pixel size
        p = 10

        for i, line in enumerate(color_map):
            for j, color in enumerate(line):
                self.Cow_Parts.append(NewShape(
                    shape_type=shape_type,
                    x=(self.position.x + x_offset) + p * j,
                    y=(self.position.y + y_offset) - p * i,
                    width=p,
                    height=p,
                    color=color,
                    batch=batch)
                )

    ##########################################################
    #                                                        #
    #           THIS IS WHERE WE INITIATE THE COWS           #
    #                                                        #
    ##########################################################

    # Initiate Cow instance
    def __init__(self, init_pos):

        # Cow batch
        self.Cow_Batch = Batch()

        # Store all cow parts
        self.Cow_Parts = []

        # 2D vector position of the Cow
        self.position = Vec2(*init_pos)

        # # Cow Matrixes
        # self.translation_matrix = Mat3()
        # self.rotation_matrix = Mat3()
        # self.scaling_matrix = Mat3()
        # self.combined_matrix = Mat3()

        ##########################################################
        #                                                        #
        #          THIS IS WHERE WE CREATE THE COW PARTS         #
        #                                                        #
        ##########################################################

        # Create Mushroom part
        self.create_part('rectangle', self.mushroom_colors, 120, 40, self.Cow_Batch)

        # Create Backlegs front and back parts
        self.create_part('rectangle', self.back_legs_colors, 60, -100, self.Cow_Batch)
        self.create_part('rectangle', self.back_legs_colors, 180, -100, self.Cow_Batch)

        # Create Frontlegs front and back parts
        self.create_part('rectangle', self.front_legs_colors, 40, -100, self.Cow_Batch)
        self.create_part('rectangle', self.front_legs_colors, 160, -100, self.Cow_Batch)

        # Create Body part
        self.create_part('rectangle', self.body_colors, 40, -20, self.Cow_Batch)

        # Create Head part
        self.create_part('rectangle', self.head_colors, 0, 0, self.Cow_Batch)

        # Create Ears part
        self.create_part('rectangle', self.ear_colors, -10, 10, self.Cow_Batch)

    ##########################################################
    #                                                        #
    #       THIS IS WHERE WE MANIPULATE COW BEHAVIOUR        #
    #        MADE BY CHATGPT FOR EDUCATIONAL PURPOSES        #
    #                                                        #
    ##########################################################

    # def update_cow(self, dt):
    #     # Translate the entire cow to the right
    #     translation_speed = 100  # You can adjust the translation speed as needed
    #     self.translation_matrix = self.translation_matrix.translate(translation_speed * dt, 0)
    #
    #     # Combine the transformation matrices
    #     self.combined_matrix = self.translation_matrix @ self.rotation_matrix @ self.scaling_matrix
    #
    #     # Apply the combined transformation to all cow parts
    #     for part in self.Cow_Parts:
    #         # Transform the part's position using the combined matrix
    #         x, y = self.combined_matrix.transform_point(part.x, part.y)
    #         part.shape_instance.x = x
    #         part.shape_instance.y = y
