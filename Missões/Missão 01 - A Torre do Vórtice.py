#Seu primeiro desafio como aprendiz no mundo 3D é materializar a Torre do Vórtice, uma estrutura em formato de cone, vista de três pontos cardeais distintos. 
#Você deve usar glutWireCone() para renderizar o cone. Altere a posição da câmera (ex: com gluLookAt) para visualizá-lo de três ângulos diferentes: frontal, lateral e superior. 
#Marque cada ângulo com uma cor diferente de fundo para distinguir as perspectivas.

import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
import math
import sys

def keyboard(key, x, y):
   if key == b's':
      cam_top()

   elif key == b'a':
      cam_sideLeft()

   elif key == b'd':
      cam_sideRight()

   elif key == b'w':
      cam_base()

   elif key == b'r':
      cam_reset()

def cam_top():
   gl.glClearColor(0.5, 0, 0, 1)
   gl.glMatrixMode(gl.GL_PROJECTION)
   gl.glLoadIdentity()
   glu.gluPerspective(32, 1.0, 1.0, 10)
   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()
   glu.gluLookAt(0.0, 5.0, 2.0,
                 0.0, 0.0, 0.0,
                 0.0, 1.0, 0.0)

   glut.glutPostRedisplay()

def cam_sideLeft():
   gl.glClearColor(0, 0.5, 0, 1)
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
   gl.glClearColor(0, 0, 0.5, 1)
   gl.glMatrixMode(gl.GL_PROJECTION)
   gl.glLoadIdentity()
   glu.gluPerspective(32, 1.0, 1.0, 10)
   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()
   glu.gluLookAt(-5.0, 0.0, 2.0,
                 0.0, 0.0, 0.0,
                 0.0, 1.0, 0.0)

   glut.glutPostRedisplay()

def cam_base():
   gl.glClearColor(1, 0.5, 0, 1)
   gl.glMatrixMode(gl.GL_PROJECTION)
   gl.glLoadIdentity()
   glu.gluPerspective(64, 1.0, 1.0, 10)
   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()
   glu.gluLookAt(0.0, 0.0, 2.0,
                 0.0, 0.0, 0.0,
                 0.0, 1.0, 0.0)

   glut.glutPostRedisplay()

def cam_reset(): 
   gl.glClearColor(0, 0, 0, 1)
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
   gl.glColor3f(1, 1, 1)
   glut.glutWireCone(1, 1, 25, 10)

def draw():
   gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
   cone()
   glut.glutSwapBuffers()

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
glut.glutCreateWindow("A torre do Vórtice")

gl.glEnable(gl.GL_DEPTH_TEST)

cam_reset()

glut.glutReshapeWindow(800, 800)
glut.glutDisplayFunc(draw)
glut.glutKeyboardFunc(keyboard)
glut.glutMainLoop()
