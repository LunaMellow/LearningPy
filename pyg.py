"""
Assigment week 3
7b

We want you to draw a creature using the shapes you used in the previous
assignment. This is worth 5 points.

A cat is our suggestion, although you can do whatever, as long as your
creature has a similar depth and complexity to what we describe below. Also,
you will not be graded on artistic ability.

Each part should be one shape. You can use different kinds of shapes, or
stick with one shape for all body parts, for instance a rectangle.
(Yes, we allow square shaped cats - just try to keep it simple).

We want to see (at least): 1 main body together with 4 paws, 4 legs,
4 thighs, 1 head, 2 ears and finally a tail divided into three separate parts.
Each body part (except the main body) has one body part it is attached to.

For instance, a paw attached is attached to a leg, a leg is attached to a
thigh and the thigh is attached to the main body.

Each body part has a position with respect to the position of the
parent body part. In other words, the parent acts as the origin for the
position of its children.

If the position of a body part changes, then it will changes for
all children of that body part.

When I draw the paw we do so at the screenposition:
    pawposition + thighposition + legposition + mainbodyposition


To show that everything works: make the cat move across the screen by
only changing the position of the mainbody.

@author: Sara Paulina Boudzakhet
"""
import pyglet
from pyglet import shapes
# Importing from random library the "randint"
from random import randint

window = pyglet.window.Window(1200, 700)
batch = pyglet.graphics.Batch()

# BACKGROUND
backgorund = shapes.Rectangle(0, 0, 1200, 700, color=(0, 0, 0), batch=batch)
circleList = []
for x in range(0, 1000):
    circleList.append(shapes.Circle(randint(0, 1200), randint(0, 700),
                                    randint(0, 2), color=(randint(0, 255), randint(0, 0),
                                                          randint(0, 255), randint(40, 200)), batch=batch))

# THE DOG

# TIGHT BACK
tight2 = shapes.Rectangle(460, 200, 40, 60, color=(173, 172, 173), batch=batch)
tight2.rotation = -40
tight3 = shapes.Rectangle(610, 220, 40, 60, color=(173, 172, 173), batch=batch)
tight3.rotation = 19

# LEG BACK
leg2 = shapes.Rectangle(505, 163, 40, 60, color=(122, 120, 122), batch=batch)
leg2.rotation = -50
leg3 = shapes.Rectangle(605, 170, 40, 50, color=(122, 120, 122), batch=batch)
leg3.rotation = 5

# PAW BACK
paw2 = shapes.Rectangle(506, 163, 40, 20, color=(173, 172, 173), batch=batch)
paw2.rotation = -53
paw3 = shapes.Rectangle(603, 163, 40, 20, color=(173, 172, 173), batch=batch)
paw3.rotation = 7

# Body
body = shapes.Rectangle(400, 250, 300, 140, color=(217, 215, 216), batch=batch)

# Face and Head
collar = shapes.Rectangle(390, 290, 100, 100, color=(140, 7, 23), batch=batch)
head = shapes.Rectangle(350, 310, 120, 110, color=(207, 204, 206), batch=batch)

# Tights FRONT
tight1 = shapes.Rectangle(370, 220, 40, 60, color=(217, 215, 216), batch=batch)
tight1.rotation = 30
tight4 = shapes.Rectangle(695, 200, 40, 60, color=(217, 215, 216), batch=batch)
tight4.rotation = -30

# Legs FRONT
leg1 = shapes.Rectangle(360, 160, 40, 60, color=(168, 167, 165), batch=batch)
leg1.rotation = 10
leg4 = shapes.Rectangle(698, 163, 40, 50, color=(168, 167, 165), batch=batch)
leg4.rotation = -10

# Paws FRONT
paw1 = shapes.Rectangle(360, 155, 40, 20, color=(217, 215, 216), batch=batch)
paw1.rotation = 10
paw4 = shapes.Rectangle(701, 150, 40, 20, color=(217, 215, 216), batch=batch)
paw4.rotation = -10

# Tail
tail1 = shapes.Rectangle(700, 350, 60, 40, color=(217, 215, 216), batch=batch)
tail1.rotation = -3
tail2 = shapes.Rectangle(760, 352, 60, 40, color=(217, 215, 216), batch=batch)
tail2.rotation = -20
tail3 = shapes.Rectangle(810, 370, 20, 40, color=(168, 167, 165), batch=batch)
tail3.rotation = -20
# Eyes
eye1 = shapes.Rectangle(370, 370, 20, 20, color=(0, 0, 0), batch=batch)
eye2 = shapes.Rectangle(430, 370, 20, 20, color=(0, 0, 0), batch=batch)

# Eyes 1 border - left
bEye1 = shapes.Rectangle(350, 370, 20, 20, color=(255, 255, 255), batch=batch)
bEye2 = shapes.Rectangle(370, 390, 20, 20, color=(255, 255, 255), batch=batch)

# Eye patch

eyeP = shapes.Rectangle(390, 370, 40, 20, color=(181, 159, 121), batch=batch)

# Eye 2 border - right
bEye3 = shapes.Rectangle(450, 370, 20, 20, color=(255, 255, 255), batch=batch)
bEye4 = shapes.Rectangle(430, 390, 20, 20, color=(255, 255, 255), batch=batch)

# Mouth area
mouthb = shapes.Rectangle(380, 330, 60, 40, color=(222, 200, 180), batch=batch)
nose = shapes.Rectangle(400, 350, 20, 20, color=(0, 0, 0), batch=batch)
mouth = shapes.Rectangle(380, 310, 60, 20, color=(46, 45, 45), batch=batch)

# Ear 1 - left
ear1 = shapes.Rectangle(350, 420, 40, 40, color=(204, 203, 200), batch=batch)
earp1 = shapes.Rectangle(350, 420, 40, 20, color=(168, 167, 165), batch=batch)

# Ear 2 - right
ear2 = shapes.Rectangle(430, 420, 40, 40, color=(204, 203, 200), batch=batch)
earp2 = shapes.Rectangle(430, 420, 40, 20, color=(168, 167, 165), batch=batch)

# Texture for the background and the dog
starList = []
for x in range(0, 1000):
    starList.append(shapes.Star(randint(0, 1200), randint(0, 700),
                                randint(0, 75), randint(0, 75), num_spikes=5,
                                color=(randint(0, 255), randint(0, 100),
                                       randint(0, 255), randint(40, 200)), batch=batch))
for i in starList:
    i.opacity = randint(0, 15)


@window.event
def on_draw():
    window.clear()
    batch.draw()


pyglet.app.run()