"""

from pyglet.math import *

p1 = Vec2(200, 100)
radius1 = 100
p2 = Vec2(120, 100)
radius2 = 200

u = p1 - p2
d = u.mag
if d < radius1 + radius2:
    pass # Collission

p = Vec2(100,200)
u = Vec2(300,100)
q = Vec2(400, 100)

v = q - p
pr = (u.dot(v) / u.dot(u)) * u
diff = v - pr
d = diff.mag

if d < radius1:
    pass # Collission
"""

# check u.dot(v) / u.dot(u) < 0, > 1, otherwise above.

"""
    Circles color collision

    for i in range(len(circles)):
        circles[i].color = color2

    for i in range(len(circles))
        for j in range(i+1, len(circles)):
            if "collision":
                circles[i].color = color1 # Colliding
                circles[j].color = color1



    How do you know if a line has left the screen?
    
    Params x1, y1, x2, y2 points on the line
    minx, maxx = min(x1, x2), max(x1, x2)
    
    if(minx > width):
        x1 = x1 - width - (maxx - minx)
        x2 = x2 - width - (maxx - minx)
        

"""

print(d)