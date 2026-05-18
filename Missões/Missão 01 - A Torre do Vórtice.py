import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
import random as rd
import math
import sys

r = 0
g = 0
b = 0

def keyboard(key, x, y):
   if key == b's':
      cor()
      cam_top()

   elif key == b'a':
      cor()
      cam_sideLeft()

   elif key == b'd':
      cor()
      cam_sideRight()

   elif key == b'w':
      cor()
      cam_front()

   elif key == b'r':
      cor()
      cam_padrao()

def cor():
  global r, g, b
  r = rd.random()
  g = rd.random()
  b = rd.random()

def cam_front():
   gl.glClearColor(r, g, b, 1)
   gl.glMatrixMode(gl.GL_PROJECTION)
   gl.glLoadIdentity()
   glu.gluPerspective(64, 1.0, 1.0, 10)
   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()
   glu.gluLookAt(0.0, 0.0, 2.0,
                 0.0, 0.0, 0.0,
                 0.0, 1.0, 0.0)

   glut.glutPostRedisplay()

def cam_sideLeft():
   gl.glClearColor(r, g, b, 1)
   gl.glMatrixMode(gl.GL_PROJECTION)
   gl.glLoadIdentity()
   glu.gluPerspective(32, 1.0, 1.0, 10)
   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()
   glu.gluLookAt(5.0, 0.0, 2.0,
                 0.0, 0.0, 0.0,
                 0.0, 1.0, 0.0)

   glut.glutPostRedisplay()

def cam_sideRight():
   gl.glClearColor(r, g, b, 1)
   gl.glMatrixMode(gl.GL_PROJECTION)
   gl.glLoadIdentity()
   glu.gluPerspective(32, 1.0, 1.0, 10)
   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()
   glu.gluLookAt(-5.0, 0.0, 2.0,
                 0.0, 0.0, 0.0,
                 0.0, 1.0, 0.0)

   glut.glutPostRedisplay()

def cam_top():
   gl.glClearColor(r, g, b, 1)
   gl.glMatrixMode(gl.GL_PROJECTION)
   gl.glLoadIdentity()
   glu.gluPerspective(32, 1.0, 1.0, 10)
   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()
   glu.gluLookAt(0.0, 5.0, 2.0,
                 0.0, 0.0, 0.0,
                 0.0, 1.0, 0.0)

   glut.glutPostRedisplay()

def cam_padrao(): 
   gl.glClearColor(r, g, b, 1)
   gl.glMatrixMode(gl.GL_PROJECTION)
   gl.glLoadIdentity()
   glu.gluPerspective(32, 1.0, 1.0, 100)
   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()
   glu.gluLookAt(0.0, -5.0, 2.0,
                 0.0, 0.0, 0.0,
                 0.0, 1.0, 0.0)

   glut.glutPostRedisplay()

def cone():
   gl.glColor3f(1 - r, 1 - g, 1 - b)
   glut.glutWireCone(1, 1, 25, 10)

def draw():
   gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
   cone()
   glut.glutSwapBuffers()

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
glut.glutCreateWindow("A torre do Vórtice")

gl.glEnable(gl.GL_DEPTH_TEST)

cam_front()

glut.glutReshapeWindow(800, 800)
glut.glutDisplayFunc(draw)
glut.glutKeyboardFunc(keyboard)
glut.glutMainLoop()
