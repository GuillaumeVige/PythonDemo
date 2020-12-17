# Resolution d'un systeme de 2 equations non lineaires a 2 inconnues
# Sous linux, lancer : python nlsove.py
        
from scipy import optimize
from numpy import array

def fun(x):
	return [x[0]  + 0.5 * (x[0] - x[1])**3 - 1.0,
	0.5 * (x[1] - x[0])**3 + x[1]]
        
def jac(x):
	return array([[1 + 1.5 * (x[0] - x[1])**2,
	-1.5 * (x[0] - x[1])**2],
	[-1.5 * (x[1] - x[0])**2,
	1 + 1.5 * (x[1] - x[0])**2]])
        
#        A solution can be obtained as follows.
        
sol = optimize.root(fun, [0, 0], jac=jac, method='hybr')
print(sol.x)
print(sol)

