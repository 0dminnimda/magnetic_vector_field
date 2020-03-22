import numpy as np
#from math import sin, cos, pi, tau, atan2
import pygame
from pygame.locals import *
from pygame_draw import pyg_draw, mou_pos
from time import time as ti
from vector import *

pd = pyg_draw(0.5)
w, h = pd.cen()
clo = pd.clock

def rd(num=1):
    return tau*np.random.random_sample((num))-pi

row, col = 10, 10

arr = []
for i in np.linspace(25, 2*w-25, col):
    for j in np.linspace(25, 2*h-25, row):
        arr.append(mul(norm(set_ang(Vector(*rd(2), i, j), rd())), 25))

#arr = [mul(norm(set_ang(Vector(*rd(2), w, h), rd())), 50) for i in range(30)]

run = True
while run:
    clo.tick(120)

    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            run = not True

    for i in arr:
        i.draw(pd, 4, arrow=1)

    pd.upd()
    pd.fill()