# Le but de cet exemple est de faire une optimisation sur un système dynamique
#
# Un canon tire un boulet.
# Trouver l'angle de tir tel que le boulet atteigne une cible.
# On peut résoudre analytiquement ce problème mais la méthode ici consiste à ne pas le faire.
#
# Il ne s'agit pas de conrole optimal car il n'y a pas de commande

# Je bloque car le temps final n'est pas connu. Il faut choisir un autre pb.
#
# Guillaume Vigé 19/11/2020

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def rosen(x):
    """The Rosenbrock function"""
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res = minimize(rosen, x0, method='nelder-mead',
               options={'xatol': 1e-8, 'disp': True})

print(res.x)

def simul():
# integration de l'equa diff par une methode d'Euler explicite
    g = 8.81 # m/s2
    v0 = 100 # m/s
    alpha = np.pi/4 # radians
    z0=np.array([0, v0*np.cos(alpha), 0, v0*np.sin(alpha)]) #conditions initiales
    z=z0
    dt = 0.1
    traj=z0
    while z[2]>=0:
        dz = np.array([z[1], 0, z[3], -9.81])
        z=z+dt*dz
        traj = np.vstack((traj, z))

    plt.plot(traj[:,0], traj[:,2])
    plt.show()

simul()


