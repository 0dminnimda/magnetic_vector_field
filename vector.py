import numpy as np
from numpy import linalg as lrg
from math import sin, cos, pi
import pygame
from pygame.locals import *
from pygame_draw import pyg_draw
from time import time as ti

#np.seterr(divide='ignore', invalid='ignore')

class Vector:
    def __init__(self, x, y, x1=0, y1=0):
        self.pos = np.array([x1, y1], dtype=float)
        self.vec = np.array([x, y], dtype=float)
        self.__mag = self.mag()

    def __str__(self):
        return f"<{self.vec[0]}, {self.vec[1]}>"
        
    def __repr__(self):
        return se.__str__()

    def __add__(self, oth):
        return Vector(*self.vec+oth.vec, *self.pos)
        
    def __sub__(self, oth):
        return Vector(*self.vec-oth.vec, *self.pos)
        
    def __mul__(self, num):
        return Vector(*self.vec*num, *self.pos)
        
    def __truediv__(self, num):
        return Vector(self.vec/num, *self.pos)

    def rotate(self, angle):
        rotation_matrix = [[np.cos(angle), np.sin(angle)], [-np.sin(angle), np.cos(angle)]]
        self.vec = np.dot(rotation_matrix, self.vec)
        self.scale(self.__mag)

    def scale(self, num):
        if self.mag() != 0:
            self.vec = self.vec*(num/self.mag())

    def mag(self):
        return lrg.norm(self.vec)

    def mul(self, num):
        self.vec *= num
        self.__mag = self.mag()

    def draw(self, pd, r=1, col="red"):
        pd.line(self.pos, self.vec+self.pos, col, r)


pd = pyg_draw(0.5)
w, h = pd.cen()
clo = pd.clock

a = Vector(2, 2, w, h) * 50
a2 = Vector(2, 2, w, h) * 50

m = a.mag()
m2 = a2.mag()

run = True
while run:
    clo.tick(120)

    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            run = not True

    print(a.mag())
    a.draw(pd, 5)
    a.rotate(-pi*0.001)
    #a.mul(1.0005)
    #print(a.__dict__)
    #print(a.mag()-m)

    pd.upd()
    pd.fill()

