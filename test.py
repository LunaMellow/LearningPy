import sympy as sp
import math as m


# scalar product of u and v
# def dot(u, v):
#     return u[0] * v[0] + u[1] * v[1] + u[2] * v[2]


# # length of u
# def absv(u):
#     return sp.sqrt(sum(x ** 2 for x in u))
#
#
# # unit vector in the direction of u
# def normalise(u):
#     return [x / absv(u) for x in u]
#
#
# def cross_product(u, v):
#     w_1 = u[1] * v[2] - u[2] * v[1]
#     w_2 = u[2] * v[0] - u[0] * v[2]
#     w_3 = u[0] * v[1] - u[1] * v[0]
#     return [w_1, w_2, w_3]
#
#
# def area_paragram(u, v):
#     return absv(cross_product(u, v))
#
#
# def sine_angle(u, v):
#     return absv(cross_product(u, v)) / (absv(u) * absv(v))


# def counter(someList):
#     div_by_3 = 0
#
#     for i in someList:
#         if i % 3 == 0:
#             div_by_3 += 1
#
#     return div_by_3
#
#
#
#
#
# # adds two vectors
# def add(u, v):
#     return [u[j] + v[j] for j in range(3)]
#
#
# # scalar multiplication of scalar k and vector v
# def mul(k, v):
#     return [[k[i] * v[i][j] for j in range(3)] for i in range(3)]
#
# def dot(u, v):
#     return [sum(u[i][j] * v[i][j] for j in range(3)) for i in range(3)]
#
#
# # the length of u
# def vabs(u):
#     return [sp.sqrt(sum(u[i][j]**2 for i in range(3))) for j in range(3)]


# def cross(u, v):
#     return [[u[i][1] * v[i][2] - u[i][2] * v[i][1],
#              u[i][2] * v[i][0] - u[i][0] * v[i][2],
#              u[i][0] * v[i][1] - u[i][1] * v[i][0]] for i in range(3)]
#
#
# # the unit vector in the same direction of u
# def normalise(u):
#     pass
#
#
# # projection of u onto v
# def project(u, v):
#     pass
#
#
# k = [1, 2, 3]
#
# # Example vector
#
# u = [[69, 55, 54], [51, 60, 59], [52, 51, 64]]
# v = [[56, 60, 53], [66, 60, 54], [52, 70, 51]]
#
# someList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numberList = [15, 11, 3, 7, 28, 99, 83, 41, 92, 50, 68, 79]
#
# print(cross(u,v))
# print(normalise(u))
# print(project(u,v))

def counter(someList):

    # Return 0 if list is empty
    if not someList:
        return 0
    else:
        max_l = 1
        current_l = 1

        # Check for length of largest sublist
        for i in range(1, len(someList)):
            current_l = current_l + 1 if someList[i] > someList[i - 1] else 1
            max_l = max(max_l, current_l)

        return max_l

manyLists = [[6, 5, 4, 4, 8, 10, 3, 5, 1, 3, 3, 5, 9, 5, 8, 9, 3, 6, 1, 8], [4, 10, 9, 9, 4, 1, 9, 10, 3, 2, 1, 7, 10, 9, 4, 6, 2, 8, 8, 9], [3, 6, 8, 10, 5, 3, 4, 3, 6, 7, 4, 10, 7, 2, 10, 4, 1, 5, 3, 9], [9, 2, 4, 5, 9, 4, 10, 5, 4, 5, 10, 6, 8, 10, 10, 6, 1, 8, 5, 9], [1, 9, 1, 5, 3, 6, 9, 9, 5, 10, 9, 2, 9, 7, 2, 1, 7, 4, 5, 9], [6, 4, 5, 10, 10, 8, 10, 1, 8, 1, 3, 9, 1, 2, 6, 10, 8, 4, 9, 3], [6, 4, 6, 4, 4, 10, 9, 10, 2, 2, 5, 1, 7, 7, 7, 7, 10, 2, 7, 6], [2, 3, 4, 1, 7, 5, 7, 2, 2, 7, 9, 2, 9, 9, 6, 10, 3, 6, 5, 7], [10, 6, 4, 5, 7, 2, 1, 10, 7, 8, 10, 7, 8, 8, 4, 10, 7, 4, 8, 3], [9, 8, 2, 3, 4, 8, 10, 9, 2, 2, 5, 4, 8, 8, 1, 1, 3, 9, 1, 10], [4, 7, 1, 10, 5, 1, 5, 9, 3, 8, 5, 4, 5, 4, 5, 1, 2, 5, 8, 7], [10, 5, 8, 8, 7, 7, 6, 3, 2, 10, 1, 9, 5, 2, 6, 2, 3, 9, 1, 5], [7, 6, 4, 10, 3, 3, 6, 8, 7, 8, 8, 6, 6, 8, 9, 10, 9, 5, 3, 3], [2, 10, 4, 8, 10, 2, 6, 9, 5, 7, 2, 6, 2, 4, 6, 8, 7, 1, 4, 1], [9, 1, 2, 10, 3, 8, 1, 6, 2, 9, 3, 1, 5, 4, 3, 2, 9, 10, 4, 9], [8, 10, 5, 10, 8, 7, 5, 8, 6, 8, 3, 4, 4, 7, 3, 4, 3, 2, 4, 4], [7, 7, 8, 10, 10, 6, 3, 8, 4, 9, 1, 1, 3, 5, 6, 9, 2, 3, 9, 6], [9, 10, 4, 8, 9, 8, 5, 8, 5, 4, 5, 5, 8, 7, 6, 6, 4, 5, 8, 6], [3, 2, 6, 4, 2, 5, 1, 6, 5, 3, 8, 2, 7, 5, 3, 1, 3, 5, 2, 2], [5, 3, 10, 6, 1, 1, 2, 3, 3, 9, 7, 1, 5, 8, 2, 6, 1, 1, 4, 2]]

answer = [counter(l) for l in manyLists]
print(answer)
