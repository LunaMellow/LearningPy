"""

    > Mat3
    -------------------
    @brief  :  Mat3 Library
    @author :  ChatGPT

"""

##########################################################
#                                                        #
#       CHATGPT MADE THIS LIBRARY. I AM ONLY USING       #
#          IT FOR TESTING PURPOSES AND LEARNING          #
#                                                        #
##########################################################

# Library imports
from math import *


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
