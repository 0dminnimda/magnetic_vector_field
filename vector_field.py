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

def pt_rot(arr, pt):
    for ar, i in zip(arr, cols):
        for r, j in zip(ar, rows):
            set_ang(r, Vector(i-pt[0], j-pt[1]).ang())

pd = pyg_draw(0.75)
w, h = pd.cen()
clo = pd.clock

def rd(num=1):
    return tau*np.random.random_sample((num))-pi

row, col = 30, 30

arr = []
rows = np.linspace(25, 2*h-25, row)
cols = np.linspace(25, 2*w-25, col)
for i in range(len(rows)):
    arr.append([])
    for j in range(len(cols)):
        arr[i].append(mul(norm(set_ang(Vector(*rd(2), cols[j], rows[i]), 0)), 25))
        # prop(col*row, pi, i+j)
        set_ang(arr[i][j], Vector(cols[j]-w, rows[i]-h).ang()+pi)

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