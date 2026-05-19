#Nas ruínas do antigo sistema geométrico, repousa a lendária Pirâmide de Pentagar, uma construção sagrada composta por uma base pentagonal e cinco faces triangulares que se erguem rumo ao infinito.
#Sua missão é reconstruir esse objeto sem auxílio das formas automáticas da GLUT, utilizando apenas sua habilidade com vértices, polígonos e a lógica do espaço tridimensional.
#Modele uma pirâmide com base pentagonal em OpenGL puro (GL_POLYGON para a base e GL_TRIANGLES para as faces). Posicione manualmente os vértices da base e do vértice superior (ápice).
#Apresente a pirâmide sob três ângulos diferentes, simulando a observação de um arqueólogo em exploração: visão frontal, visão superior e visão lateral. A base pode estar sobre o plano XY, e o ápice se projetando ao longo do eixo Z.
  
import OpenGL.GL as gl
import OpenGL.GLUT as  glut
import OpenGL.GLU as glu

apice = [0.0, 0.0, 2.0]

triangles = [
  apice,
  [0.0, -1.0, 0.0],
  [1.0, -0.3, 0.0],

  apice,
  [1.0, -0.3, 0.0],
  [0.6, 1.0, 0.0],

  apice,
  [0.6, 1.0, 0.0],
  [-0.6, 1.0, 0.0],

  apice,
  [-0.6, 1.0, 0.0],
  [-1.0, -0.3, 0.0],

  apice,
  [-1.0, -0.3, 0.0],
  [0.0, -1.0, 0.0],
]

base = [
  [0.0, -1.0, 0.0],
  [1.0, -0.3, 0.0],
  [0.6, 1.0, 0.0],
  [-0.6, 1.0, 0.0],
  [-1.0, -0.3, 0.0]

]


def figure():
   gl.glColor3f(1.0, 1.0, 1.0)
   gl.glBegin(gl.GL_TRIANGLES)
   for triangle in triangles:
       gl.glVertex3fv(triangle)
    
   gl.glEnd()

   gl.glColor3f(1.0, 1.0, 1.0)
   gl.glBegin(gl.GL_POLYGON)
   for vertex in base:
       gl.glVertex3fv(vertex)
   gl.glEnd()

def draw():
   gl.glClearColor(0.0, 0.0, 0.0, 0.0)
   gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
   gl.glMatrixMode(gl.GL_PROJECTION)
   gl.glLoadIdentity()
   glu.gluPerspective(48, 1, 1, 10)
   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()
   glu.gluLookAt(0.0, -5.0, 2.0, 
                 0.0, 0.0, 0.0, 
                 0.0, 1.0, 0.0)
   figure()
   glut.glutSwapBuffers()

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
glut.glutCreateWindow('A Pirâmide de Pentagar')
glut.glutReshapeWindow(500, 500)
gl.glEnable(gl.GL_DEPTH_TEST)
glut.glutDisplayFunc(draw)
glut.glutMainLoop()

   
   
