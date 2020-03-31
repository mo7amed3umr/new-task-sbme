from PyQt5 import QtWidgets,QtCore,QtGui
from gl import Ui_MainWindow
import sys
from GL_class import *
import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


class ApplicationWindow(QtWidgets.QMainWindow):
#     cubeVertices = ((1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (-1, 1, 1), (-1, -1, -1), (-1, -1, 1), (-1, 1, -1))
#     cubeEdges = ((0, 1), (0, 3), (0, 4), (1, 2), (1, 7), (2, 5), (2, 3), (3, 6), (4, 6), (4, 7), (5, 6), (5, 7))
#     cubeQuads = ((0, 3, 6, 4), (2, 5, 6, 3), (1, 2, 5, 7), (1, 0, 4, 7), (7, 4, 6, 5), (2, 3, 0, 1))
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.openGLWidget.initializeGL()
        # self.ui.openGLWidget.
        # w = self.ui.openGLWidget.width()
        # h = self.ui.openGLWidget.height()

        gl_object = pyqtopengl(parent= self.ui.openGLWidget)
        gl_object.w = self.ui.openGLWidget.width()
        gl_object.h = h = self.ui.openGLWidget.height()
        # gl_object.paint4 = True
        # gl_object.loadScene()
        #
        # gl_object.setMinimumSize(300,300)
        # self.ui.openGLWidget.initializeGL()

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

    def Pgame(self):
        pg.init()
        # display = (1680, 1050)
        w = self.ui.openGLWidget.width()
        h = self.ui.openGLWidget.height()
        display = (w,h)
        pg.display.set_mode(display, DOUBLEBUF | OPENGL)

        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

        glTranslatef(0.0, 0.0, -5)

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            glRotatef(1, 1, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.solidCube()
            # wireCube()
            pg.display.flip()
            pg.time.wait(10)



def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
