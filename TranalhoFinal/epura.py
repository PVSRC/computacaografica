from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# Number of the glut window.
window = 0

# Rotations for cube. 
xrot = yrot = zrot = 0.0
dx = 0.0
dy = 0.0
dz = 0.0
width = 640
height = 480

X = 0.5
Y = 0.7
Z = 0.4

"""
    (0,1),
    (0,3),
    (2,1),
    (2,3),
    (4,6),
    (4,5),
    (7,5),
    (6,7),

    (4,5,6,7)
"""

vertices = (
    ( 1,-1,-1),
    ( 1, 1,-1),
    (-1, 1,-1),
    (-1,-1,-1),
    ( 1,-1, 1),
    ( 1, 1, 1),
    (-1,-1, 1),
    (-1, 1, 1),
    )

linhas = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (6,3),
    (6,4),
    )

faces = (
    (0,1,2,3),
    (0,4,6,3)
    )

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def desenha2():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    w = 3*width/4
    glViewport(0,0,w,height)
    desenha3D()
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    glViewport(w,0,width-w,height)
    desenha2D()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()
    glutSwapBuffers()

    
def desenha2D():
    glBegin(GL_LINES)
    glColor3f(1.0,1.0,0.0)

    glVertex2f(-0.9,0.0)
    glVertex2f(0.9,0.0)

    glVertex2f(0.9,-0.9)
    glVertex2f(0.9,0.9)

    glVertex2f(-0.9,0.9)
    glVertex2f(0.9,0.9)

    glVertex2f(-0.9,-0.9)
    glVertex2f(-0.9,0.9)

    glVertex2f(-0.9,-0.9)
    glVertex2f(0.9,-0.9)

    glEnd();

    glBegin(GL_POINTS)

    glVertex2f(Z, Y)
    glVertex2f(Z, -X)

    glEnd();

def InitGL(Width, Height):             
    glClearColor(0.0, 0.0, 0.0, 0.0)    
    glClearDepth(1.0)                  
    glDepthFunc(GL_LESS)               
    glEnable(GL_DEPTH_TEST)            
    glShadeModel(GL_SMOOTH)            
    ReSizeGLScene(Width, Height)    


def ReSizeGLScene(newWidth, newHeight):
    global width, height
    if newHeight == 0:                        
        newHeight = 1
    width = newWidth
    height = newHeight
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(newWidth)/float(newHeight), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def desenha3D():
    global xrot, yrot, zrot, texture

#    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()                   

    glClearColor(0.0,0.0,0.0,0.0)            
    
    glTranslatef(0.0,0.0,-5.0)            

    glRotatef(xrot,1.0,0.0,0.0)          
    glRotatef(yrot,0.0,1.0,0.0)           
    glRotatef(zrot,0.0,0.0,1.0)

    glBegin(GL_QUADS)
    i = 0
    for face in faces:
        glColor3fv(cores[i])
        for vertex in face:
            glColor3fv(cores[vertex])
            #glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

    glColor3fv((0,0.5,0))
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()
#    glutSwapBuffers()

    glBegin(GL_POINTS)

    #Plano A
    glVertex3f(X, Y, -1)

    #Plano B
    glVertex3f(X, -1, Z)

    glVertex3f(X, Y, Z)

    glEnd();


def keyPressed(tecla, x, y):
    global dx, dy, dz
    if tecla == ESCAPE:
        glutLeaveMainLoop()
    elif tecla == 'x' or tecla == 'X':
        dx = 1.0
        dy = 0
        dz = 0   
    elif tecla == 'y' or tecla == 'Y':
        dx = 0
        dy = 1.0
        dz = 0   
    elif tecla == 'z' or tecla == 'Z':
        dx = 0
        dy = 0
        dz = 1.0

def teclaEspecialPressionada(tecla, x, y):
    global xrot, yrot, zrot, dx, dy, dz
    if tecla == GLUT_KEY_LEFT:
        print "ESQUERDA"
        xrot -= dx                # X rotation
        yrot -= dy                 # Y rotation
        zrot -= dz                     
    elif tecla == GLUT_KEY_RIGHT:
        print "DIREITA"
        xrot += dx                # X rotation
        yrot += dy                 # Y rotation
        zrot += dz                     
    elif tecla == GLUT_KEY_UP:
        print "CIMA"
    elif tecla == GLUT_KEY_DOWN:
        print "BAIXO"


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def main():
    global window
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    
    # get a 640 x 480 window 
    glutInitWindowSize(width, height)
    
    # the window starts at the upper left corner of the screen 
    glutInitWindowPosition(0, 0)
    
    window = glutCreateWindow("Textura")

    glutDisplayFunc(desenha2)
    
    # When we are doing nothing, redraw the scene.
    glutTimerFunc(50,timer,1)
    
    # Register the function called when our window is resized.
    glutReshapeFunc(ReSizeGLScene)
    
    # Register the function called when the keyboard is pressed.  
    glutKeyboardFunc(keyPressed)

    glutSpecialFunc(teclaEspecialPressionada)

    # Initialize our window. 
    InitGL(640, 480)

    # Start Event Processing Engine    
    glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
    print "Hit ESC key to quit."
    main()
