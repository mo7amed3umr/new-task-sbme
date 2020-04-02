from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import time
import numpy as np
# import cv2
from tkinter import filedialog
import matplotlib.pyplot as plt
from PyQt5 import QtCore
from itertools import count
from math import *
from matplotlib.animation import FuncAnimation
import threading

name = 'ball_glut'
rotAngle = 0.0
angle = 0.0
angle2 = 0.0
moving = 0
startx = 0
starty = 0
index = count()
x_Mxy = np.array([])
y_Mxy = np.array([])
x_Mz = np.array([])
y_Mz = np.array([])
x = 0
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_FLAT)



def rt(fangle):
    global rotAngle
    rotAngle = fangle
    display()

def display():
    global rotAngle
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    # glClear(GL_COLOR_BUFFER_BIT)
    # glPushMatrix()
    glRotatef(angle2, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)



    glColor3f(1.0, 1.0, 0.0)
    glRotatef(rotAngle, 0.0, 0.0, 1.0)



    glPushMatrix()
    glBegin(GL_LINES)
    glLineWidth(2.5)
    glVertex3f(0.0, -0.4, 0)
    glVertex3f(0.0, 0.4, 0)
    glEnd
    glPopMatrix()



    glPushMatrix()
    glColor3f(1.0,1.0,0.0)

    glutWireSphere(0.1, 20, 10)
    glPopMatrix()

    glPopMatrix()

    glutSwapBuffers()
def reshape(  w ,   h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(85.0, w / h, 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5.0)

def mouse( button,  state,  x,  y):
    global startx,starty,moving
    if button == GLUT_LEFT_BUTTON :
        if state == GLUT_DOWN:
            moving = 1
            startx = x
            starty = y
        if state == GLUT_UP:
            moving = 0

def motion( x,  y):
    global angle,angle2,startx,starty
    if moving:
        angle = angle + (x - startx)
        angle2 = angle2 + (y - starty)
        startx = x
        starty = y
        glutPostRedisplay()


def rotate(flipAngle: 'float', Mo: 'float')-> np.ndarray:
    flipAngle = (flipAngle * 3.14) / 180
    xy =  Mo * np.sin(flipAngle)
    z = Mo * np.cos(flipAngle)
    return np.array([xy, z])

def relaxition(i, array, T2, T1, Mo):
    global x_Mxy, y_Mxy, x, x_Mz, y_Mz,rotAngle
    exp2 = array[0] * np.exp(-1 * np.arange(0, 5 * T2, 0.5) / T2)
    exp1 = (np.ones(len(exp2)) * Mo) - ((Mo - array[1]) * np.exp(-1 * np.arange(0, 5 * T1, 0.5) / T1))
    if x < len(exp1):
        x_Mz = np.append(x_Mz, next(index))
        y_Mz = np.append(y_Mz, exp1[x])
        x_Mxy = np.append(x_Mxy, next(index))
        y_Mxy = np.append(y_Mxy, exp2[x])
        flipAngle = (atan2(exp2[x], exp1[x]) * 180) / 3.14
        rotAngle =flipAngle
        display()




        plt.plot(x_Mxy, y_Mxy, label='Mxy')
        plt.plot(x_Mz, y_Mz, label='Mz')
        x = x + 1
    else:
        x_Mz = np.append(x_Mz, next(index))
        y_Mz = np.append(y_Mz, Mo)
        x_Mxy = np.append(x_Mxy, next(index))
        y_Mxy = np.append(y_Mxy, 0)
        plt.plot(x_Mxy, y_Mxy, label='Mxy')
        plt.plot(x_Mz, y_Mz, label='Mz')

def opengl():
    glutInit(sys.argv)
    glutInitDisplayMode(0)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(900, 500)
    glutCreateWindow(name)

    init()
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutDisplayFunc(display)

    glutReshapeFunc(reshape)
    # glutKeyboardFunc(keyboard)
    # rotateangle()
    display()
    plotting()
    # glutMainLoop()


def plotting():
    z = rotate(120, 5)
    ani = FuncAnimation(plt.gcf(), relaxition, fargs=(z, 3, 3, 5,), interval=1000)
    plt.show()
def main():
    opengl()
   # z = rotate(60, 5)
   # ani = FuncAnimation(plt.gcf(), relaxition, fargs=(z, 3, 3, 5,), interval=1000)
   # anix = FuncAnimation(plt.gcf(), opengl, interval=500)
   # plt.show()
   # mtplib()


if __name__ == '__main__':
    main()



