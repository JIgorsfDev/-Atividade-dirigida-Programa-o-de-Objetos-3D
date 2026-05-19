#fazer um sable de luz 

import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

r = 0
g = 0
b = 0

vertices = [ #teria de ser 2 retangulos colados um no outro
    (0, 0, 0),  # Vértice 0
    (1, 0, 0),  # Vértice 1
    (1, 1, 0),  # Vértice 2
    (0, 1, 0),  # Vértice 3
    (0, 0, 1),  # Vértice 4
    (1, 0, 1),  # Vértice 5
    (1, 1, 1),  # Vértice 6
    (0, 1, 1),
    (0, 0, 0),  # Vértice 0
    (1, 0, 0),  # Vértice 1
    (1, 1, 0),  # Vértice 2
    (0, 1, 0),  # Vértice 3
    (0, 0, 1),  # Vértice 4
    (1, 0, 1),  # Vértice 5
    (1, 1, 1),  # Vértice 6
    (0, 1, 1)
]

faces = [
    (0, 1, 2, 3),  # Face frontal
    (4, 5, 6, 7),  # Face traseira
    (0, 1, 5, 4),  # Face inferior
    (2, 3, 7, 6),  # Face superior
    (0, 3, 7, 4),  # Face esquerda
    (0, 1, 2, 3),  # Face frontal
    (4, 5, 6, 7),  # Face traseira
    (0, 1, 5, 4),  # Face inferior
    (2, 3, 7, 6),  # Face superior
]

def keyboard(key, x, y):
  if key == b'w':
     cam_top()
  elif key == b'a':
     cam_left()
  elif key == b'd':
     cam_right()
  elif key == b's':
     cam_init()

def cam_top():
   gl.glMatrixMode(gl.GL_PROJECTION)
   gl.glLoadIdentity()
   glu.gluPerspective(32, 1.0, 1.0, 20)
   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()
   glu.gluLookAt(0.0, 10.0, 2.0,
                 0.0, 0.0, 0.0,
                 0.0, 1.0, 0.0)

   glut.glutPostRedisplay()

def cam_left():
   gl.glMatrixMode(gl.GL_PROJECTION)
   gl.glLoadIdentity()
   glu.gluPerspective(32, 1.0, 1.0, 20)
   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()
   glu.gluLookAt(10.0, 0.0, 2.0,
                 0.0, 0.0, 0.0,
                 0.0, 1.0, 0.0)

   glut.glutPostRedisplay()

def cam_right():
   gl.glMatrixMode(gl.GL_PROJECTION)
   gl.glLoadIdentity()
   glu.gluPerspective(32, 1.0, 1.0, 20)
   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()
   glu.gluLookAt(-10.0, 0.0, 2.0,
                 0.0, 0.0, 0.0,
                 0.0, 1.0, 0.0)

   glut.glutPostRedisplay()

def cam_init():
   gl.glMatrixMode(gl.GL_PROJECTION)
   gl.glLoadIdentity()
   glu.gluPerspective(32, 1.0, 1.0, 20)
   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()
   glu.gluLookAt(0.0, -10.0, 2.0,
                 0.0, 0.0, 0.0,
                 0.0, 1.0, 0.0)

   glut.glutPostRedisplay()

option = int(input('Escolha uma cor para o sabre de luz:\n1 - Azul\n2 - Vermelho\n3 - Verde\n4 - Amarelo\n5 - Roxo\n6 - Laranja\n7 - Branco\n8 - Preto'))

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
     r = 0.2
     g = 0.2
     b = 0.2
  elif option == 8:
     r = 1
     g = 1
     b = 1

def draw_saber():
   gl.glColor3f(0.5, 0.5, 0.5)
   gl.glBegin(gl.GL_QUADS)
   for face in faces:
       for vertex in face:
           gl.glVertex3fv(vertices[vertex])

   gl.glEnd()
   
   gl.glColor3f(r, g, b)
   gl.glBegin(gl.GL_QUADS)
   for face in faces:
      for vertex in face:
         gl.glVertex3fv(vertices[vertex])

   gl.glEnd()

def draw():
   gl.glClearColor(1.0, 1.0, 1.0, 1.0)
   gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
   draw_saber()
   glut.glutSwapBuffers()


glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
glut.glutCreateWindow('O bloco de pedra de Koralon')
glut.glutReshapeWindow(500, 500)
gl.glEnable(gl.GL_DEPTH_TEST)
cam_init()
glut.glutDisplayFunc(draw)
glut.glutKeyboardFunc(keyboard)
glut.glutMainLoop()
