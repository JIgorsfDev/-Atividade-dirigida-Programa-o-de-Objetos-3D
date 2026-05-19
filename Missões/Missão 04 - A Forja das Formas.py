#Guardião, sua jornada está prestes a alcançar seu auge! Nas profundezas da Forja das Formas, um espaço onde a imaginação se torna vértice e a criatividade é
#fundida em polígonos, você deverá criar um objeto tridimensional original. Ele não pode ser encontrado nos registros da GLUT — ele deve nascer do seu raciocínio, da sua abstração, da sua visão.
#Escolha um objeto 3D qualquer, real ou fictício (ex: uma nave, um obelisco, um robô minimalista, um monólito, etc.).
#Modele-o manualmente, utilizando estruturas de dados adequadas para armazenar os vértices, faces e cores do objeto (pode ser a mesma dos exercícios anteriores ao OpenGL, o de “estrutura de dados em CG”).
#Exiba o objeto sob múltiplos ângulos de visualização, utilizando diferentes configurações de câmera (sempre mantenha o objeto fixo e movimente apenas a câmera).
#Programe de forma modular: separe a estrutura do objeto da lógica de visualização.

import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
import random

r = 0
g = 0
b = 0

vertices = [
    (-0.2, -2.0, -0.2),
    (0.2, -2.0, -0.2),
    (0.2, -1.0, -0.2),
    (-0.2, -1.0, -0.2),
    (-0.2, -2.0, 0.2),
    (0.2, -2.0, 0.2),
    (0.2, -1.0, 0.2),
    (-0.2, -1.0, 0.2),

    (-0.08, -1.0, -0.08),
    (0.08, -1.0, -0.08),
    (0.08, 2.5, -0.08),
    (-0.08, 2.5, -0.08),
    (-0.08, -1.0, 0.08),
    (0.08, -1.0, 0.08),
    (0.08, 2.5, 0.08),
    (-0.08, 2.5, 0.08)
]

faces = [
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (0, 1, 5, 4),
    (2, 3, 7, 6),
    (0, 3, 7, 4),
    (1, 2, 6, 5),

    (8, 9, 10, 11),
    (12, 13, 14, 15),
    (8, 9, 13, 12),
    (10, 11, 15, 14),
    (8, 11, 15, 12),
    (9, 10, 14, 13)
]

def keyboard(key, x, y):
  if key == b'w':
     cam_top()

  elif key == b'a' or key == b'd':
     cam_side()

  elif key == b's':
     cam_init()

def cam_top():
   gl.glMatrixMode(gl.GL_PROJECTION)
   gl.glLoadIdentity()
   glu.gluPerspective(32, 1.0, 1.0, 30)

   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()

   glu.gluLookAt(0.0, 12.0, 0.0,
                 0.0, 0.0, 0.0,
                 0.0, 0.0, -1.0)

   glut.glutPostRedisplay()

def cam_side():
   gl.glMatrixMode(gl.GL_PROJECTION)
   gl.glLoadIdentity()
   glu.gluPerspective(32, 1.0, 1.0, 20)

   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()

   glu.gluLookAt(10.0, 0.0, 1.5,
                 0.0, 0.0, 0.0,
                 0.0, 1.0, 0.0)

   glut.glutPostRedisplay()

def cam_init():
   gl.glMatrixMode(gl.GL_PROJECTION)
   gl.glLoadIdentity()
   glu.gluPerspective(32, 1.0, 1.0, 20)

   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()

   glu.gluLookAt(0.0, 0.0, 10.0,
                 0.0, 0.0, 0.0,
                 0.0, 1.0, 0.0)

   glut.glutPostRedisplay()

option = random.randint(1, 8)

def color_saber(option):
  global r, g, b

  if option == 1:
     r = 0
     g = 0
     b = 1

  elif option == 2:
     r = 1
     g = 0
     b = 0

  elif option == 3:
     r = 0
     g = 1
     b = 0

  elif option == 4:
     r = 1
     g = 1
     b = 0

  elif option == 5:
     r = 0.5
     g = 0
     b = 0.5

  elif option == 6:
     r = 1
     g = 0.647
     b = 0

  elif option == 7:
     r = 1
     g = 1
     b = 1

  elif option == 8:
     r = 0.2
     g = 0.2
     b = 0.2

color_saber(option)

def draw_saber():
   gl.glColor3f(0.5, 0.5, 0.5)

   gl.glBegin(gl.GL_QUADS)

   for face in faces[:6]:
       for vertex in face:
           gl.glVertex3fv(vertices[vertex])

   gl.glEnd()

   gl.glColor3f(r, g, b)

   gl.glBegin(gl.GL_QUADS)

   for face in faces[6:]:
      for vertex in face:
         gl.glVertex3fv(vertices[vertex])

   gl.glEnd()

def draw():
   gl.glClearColor(0.0, 0.0, 0.0, 1.0)
   gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

   draw_saber()

   glut.glutSwapBuffers()

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
glut.glutCreateWindow('A Forja das Formas')
glut.glutReshapeWindow(500, 500)

gl.glEnable(gl.GL_DEPTH_TEST)

cam_init()

glut.glutDisplayFunc(draw)
glut.glutKeyboardFunc(keyboard)

glut.glutMainLoop()
