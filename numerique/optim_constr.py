import numpy as np
from scipy.optimize import minimize
from scipy.optimize import Bounds
from scipy.optimize import LinearConstraint
from scipy.optimize import NonlinearConstraint
from scipy.optimize import BFGS
from scipy.optimize import SR1

bounds = Bounds([0, -0.5], [1.0, 2.0])
linear_constraint = LinearConstraint([[1, 2], [2, 1]], [-np.inf, 1], [1, 1])

def rosen(x):
    # The Rosenbrock function
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

def rosen_der(x):
    # gradient de la fonction objectif
    xm = x[1:-1]
    xm_m1 = x[:-2]
    xm_p1 = x[2:]
    der = np.zeros_like(x)
    der[1:-1] = 200*(xm-xm_m1**2) - 400*(xm_p1 - xm**2)*xm - 2*(1-xm)
    der[0] = -400*x[0]*(x[1]-x[0]**2) - 2*(1-x[0])
    der[-1] = 200*(x[-1]-x[-2]**2)
    return der

def cons_f(x):
    return [x[0]**2 + x[1], x[0]**2 - x[1]]

def cons_J(x):
    return [[2*x[0], 1], [2*x[0], -1]]

# on peut demander un calcul approché du hessien des constraintes (BFGS)
nonlinear_constraint = NonlinearConstraint(cons_f, -np.inf, 1, jac=cons_J, hess=BFGS())

x0 = np.array([0.5, 0])

# on peut demander une approximation (SR1) du hessien de l'objectif
res = minimize(rosen, x0, method='trust-constr', jac=rosen_der, hess=SR1(),
               constraints=[linear_constraint, nonlinear_constraint],
               options={'verbose': 1}, bounds=bounds)

print(res.x)