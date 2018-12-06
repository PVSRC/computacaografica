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

x = ( (0.6),(0.5),(0.3),(0.2) )
y = ( (0.7),(0.5),(0.2),(0.1) )
z = ( (-0.2),(0.6),(0.5),(-0.1) )

vertices2 = (
    (z[0], y[0], -x[0]),
    (z[1], y[1], -x[1]),
    (z[2], y[2], -x[2]),
    (z[3], y[3], -x[3]),
    (z[0], y[3], -x[0]),
    (z[1], y[3], -x[1]),
    )

linhas2 = (
    (0,1),
    (1,2),
    (2,3),
    (0,3),
    (0,4),
    (3,4),
    (4,5),
    (1,5),
    (2,5),
    )
    
faces2 = (
    (0,1,2,3),
    (3,4,5,2),
    (0,1,5,4),
    (0,3,4),
    (1,2,5),
    )


vertices = (
    ( 0.9,-0.9,-0.9),
    ( 0.9, 0.9,-0.9),
    (-0.9, 0.9,-0.9),
    (-0.9,-0.9,-0.9),
    ( 0.9,-0.9, 0.9),
    ( 0.9, 0.9, 0.9),
    (-0.9,-0.9, 0.9),
    (-0.9, 0.9, 0.9),
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

def desenha():
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

    #Epura
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

    #Plano A
    glBegin(GL_LINE_LOOP)
    i = 0    
    for ponto in y:
        glVertex2f(z[i], y[i])
        i = i+1
    glEnd();

    #Plano B
    glBegin(GL_LINE_LOOP)
    i = 0    
    for ponto in x:
        glVertex2f(z[i], -x[i])
        i = i+1
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

    #Epura
    glColor3fv((0,0.5,0))
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()

    #Plano A
    glBegin(GL_LINE_LOOP)
    i = 0    
    for ponto in y:
        glVertex3f(z[i], y[i], -0.9)
        i = i+1
    glEnd();

    #Plano B
    glBegin(GL_LINE_LOOP)
    i = 0    
    for ponto in y:
        glVertex3f(z[i], -0.9, -x[i])
        i = i+1
    glEnd();

    #3D
    glColor3fv((0.5,0,0))
    glBegin(GL_LINES)
    for linha in linhas2:
        for vertice in linha:
            glVertex3fv(vertices2[vertice])
    glEnd()


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

    glutDisplayFunc(desenha)
    
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
