#Um antigo artefato está enterrado nos arquivos da geometria tridimensional: o Bloco de Pedra de Koralon, um paralelepípedo sólido, esculpido manualmente nos primórdios do espaço cartesiano.
#Como Guardião Espacial, sua tarefa é reconstruí-lo sem recorrer às formas pré-fabricadas da GLUT. Cada vértice, cada face, deve ser definido com exatidão e clareza, como um escultor digital. 
#Modele um paralelepípedo 3D utilizando GL_QUADS ou GL_POLYGON, definindo manual e explicitamente cada face e coordenadas dos vértices.
#Utilize diferentes chamadas de câmera (com gluLookAt ou manipulação da glMatrixMode) para exibir o objeto sob pelo menos três ângulos de visualização distintos: frontal, lateral e inclinado.
#Mantenha o objeto fixo e alterne apenas a posição do observador (câmera). Você pode usar uma variável global para modificar os valores de posição da câmera usando as teclas especiais (UP, DOWN, LEFT e RIGHT).

import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

vertices = [
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, -1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1],
    [-1, -1, 1]
             ]

faces = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [3, 2, 6, 7],
    [0, 1, 5, 4],
    [1, 2, 6, 5],
    [0, 3, 7, 4]
               ]

cor = [
    [0, 1, 0],
    [1, 0.5, 0],
    [1, 0, 0],
    [1, 1, 0],
    [1, 1, 1],
    [0, 0, 1]
     ]

def keyboard_gamer (key, x, y):
    if key == b'w':
       cam_top()

    elif key == b's':
       cam_down()

    elif key  == b'a':
       cam_left()

    elif key == b'd':
       cam_right()

    elif key == b'r': 
       cam_reset()

def keyboard_common(key, x, y):
  if key == glut.GLUT_KEY_UP:
     cam_top()

  elif key == glut.GLUT_KEY_DOWN:
     cam_down()

  elif key == glut.GLUT_KEY_LEFT:
     cam_left()

  elif key == glut.GLUT_KEY_RIGHT:
     cam_right()


def cam_top():
   gl.glMatrixMode(gl.GL_PROJECTION)
   gl.glLoadIdentity()
   glu.gluPerspective(32, 1.0, 1.0, 20)
   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()
   glu.gluLookAt(0.0, 0.0, 10.0,
                 0.0, 0.0, 0.0,
                 0.0, 1.0, 0.0)

   glut.glutPostRedisplay()

def cam_down():
   gl.glMatrixMode(gl.GL_PROJECTION)
   gl.glLoadIdentity()
   glu.gluPerspective(32, 1.0, 1.0, 20)
   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()
   glu.gluLookAt(0.0, 0.0, -10.0,
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

def cam_reset():
 gl.glMatrixMode(gl.GL_PROJECTION)
 gl.glLoadIdentity()
 glu.gluPerspective(32, 1.0, 1.0, 20)
 gl.glMatrixMode(gl.GL_MODELVIEW)
 gl.glLoadIdentity()
 glu.gluLookAt(0.0, -10.0, 2.0,
               0.0, 0.0, 0.0,
               0.0, 1.0, 0.0)

 glut.glutPostRedisplay()

def cube():
   gl.glBegin(gl.GL_QUADS)

   for i in range(len(faces)):
       gl.glColor3fv(cor[i])

       for vertex in faces[i]:
           gl.glVertex3fv(vertices[vertex])

   gl.glEnd()

def draw():
    gl.glClearColor(0.0, 0.0, 0.0, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    cube()
    glut.glutSwapBuffers()

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
glut.glutCreateWindow('O bloco de pedra de Koralon')
glut.glutReshapeWindow(500, 500)
gl.glEnable(gl.GL_DEPTH_TEST)
cam_reset()
glut.glutDisplayFunc(draw)
glut.glutKeyboardFunc(keyboard_gamer)
glut.glutSpecialFunc(keyboard_common)
glut.glutMainLoop()

