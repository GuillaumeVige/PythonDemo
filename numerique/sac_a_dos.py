# PAS REUSSI A INSTALLER LE SOLVER (GLPK)
import cvxpy
# sous Linux echec de l'install avec : pip3 install cvxpy
#sous windows depuis pyzo echec avec : pip install cvxpy
'''
CVXPY is a Python-embedded modeling language for convex optimization problems. It automatically transforms the problem into standard form, calls a solver, and unpacks the results.
'''
import numpy as np

# The data for the Knapsack problem
# P is total weight capacity of sack
# weights and utilities are also specified
P = 165
weights = np.array([23, 31, 29, 44, 53, 38, 63, 85, 89, 82])
utilities = np.array([92, 57, 49, 68, 60, 43, 67, 84, 87, 72])

# The variable we are solving for
x = cvxpy.Variable(len(weights),boolean=True)

# The sum of the weights should be less than or equal to P
weight_constraint = weights @ x <= P

# Our total utility is the sum of the item utilities
objective = cvxpy.Maximize(utilities @ x)

# We tell cvxpy that we want to maximize total utility
# subject to weight_constraint. All constraints in
# cvxpy must be passed as a list
prob = cvxpy.Problem(objective, [weight_constraint])


# Solving the problem
#prob.solve(solver=cvxpy.GLPK_MI)
prob.solve(solver=cvxpy.ECOS_BB)

print("Status: ", prob.status)
print("The optimal value is", prob.value)
print("A solution x is")
print(x.value)