'''
Modèle épidémiologique SIR
https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology


ameliorations
- trace des courbes jusqu'à ce qu'elles soient stabilisées
- nb de morts
- test p=0.019, p=0.021
'''

import matplotlib.pyplot as plt

S=[]
I=[]
R=[]

pop=70000000

c=5        #nb contact par jour
p=0.022    #proba de transmission
d=10        #durée de la maladie
R0 = c*p*d
print("R0 = " + str(R0))

S.append(pop)
I.append(2000)
R.append(200)

n=0
cont = True
while cont:
    S.append(S[n]-I[n]*c*p*S[n]/pop)
    I.append(I[n]+I[n]*c*p*S[n]/pop-(I[n]/d))
    R.append(R[n]+I[n]/d)
    cont = abs(S[n+1]-S[n])>1
    n = n+1
    
plt.subplot(2,2,1)
plt.plot(range(len(S)),S)

plt.subplot(2,2,2)
plt.plot(range(len(I)),I,'r')

plt.subplot(2,2,3)
plt.plot(range(len(R)),R,'g')

plt.show()