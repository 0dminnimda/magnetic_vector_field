import numpy as np
from numpy import linalg as lrg
from math import sin, cos, pi, tau, atan2
import pygame
from pygame.locals import *
from pygame_draw import pyg_draw, mou_pos
from time import time as ti

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

    def set_vec(self, vec):
        self.vec = np.array(vec)

    def set_pos(self, pos):
        self.pos = np.array(pos)

    def set_x(self, x):
        self.vec[0] = x

    def set_y(self, y):
        self.vec[1] = y

    def set_x0(self, x0):
        self.pos[0] = x0

    def set_y0(self, y0):
        self.pos[1] = y0

    def set_mag(self, num, ret=0):
        if bool(ret):
            return self.vec*num/self.mag()
        else:
            if self.mag() != 0:
                self.vec = self.vec*num/self.mag()
            self.__mag = num

    def set_ang(self, angle):
        self.vec = np.array([self.__mag, 0])
        self.rotate(angle)

    def rotate(self, angle):
        rotation_matrix = [[np.cos(angle), np.sin(angle)], [-np.sin(angle), np.cos(angle)]]
        self.vec = np.dot(rotation_matrix, self.vec)
        self.set_mag(self.__mag)

    def mag(self):
        return lrg.norm(self.vec)

    def dot(self, vec):
        return np.vdot(self.vec, vec)

    def norm(self, ret=1):
        if bool(ret):
            return self.set_mag(1, ret)
        else:
            self.set_mag(1)

    def mul(self, num):
        self.vec *= num
        self.__mag = self.mag()

    def ang(self):
        return -np.arctan2(*self.vec[::-1])

    def ang_betw(self, oth):
        return abs(self.ang()-oth.ang())

    def proj(self, oth):
        return Vector(*self.dot(oth.norm())*oth.norm(), *self.pos)

    def end_pos(self):
        return self.vec + self.pos



    def draw(self, pd, r=1, col="red", arrow=0):
        if bool(arrow):
            pts = self.arrow_pts()
            pd.line(self.pos, sum(pts)/3, col, r)
            pd.poly(pts, col)
        else:
            pd.line(self.pos, self.vec+self.pos, col, r)

    def draw_arrow(self, pd):
        pd.poly(self.arrow_pts())
        
    def arrow_pts(self, rat=0.15, mul=0.4):
        vec = self.vec
        vec_s = vec*rat
        vec_l = vec-vec_s
        p1 = vec_l+(vec_s[1]*mul, -vec_s[0]*mul)
        p2 = vec_l+(-vec_s[1]*mul, vec_s[0]*mul)
        return self.pos+p1, self.pos+p2, self.end_pos()


pd = pyg_draw(0.5)
w, h = pd.cen()
clo = pd.clock

a = Vector(2, 2, w, h) * 50
a2 = Vector(2, 2, w, h) * 50

m = a.mag()
m2 = a2.mag()

#a.set_mag(1)
#a.rotate(pi*0.5)
#a.set_ang(pi)

ang = 0

run = True
while run:
    clo.tick(120)

    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            run = not True

    ang += 0.01
    #print(a.mag(), a.ang())
    a.set_ang(a.ang())
    a.rotate(-pi*0.001)
    print(a.ang_betw(a2))

    a.draw(pd, 4, arrow=1)
    a2.draw(pd, 4, arrow=1)

    a3 = a.proj(a2)
    a3.draw(pd, 4, arrow=1, col="lblue")

    a4 = a2.proj(a)
    a4.draw(pd, 4, arrow=1, col="lblue")

    pd.line(a3.end_pos(), a.end_pos(), "green", 2)
    pd.line(a4.end_pos(), a2.end_pos(), "green", 2)

    #a.mul(1.0005)

    pd.upd()
    pd.fill()

