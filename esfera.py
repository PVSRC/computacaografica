import math
import random
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

contador = 0.0

def polygonRevolucao():
	global contador
	r = 1.0
	c = 0
	
	def s(theta, phi):
		return( r*math.cos(theta)*math.cos(phi), r*math.sin(phi), r*math.cos(phi)*math.sin(theta))
	
	phi = -(math.pi)/2
	theta = 0
	aux = 0.1
	glColor3f(1.0,1.0,1.0);
	glBegin(GL_QUADS)
	while phi <= (math.pi/2):
		theta = 0.0
		while theta <= (math.pi * 2):
			glVertex3fv(s(theta, phi))
			glVertex3fv(s(theta+aux, phi))
			glVertex3fv(s(theta+aux, phi+aux))
			glVertex3fv(s(theta, phi+aux))
			theta += aux
		phi += aux

	glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,0,0,10)
    polygonRevolucao()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("ESFERA")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(90,1,0,0)
glutTimerFunc(50,timer,1)
glutMainLoop()



