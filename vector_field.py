import numpy as np
#from math import sin, cos, pi, tau, atan2
import pygame
from pygame.locals import *
from pygame_draw import pyg_draw, mou_pos
from time import time as ti
from vector import *


def prop(max1, max2, val1):
    val2 = max2*val1/max1
    return val2

def pt_rot(arr, pt, func):
    global cols, rows
    a=0
    for obb, i in zip(arr, rows):
        for ob, j in zip(obb, cols):
            a += 1
            func(ob, i, j, pt)

def Bvec(i, j, pt):
    v = Vector(i-pt[1], j-pt[0])
    r = v.mag()
    theta = angy(v)
    phi = 0
    B = diopole(theta, phi, r) 
    return Vector(B[0], B[-1])

def trans(ob, i, j, pt):
    a = Bvec(i, j, (pt[0], pt[1]-120))
    b = Bvec(i, j, (pt[0], pt[1]+120))
    #set_ang(ob, a.ang()-pi)
    set_ang(ob, (a.ang() + b.ang()))
    # set_mag(ob, Bv.mag()*10**6.25)


def diopole(theta, phi, r, mu=1):
    xh = np.array([1, 0, 0])
    yh = np.array([0, 1, 0])
    zh = np.array([0, 0, 1])
    vec = (sin(theta)*cos(theta)*(cos(phi)*xh + sin(phi)*yh)
           + (cos(theta)**2 - 1/3)*zh)
    return 3*mu/r**3 * vec

pd = pyg_draw(0.75)
w, h = pd.cen()
clo = pd.clock

def rd(num=1):
    return tau*np.random.random_sample((num))-pi

row, col = 24, 35

arr = []
rows = np.linspace(25, 2*h-25, row)
cols = np.linspace(25, 2*w-25, col)
for i in range(len(rows)):
    arr.append([])
    for j in range(len(cols)):
        arr[i].append(mul(norm(set_ang(Vector(*rd(2), cols[j], rows[i]), 0)), 25))
        # prop(col*row, pi, i+j)
        #set_ang(arr[i][j], (Vector(cols[j]-w-120, rows[i]-h).ang() + Vector(cols[j]-w+120, rows[i]-h).ang() + pi)/2)

#pt_rot(arr)

pt_rot(arr, (w, h), trans)

#arr = [mul(norm(set_ang(Vector(*rd(2), w, h), rd())), 50) for i in range(30)]

a = 0.25/2

run = True
while run:
    #clo.tick(240)

    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            run = not True

    for i in arr:
        for j in i:
            #rotate(j, a)
            j.draw(pd, 1, arrow=1, rat=0.4, mul=0.3, col=(127, 255, 255))

    pd.upd()
    pd.fill()