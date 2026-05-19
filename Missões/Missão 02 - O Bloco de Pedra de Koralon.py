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
    [-1, -1, 1],
    [-1, 1, 1]
             ]
faces = [
    [0, 1, 2, 3],
    [3, 2, 7, 6],
    [6, 7, 5, 4],
    [4, 5, 1, 0],
    [1, 5, 7, 2],
    [4, 0, 3, 6]
               ]

cor = [
    [1, 0.5, 0],   
    [1, 0, 0],     
    [1, 1, 1],     
    [1, 1, 0],     
    [0, 0, 1],     
    [0, 1, 0] 
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
    if key == b'GLUT_KEY_UP':
       cam_top()

    elif key == b'GLUT_KEY_DOWN':
       cam_down()

    elif key  == b'GLUT_KEY_LEFT':
       cam_left()

    elif key == b'GLUT_KEY_RIGHT':
       cam_right()


def cam_top(): #o topo tá errado
   gl.glMatrixMode(gl.GL_PROJECTION)
   gl.glLoadIdentity()
   glu.gluPerspective(32, 1.0, 1.0, 10)
   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()
   glu.gluLookAt(0.0, 5.0, 2.0,
                 0.0, 0.0, 0.0,
                 0.0, 1.0, 0.0)

   glut.glutPostRedisplay()

def cam_down():
   gl.glMatrixMode(gl.GL_PROJECTION)
   gl.glLoadIdentity()
   glu.gluPerspective(32, 1.0, 1.0, 10)
   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()
   glu.gluLookAt(0.0, -5.0, 2.0,
                 0.0, 0.0, 0.0,
                 0.0, 1.0, 0.0)

   glut.glutPostRedisplay()

def cam_left():
 gl.glMatrixMode(gl.GL_PROJECTION)
 gl.glLoadIdentity()
 glu.gluPerspective(32, 1.0, 1.0, 10)
 gl.glMatrixMode(gl.GL_MODELVIEW)
 gl.glLoadIdentity()
 glu.gluLookAt(5.0, 0.0, 2.0,
               0.0, 0.0, 0.0,
               0.0, 1.0, 0.0)

 glut.glutPostRedisplay()

def cam_right():
 gl.glMatrixMode(gl.GL_PROJECTION)
 gl.glLoadIdentity()
 glu.gluPerspective(32, 1.0, 1.0, 10)
 gl.glMatrixMode(gl.GL_MODELVIEW)
 gl.glLoadIdentity()
 glu.gluLookAt(-5.0, 0.0, 2.0,
               0.0, 0.0, 0.0,
               0.0, 1.0, 0.0)

 glut.glutPostRedisplay()
  
def cam_reset():
 gl.glMatrixMode(gl.GL_PROJECTION)
 gl.glLoadIdentity()
 glu.gluPerspective(32, 1.0, 1.0, 100)
 gl.glMatrixMode(gl.GL_MODELVIEW)
 gl.glLoadIdentity()
 glu.gluLookAt(0.0, -5.0, 2.0,
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



  
