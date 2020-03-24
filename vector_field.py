import numpy as np
#from math import sin, cos, pi, tau, atan2
import pygame
from pygame.locals import *
from pygame_draw import pyg_draw, mou_pos
from time import time as ti
from vector import *

Vec = Vector

def prop(max1, max2, val1):
    val2 = max2*val1/max1
    return val2

def pt_rot(arr, pts, func):
    global cols, rows
    a=0
    for obb, i in zip(arr, rows):
        for ob, j in zip(obb, cols):
            a += 1
            func(ob, i, j, pts)

def trans2(ob, i, j, pts):
    vcs = [B_diopole(i, j, pt) for pt in pts]
    vcs[0].rotate(pi)
    bv = vec_sum(vcs)
    set_ang(ob, bv.ang())
    #set_mag(ob, bv.mag()*10**6.25)

def trans(ob, i, j, pts):
    bv = B_poles(i, j, pts)
    set_ang(ob, bv.ang())
    #set_mag(ob, bv.mag()*10**6.25)

def B_diopole(i, j, pt):
    v = Vector(i-pt[1], j-pt[0])
    r = v.mag()
    theta = angy(v)
    phi = 0
    B = diopole(theta, phi, r) 
    return Vector(B[0], B[-1])

'''
def B_poles(i, j, pt):
    pt1, pt2 = pt
    v1 = Vector(i-pt1[1], j-pt1[0], *pt2)
    v2 = Vector(i-pt2[1], j-pt2[0], 500, 400)
    v = Vector(i ,j, y1=600)
    v1.rotate(-pi*0.5)
    v1.draw(pd, 1, arrow=1)#, rat=0.4, mul=0.3)
    pd.circ(pt1)
    pd.circ(pt2)
    #v2.draw(pd, 1, arrow=1)#, rat=0.4, mul=0.3)
    r1 = v1.mag()
    r2 = v2.mag()
    B = pole(r1, r2) 
    return Vector(0, 0)#B[0], B[-1])'''

def B_poles(i, j, pt):
    p = (j, i)
    pt1 = pt[0]
    pt2 = pt[1]
    cen = (np.array(pt1)+np.array(pt2))/2

    r = [p, cen]
    r1 = [p, pt1]
    r2 = [p, pt2]

    rv = Vec(*to_pt(r)).mag()
    r1v = Vec(*to_pt(r1)).mag()
    r2v = Vec(*to_pt(r2)).mag()

    l = [pt1, pt2]
    lx = [(pt1[0], pt2[1]), pt2]
    ly = [(pt1[0], pt2[1]), pt1]

    x = [cen, (p[0], cen[1])]
    x1 = [pt1, (p[0], pt1[1])]
    x2 = [pt2, (p[0], pt2[1])]

    # x1 > x > x2

    xv = Vec(*to_pt(x)).mag()
    x1v = Vec(*to_pt(x1)).mag()
    x2v = Vec(*to_pt(x2)).mag()

    y = [cen, (cen[0], p[1])]
    y1 = [pt1, (pt1[0], p[1])]
    y2 = [pt2, (pt2[0], p[1])]

    # y1 > y > y2

    yv = Vec(*to_pt(y)).mag()
    y1v = Vec(*to_pt(y1)).mag()
    y2v = Vec(*to_pt(y2)).mag()

    '''
    pd.circ(p, 3)
    pd.line(*r1, col="purple")
    pd.line(*r2, col="lblue")
    pd.line(*r, col="yellow", wid=3)
    pd.line(*l, col="green", wid=5)
    pd.line(*lx, col="green", wid=5)
    pd.line(*ly, col="green", wid=5)

    pd.line(*x, col="red", wid=5)
    pd.line(*x1, col="red", wid=5)
    pd.line(*x2, col="red", wid=5)

    pd.line(*y, col="red", wid=5)
    pd.line(*y1, col="red", wid=5)
    pd.line(*y2, col="red", wid=5)
    '''

    B = pole(r1v, r2v, x1v, x2v, y1v, y2v, 10**-3)

    ve = Vec(*B)
    
    #ve.draw(pd, 1, arrow=1)

    print(ve.ang())

    return ve

def to_pt(l):
    return *l[0], *l[1]

def diopole(theta, phi, r, mu=1):
    xh = np.array([1, 0, 0])
    yh = np.array([0, 1, 0])
    zh = np.array([0, 0, 1])
    vec = (sin(theta)*cos(theta)*(cos(phi)*xh + sin(phi)*yh)
           + (cos(theta)**2 - 1/3)*zh)
    return 3*mu/r**3 * vec

def pole(r1, r2, x1, x2, y1, y2, b=1):
    xh = np.array([1, 0])
    yh = np.array([0, 1])
    vec = (Baxis(r1, r2, x1, x2, b, -b)*xh
           + Baxis(r1, r2, y1, y2, b, -b)*yh)
    return vec

def Baxis(r1, r2, dist1, dist2, b1=1, b2=-1):
    return (b1*dist1/r1**3
            + b2*dist2/r2**3)

pd = pyg_draw(0.75)
w, h = pd.cen()
clo = pd.clock

def rd(num=1):
    return tau*np.random.random_sample((num))-pi

sc = 2#1/16
row, col = int(sc*801*0.01)+1, int(sc*1540*0.01)+1 # heigth, width
print(f"{row=}, {col=}")

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

pts = [(w+1, h-1), (w-1, h+1)]

pt_rot(arr, pts, trans2)

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
            pass

    pd.upd()
    pd.fill()