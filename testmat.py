#!/usr/bin/python3

import numpy as np #np est un alias pour numpy
import matplotlib.pyplot as plt

#z=np.linalg.inv(a);

def plotTriangle(x,y,z):
    plt.axis('equal')
    plt.plot([x[0],y[0]],[x[1],y[1]],'k-')
    plt.plot([x[0],z[0]],[x[1],z[1]],'k-')
    plt.plot([y[0],z[0]],[y[1],z[1]],'k-')
    plt.plot(x[0],x[1],'bo')
    plt.plot(y[0],y[1],'ro')
    plt.plot(z[0],z[1],'go')

mat = np.random.rand(2,2)
mat = 2*mat-1
mat=np.array([[0,1],[-1,0]])
lamb,vecp = np.linalg.eig(mat)
print(lamb)

x = np.array([[1,2]]).T
y = np.array([[-2,1]]).T
z = np.array([[2,-2]]).T
plotTriangle(x,y,z)
u = np.dot(mat, x)
v = np.dot(mat, y)
w = np.dot(mat, z)
#plotTriangle(u,v,w)

# plt.arrow(0, 0, vecp[0,0], vecp[0,1],head_width=0.05, head_length=0.1, fc='k', ec='k')
# plt.arrow(0, 0, vecp[1,0], vecp[1,1],head_width=0.05, head_length=0.1, fc='k', ec='k')

plt.title("valeurs propres : " + str(round(lamb[0],2)) + ", " + str(round(lamb[1],2)))


fig = plt.figure(1)
#on part de la matrice identité et on va jusqu'à une matrice de rotation par petits incréments
a=np.eye(2);

b=np.array([[1,0],[0,-1]]) #symétrie par rapport à y=0
b=np.array([[-1,0],[0,-1]]) #symétrie par rapport au point 0 (=rotation de pi)
b=np.array([[0,1],[1,0]]) #symétrie par rapport à y=x
b=np.array([[1,0],[0,2]]) #homothétie
b=np.array([[0,1],[-1,0]]) #rotation pi/2
b = np.random.rand(2,2)
b = 2*b-1
b=np.array([[1,1],[0,1]]) #matrice non diagonalisable
n=20
print("\nDebut boucle")
for i in range(0,n+1):
    mat = a+(b-a)*(i/n)
    lamb,vecp = np.linalg.eig(mat)
    print(vecp)
    u = np.dot(mat, x)
    v = np.dot(mat, y)
    w = np.dot(mat, z)
    plotTriangle(u,v,w)
    plt.title("valeurs propres : " + str(round(lamb[0],2)) + ", " + str(round(lamb[1],2)))
    plt.pause(1) # pause avec duree en secondes
    plt.show()
'''
mat=np.eye(2)
for i in range(0,15):
    mat = np.dot(mat,b)
    lamb,vecp = np.linalg.eig(mat)
    u = np.dot(mat, x)
    v = np.dot(mat, y)
    w = np.dot(mat, z)
    plotTriangle(u,v,w)
    plt.title("valeurs propres : " + str(round(lamb[0],2)) + ", " + str(round(lamb[1],2)))
    plt.pause(1) # pause avec duree en secondes
    plt.show()
'''