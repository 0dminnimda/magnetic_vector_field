import numpy as np
from numpy import linalg as lrg
from math import sin, cos, pi, tau, atan2

class Vector:
    def __init__(self, *args, **kwargs):
        x1=0
        y1=0

        if len(args) == 4:
            x, y, x1, y1 = args

        elif len(args) == 2:
            if isinstance(args[0], (int, float)):
                x = args[0]
                if isinstance(args[1], (int, float)):
                    y = args[1]
                else:
                    raise Exception("не оба компонента числа или массивы")
            else:
                if isinstance(args[1], (int, float)):
                    raise Exception("не оба компонента числа или массивы")
                else:
                    x, y = args[0]
                    x1, y1 = args[1]

        elif len(args) == 1:
            x, y = args[0][0]
            x1, y1 = args[0][1]

        self.pos = np.array([x1, y1], dtype=float)
        self.vec = np.array([x, y], dtype=float)
        self._mag = self.mag()

    def __str__(self):
        return f"<{self.vec[0]}, {self.vec[1]}>"
        
    def __repr__(self):
        return self.__str__()

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

    def set_mag(self, num):
        if self.mag() != 0:
            self.vec = self.vec*num/self.mag()
        self._mag = num

    def set_ang(self, angle):
        self.vec = np.array([self._mag, 0])
        self.rotate(angle)

    def rotate(self, angle):
        rotation_matrix = [[cos(angle), sin(angle)], [-sin(angle), cos(angle)]]
        self.vec = np.dot(rotation_matrix, self.vec)
        self.set_mag(self._mag)

    def mag(self):
        return lrg.norm(self.vec)

    def dot(self, oth):
        return np.vdot(self.vec, oth.vec)

    def norm(self):
        self.set_mag(1)

    def mul(self, num):
        self.vec *= num
        self._mag = self.mag()

    def ang(self):
        return -np.arctan2(*self.vec[::-1])

    def angy(self):
        return -np.arctan2(*self.vec)%tau-pi

    def ang_betw(self, oth):
        return -(abs((self.ang()-oth.ang())%tau-pi)-pi)

    def proj(self, oth):
        return proj(self, oth)

    def end_pos(self):
        return self.vec + self.pos

    def copy(self):
        return Vector(*self.vec, *self.pos)

    # drawing part

    def draw(self, pd, r=1, col="red", arrow=0, rat=0.15, mul=0.4):
        if bool(arrow):
            pts = self.arrow_pts(rat, mul)
            pd.line(self.pos, sum(pts)/3, col, r)
            pd.poly(pts, col)
        else:
            pd.line(self.pos, self.vec+self.pos, col, r)

    def draw_arrow(self, pd, rat=0.15, mul=0.4):
        pd.poly(self.arrow_pts(rat, mul))
        
    def arrow_pts(self, rat=0.15, mul=0.4):
        vec = self.vec
        vec_s = vec*rat
        vec_l = vec-vec_s
        p1 = vec_l+(vec_s[1]*mul, -vec_s[0]*mul)
        p2 = vec_l+(-vec_s[1]*mul, vec_s[0]*mul)
        return self.pos+p1, self.pos+p2, self.end_pos()

for _ in [1]:
    def isiterable(obj):
        return hasattr(obj, '__contains__')

    def vec_sum(arr):
        sum = Vector(0, 0)
        for i in arr:
            sum += i
        return sum

    def set_vec(obj, vec):
        obj.vec = np.array(vec)
        return obj

    def set_pos(obj, pos):
        obj.pos = np.array(pos)
        return obj

    def set_x(obj, x):
        obj.vec[0] = x
        return obj

    def set_y(obj, y):
        obj.vec[1] = y
        return obj

    def set_x0(obj, x0):
        obj.pos[0] = x0
        return obj

    def set_y0(obj, y0):
        obj.pos[1] = y0
        return obj

    def set_mag(obj, num):
        if obj.mag() != 0:
            obj.vec = obj.vec*num/obj.mag()
        obj._mag = num
        return obj

    def set_ang(obj, angle):
        obj.vec = np.array([obj._mag, 0])
        obj.rotate(angle)
        return obj

    def rotate(obj, angle):
        #rotation_matrix = 
        obj.vec = np.dot([[cos(angle), sin(angle)], [-sin(angle), cos(angle)]], obj.vec)
        obj.set_mag(obj._mag)
        return obj

    def mag(obj):
        return lrg.norm(obj.vec)

    def ang(obj):
        return -np.arctan2(*obj.vec[::-1])

    def angy(obj):
        return -np.arctan2(*obj.vec)%tau-pi

    def ang_betw(obj, oth):
        return -(abs((obj.ang()-oth.ang())%tau-pi)-pi)

    def dot(obj, oth):
        return np.vdot(obj.vec, oth.vec)

    def norm(obj):
        obj.set_mag(1)
        return obj

    def mul(obj, num):
        obj.vec *= num
        obj._mag = obj.mag()
        return obj

    def proj(obj, oth):
        oth = oth.copy()
        v = dot(obj, norm(oth))*norm(oth).vec
        return Vector(*v, *oth.pos)

    def comp(obj, oth):
        oth = oth.copy()
        return dot(obj, norm(oth))

    def end_pos(obj):
        return obj.vec + obj.pos

    def copy(obj):
        return Vector(*obj.vec, *obj.pos)

if __name__ == "__main__":

    import pygame
    from pygame.locals import *
    from pygame_draw import pyg_draw, mou_pos
    from time import time as ti

    pd = pyg_draw(0.5)
    w, h = pd.cen()
    clo = pd.clock

    a = Vector(2, 2, w, h) * 50
    a2 = Vector(2, 2, w, h) * 50

    m = a.mag()
    m2 = a2.mag()

    #a.set_mag(1)
    #a.rotate(pi*0.5)
    a2.set_ang(pi*0.5)
    print(a2.angy())

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
        print(a.angy(), a.ang())
        print(a.ang_betw(a2))

        a.draw(pd, 4, arrow=1)
        a2.draw(pd, 4, arrow=1)

        a3 = a.proj(a2)
        a3.draw(pd, 4, arrow=1, col="lblue")

        a4 = proj(a2, a)
        a4.draw(pd, 4, arrow=1, col="lblue")

        pd.line(a3.end_pos(), a.end_pos(), "green", 2)
        pd.line(a4.end_pos(), a2.end_pos(), "green", 2)

        #a.mul(1.0005)

        pd.upd()
        pd.fill()

