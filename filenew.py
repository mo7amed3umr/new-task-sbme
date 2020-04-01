from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import time
name = 'ball_glut'

angle = 0.0
angle2 = 0.0
moving = 0
startx = 0
starty = 0

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_FLAT)

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glRotatef(angle2, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)

    glColor3f(1.0, 1.0, 0.0)

    glRotatef(-45, 0.0, 0.0, 1.0)


    glPushMatrix()
    #glRotatef(rotAngle, 0.0, 0.0, 0.1)
    glBegin(GL_LINES)
    glLineWidth(2.5)
    glVertex3f(0.0, -2.5, 0)
    glVertex3f(0.0, 2.5, 0)
    glEnd
    glPopMatrix()
    glPopMatrix()

    glPushMatrix()
    # color = [1.0, 0., 0., 1.]
    # glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
    glColor3f(1.0,1.0,0.0)

    glutSolidSphere(0.7, 20, 10)
    glPopMatrix()

    glPopMatrix()

    glFlush()

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



def main():
   glutInit(sys.argv)
   glutInitDisplayMode(0)
   glutInitWindowSize(500, 500)
   glutInitWindowPosition(400, 400)
   glutCreateWindow(name)

   init()
   glutMouseFunc(mouse)
   glutMotionFunc(motion)
   glutDisplayFunc(display)
   glutReshapeFunc(reshape)
   #glutKeyboardFunc(keyboard)
   glutMainLoop()

   return

if __name__ == '__main__':
    main()



