# -*- coding: cp1252 -*-

#ouvrir une console et taper : python Gauss.py
#depuis l'interpreteur, taper : import Gauss


# Ce programme resout un système d'equations Ax=b, par la methode de Gauss-Seidel

from math import*

print ("Resolution du système d\'equations par la methode Gauss-Seidel")

A=[[4,1,-1],[2,7,1],[1,-3,12]]
# A est la matrice du système définie ligne par ligne
b=[3,19,31]              
x=[0,0, 0]
#  x est le vecteur initial
tol=1e-16
# tol = précision 
itmax=100
# itmax est le nombre d'itération maximal
for k in range (itmax):
      for i in range(len(A)):
            s=b[i]
            for j in range(len(A)):
                  if i!=j:
                        s=s-A[i][j]*x[j]
            x[i]=float(s)/float(A[i][i])
      err=b[:]
#En Python modifier une donnee d’une extraction d’un tableau entraîne aussi une modification du tableau initial
#on ne peut pas faire err=b
      for i in range(len(A)):
            for j in range(len(A)):
                err[i]=err[i]-A[i][j]*x[j]
      errtot=0
      for i in range(len(A)):
            errtot=errtot+err[i]*err[i]
      errtot=sqrt(errtot)     
      print ('iter:',k,'  err:',errtot)
      if errtot<tol:
            print('Nombre d\'iterations',k,'Erreur',float(errtot))
            print (" la solution du systeme est:",x)
            break
else:
      print ("Gauss-Seidel ne converge pas")