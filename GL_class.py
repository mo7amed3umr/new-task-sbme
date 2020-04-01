import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt5.QtWidgets import QOpenGLWidget,QApplication
import pygame as pg
from pygame.locals import *

class pyqtopengl(QOpenGLWidget):
    cubeVertices = ((1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (-1, 1, 1), (-1, -1, -1), (-1, -1, 1), (-1, 1, -1))
    cubeEdges = ((0, 1), (0, 3), (0, 4), (1, 2), (1, 7), (2, 5), (2, 3), (3, 6), (4, 6), (4, 7), (5, 6), (5, 7))
    cubeQuads = ((0, 3, 6, 4), (2, 5, 6, 3), (1, 2, 5, 7), (1, 0, 4, 7), (7, 4, 6, 5), (2, 3, 0, 1))
    w = 0
    h = 0
    def __init__(self,parent= None):
        super().__init__(parent)
        self.paint0 = False
        self.paint1 = False
        self.paint2 = False
        self.paint3 = False
        self.paint4 = False

    def initializeGL(self):
        self.paint3 = True
        # glClearColor(1.0,0.0,1.0,0.0)
        # glClear(GL_COLOR_BUFFER_BIT)


    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-50,50,-50,50,-50,50)
        glViewport(0,0,w,h)

    def paintGL(self):
        if self.paint0:
            glColor3f(1.0,0.0,0.0)
            glRectf(-5,-5,5,5)
        if self.paint1:
            glColor3f(0.0,1.0,0.0)
            x = 10
            y = 10
            self.draw_loop(x,y)
        if self.paint2:
            glColor3f(0.0,0.0,1.0)
            x = 5
            y = 5
            self.draw_loop(x,y)

        if self.paint3:
            self.loadScene()
            glutWireSphere(5, 13, 13)

        if self.paint4:
            pg.init()
            display = (300, 400)
            # w = self.ui.openGLWidget.width()
            # h = self.ui.openGLWidget.height()
            display = (self.w, self.h)
            pg.display.set_mode(display, DOUBLEBUF | OPENGL)
            gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
            glTranslatef(0.0, 0.0, -10)
            glRotatef(1, 1, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.solidCube()
            #self.wireCube()
            pg.display.flip()
            pg.time.wait(10)

    def draw_loop(self,x,y,incr = 10):
        pass

    # def draw(self):
    #     glScalef(self.width, self.height, self.depth)
    #     glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    #     gluSphere(self.quad, 1.0, 12, 12)
    #     glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    def loadScene(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        x, y, width, height = glGetDoublev(GL_VIEWPORT)
        gluPerspective(
            45,  # field of view in degrees
            width / float(height or 1),  # aspect ratio
            .25,  # near clipping plane
            200,  # far clipping plane
        )

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        gluLookAt(12, 12, 12, 0, 0, 0, 0, 1, 0)

    def wireCube(self):
        glBegin(GL_LINES)
        for cubeEdge in self.cubeEdges:
            for cubeVertex in cubeEdge:
                glVertex3fv(self.cubeVertices[cubeVertex])
        glEnd()

    def solidCube(self):
        glBegin(GL_QUADS)
        for cubeQuad in self.cubeQuads:
            for cubeVertex in cubeQuad:
                glVertex3fv(self.cubeVertices[cubeVertex])
        glEnd()
