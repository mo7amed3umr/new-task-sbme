from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import time


name = 'ball_glut'
rotAngle =-90
def line():
    glPushMatrix()
    glBegin(GL_LINE)
    glLineWidth(2.5)
    glColor3f(0.7, 0.0, 1.0)

    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(100, 100, 100)
    glEnd
    glPopMatrix()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(0)
    glutInitWindowSize(400,400)
    glutCreateWindow(name)

    glClearColor(0.,0.,0.,1.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    lightZeroPosition = [10.,4.,10.,1.]
    lightZeroColor = [0.8,1.0,0.8,1.0] #green tinged
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
    glutDisplayFunc(display)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40.,1.,1.,40.)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0,0,10,
              0,0,0,
              0,1,0)
    glPushMatrix()
    rotate()
    glutMainLoop()
    return

def rotate():
    global rotAngle
    for i in range(9):
        rotAngle = rotAngle + 10
        time.sleep(1)

        display()


def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()

    glColor3f(1.0, 1.0, 0.0)

    glRotatef(rotAngle, 0.0, 0.0, 1.0)

    glLineWidth(2.5)
    glPushMatrix()
    #glRotatef(rotAngle, 0.0, 0.0, 0.1)
    glBegin(GL_LINES)
    glVertex3f(0.0, -1, 0)
    glVertex3f(0.0, 1, 0)
    glEnd()
    glPopMatrix()
    glPopMatrix()

    glPushMatrix()
    # color = [1.0, 0., 0., 1.]
    # glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
    glColor3f(1.0,1.0,0.0)

    glutWireSphere(0.3, 20, 20)
    glPopMatrix()





    glFlush()



if __name__ == '__main__':
    main()
