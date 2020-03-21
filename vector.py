import numpy as np
from numpy import linalg as lrg
from math import sin, cos, pi
import pygame
from pygame.locals import *
from pygame_draw import pyg_draw

class Vector:
    def __init__(self, x, y):
        self.vec = np.array([x, y], dtype=float)

    def __str__(self):
        return f"<{self.vec[0]}, {self.vec[1]}>"
        
    def __repr__(self):
        return se.__str__()

    def rotate(self, angle):
        tr = np.array([[cos(angle), -sin(angle)], [sin(angle), cos(angle)]])
        return tr

    def draw(self, pd, r=1, col="red"):
        pd.line(self.vec, [0, 0], col, r)


a = Vector(5, 6)
print(a.rotate(pi*0.9))
#print(np.dot([[5], [6]], [[2, 3]]))

pd = pyg_draw(0.5)

run = True
while run:
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            run = not True

    a.draw(pd)

    pd.upd()
    pd.fill()

