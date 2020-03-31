# import OpenGL.GL as gl
# import OpenGL.GLU as glu
# import OpenGL.GLUT as glut
# from PyQt5 import QtWidgets as qWidget
# from PyQt5 import QtGui as qGui
# from PyQt5 import QtCore as qCore
# from PyQt5 import uic
# import sys
# import os
#
#
# class mainWindow(qWidget.QMainWindow):
#     """Main window class."""
#
#     def __init__(self, *args):
#         """Init."""
#         super(mainWindow, self).__init__(*args)
#         ui = os.path.join(os.path.dirname(__file__), 'test.ui')
#         uic.loadUi(ui, self)
#
#     def setupUI(self):
#         print("\033[1;101m SETU6P UI \033[0m")
#         self.windowsHeight = self.openGLWidget.height()
#         self.windowsWidth = self.openGLWidget.width()
#
#         self.openGLWidget.initializeGL()
#         self.openGLWidget.resizeGL(self.windowsWidth, self.windowsHeight)
#         self.openGLWidget.paintGL = self.paintGL
#         self.openGLWidget.initializeGL = self.initializeGL
#
#     def paintGL(self):
#         self.loadScene()
#         glut.glutWireSphere(2, 13, 13)
#
#     def initializeGL(self):
#         print("\033[4;30;102m INITIALIZE GL \033[0m")
#         gl.glEnable(gl.GL_BLEND)
#         gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
#         gl.glEnable(gl.GL_DEPTH_TEST)
#
#     def loadScene(self):
#         gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
#         gl.glMatrixMode(gl.GL_PROJECTION)
#         gl.glLoadIdentity()
#         x, y, width, height = gl.glGetDoublev(gl.GL_VIEWPORT)
#         glu.gluPerspective(
#             45,  # field of view in degrees
#             width / float(height or 1),  # aspect ratio
#             .25,  # near clipping plane
#             200,  # far clipping plane
#         )
#
#         gl.glMatrixMode(gl.GL_MODELVIEW)
#         gl.glLoadIdentity()
#
#         glu.gluLookAt(12, 12, 12, 0, 0, 0, 0, 1, 0)
#
#
# app = qWidget.QApplication(sys.argv)
# window = mainWindow()
# window.setupUI()
# window.show()
# sys.exit(app.exec_())
import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

cubeVertices = ((1,1,1),(1,1,-1),(1,-1,-1),(1,-1,1),(-1,1,1),(-1,-1,-1),(-1,-1,1),(-1,1,-1))
cubeEdges = ((0,1),(0,3),(0,4),(1,2),(1,7),(2,5),(2,3),(3,6),(4,6),(4,7),(5,6),(5,7))
cubeQuads = ((0,3,6,4),(2,5,6,3),(1,2,5,7),(1,0,4,7),(7,4,6,5),(2,3,0,1))

def wireCube():
    glBegin(GL_LINES)
    for cubeEdge in cubeEdges:
        for cubeVertex in cubeEdge:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()

def solidCube():
    glBegin(GL_QUADS)
    for cubeQuad in cubeQuads:
        for cubeVertex in cubeQuad:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()

def main():
    pg.init()
    display = (300, 400)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -10)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        solidCube()
        #wireCube()
        pg.display.flip()
        pg.time.wait(10)

if __name__ == "__main__":
    main()