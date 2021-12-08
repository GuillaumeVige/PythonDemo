#Construct a 2000x2000 lil_matrix and add some values to it:

from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
from scipy.sparse.linalg import bicgstab
from numpy.linalg import solve, norm
from numpy.random import rand
from time import perf_counter
#from Tkinter import *           # Importing the Tkinter (tool box) library

#def compute():
#	lab= Label(root, text = 'You pressed the button')
#	lab.pack()

#root = Tk()                     # Create a background window
#root.geometry('200x110+350+70')
#radio1  = Radiobutton(root, text = 'Full')
#radio1.pack()
#button = Button(root, text = 'Compute', command = compute)
#button.pack()
#root.mainloop()

def print_iter(xk):
	err = A*xk-b
	print(norm(err))

A = lil_matrix((2000, 2000))
A[0, :200] = rand(200)
A[1, 100:300] = A[0, :200]
A.setdiag(rand(2000))

# Now convert it to CSR format and solve A x = b for x:

print('Resolution d un systeme lineaire 2000x2000 creux, methode directe :')
A = A.tocsr()
b = rand(2000)
t1 = perf_counter()
x = spsolve(A, b)
t2 = perf_counter()
print('cpu:',t2-t1)

#Convert it to a dense matrix and solve, and check that the result
# is the same:
print('Resolution d un systeme lineaire 2000x2000 dense :')

t1 = perf_counter()
x_ = solve(A.todense(), b)
t2 = perf_counter()
print('cpu:',t2-t1)

# Now we can compute norm of the error with:

err = norm(x-x_)
print ('error:',err)

# Use BIConjugate Gradient STABilized iteration to solve A x = b
print('Resolution d un systeme lineaire 2000x2000 par bicgstab:')
t1 = perf_counter()
#[x2, info] = bicgstab(A, b, None, 1e-8, None, None, None, print_iter)
[x2, info] = bicgstab(A, b, None, 1e-8)
t2 = perf_counter()
print('cpu:',t2-t1)

err2 = A*x2-b
print ('error:',norm(err2))


