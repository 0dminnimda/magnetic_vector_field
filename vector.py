import numpy as np
from numpy import linalg as lrg
from math import sin, cos, pi
import pygame
from pygame.locals import *
from pygame_draw import pyg_draw

class Vector:
    def __init__(self, x, y, x1=0, y1=0):
        self.vec = np.array([x, y], dtype=float)
        self.pos = np.array([x1, y1], dtype=float)

    def __str__(self):
        return f"<{self.vec[0]}, {self.vec[1]}>"
        
    def __repr__(self):
        return se.__str__()

    def __add__(self, oth):
        return Vector(*self.vec+oth.vec, *self.pos)
        
    def __sub__(self, oth):
        return Vector(*self.vec-oth.vec, *self.pos)
        
    def __mul__(self, oth):
        return Vector(*self.vec*oth, *self.pos)
        
    def __truediv__(self, oth):
        return Vector(self.vec/oth, *self.pos)

    def rotate(self, angle):
        tr = np.array([[cos(angle), -sin(angle)], [sin(angle), cos(angle)]])
        self.vec = np.dot(tr, self.vec-self.pos) + self.pos

    def draw(self, pd, r=1, col="red"):
        pd.line(self.pos, self.vec, col, r, blend=0)


pd = pyg_draw(0.5)
w, h = pd.cen()
clo = pd.clock

a = Vector(2, 2, w, h) * 100

#print(list(a.vec))
#print(np.dot([[5], [6]], [[2, 3]]))

run = True
while run:
    clo.tick(120)

    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            run = not True

    a.draw(pd, 5)
    a.rotate(pi*0.001)

    pd.upd()
    pd.fill()

