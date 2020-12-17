import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

# y est le modele, c'est une fonction qui prend en argument :
# theta qui est une liste de 3 parametres (a déterminer)
# t qui est un ndarray contenant la variable continue (discrétisée)
#
#               K
# y(t) = ------------------
#                -r(t-t0)
#          1 + e
#
def y(theta, t):
    return theta[0] / (1 + np.exp(- theta[1] * (t - theta[2])))

# Variable d'entree discretisee
ts = np.linspace(0, 1, 50)
# On crée des donnée à partir d'un vecteur theta=[K,r,t0]
# puis on ajoute un bruit aleatoire
K = 1; r = 10; t0 = 0.5; noise = 0.1
ys = y([K, r, t0], ts) + noise * np.random.rand(ts.shape[0])

# fun est l'écart entre le modele évalué en theta et les données
def fun(theta):
    return y(theta, ts) - ys

# valeurs initiales pour theta (au hasard)
theta0 = [1,2,3]
res1 = least_squares(fun, theta0)
print("Solution de moindres carrés:")
print(res1.x)


plt.plot(ts, ys, 'b.',label="donnees")
plt.plot(ts, y(res1.x,ts), 'r-',label="modele")
plt.legend()
plt.show()