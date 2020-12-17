'''
Ce script extrait les donnees sur le coronavirus d'un fichier html (ou js)
trace l'evolution quotidienne du nombre de deces/reanimation/cas
G Vigé - 3/4/2020
'''

import numpy as np
import matplotlib.pyplot as plt
import json
import re

format = 2

if format==2:
    fich = open("index.js", "r")
    contenu = fich.read()
    fich.close()
    x = re.findall("JSON.parse\(\'\[\{\"casConfirmes(.*?)\'\)", contenu)
    s="[{\"casConfirmes" + x[0] #'[{"casConfirmes"
    #pas trouve un moyen propre de convertir l'UTF8
    s = s.replace("\\xe9", "é")
    s = s.replace("\\xce","I")
    s = s.replace("\\xf4","ô")
    s = s.replace("\\'","'")
    s = s.replace("\\xe8","è")
    liste = json.loads(s)
elif format==1:
    #ancien format (html)
    fich = open("a.html", "r")
    contenu = fich.read()
    fich.close()
    x = re.findall("\"data\":\[(.*?)\]", contenu) #x est une liste (a un element)
    s="["+x[0]+"]" #la chaine doit commencer et finir par des crochets
    liste = json.loads(s)
    
cas=[0]; deces=[0]; reanimation=[0]; hospitalises=[0]
for dic in liste:
    if dic["code"]=="FRA":
        if ('casConfirmes' in dic):
            cas=cas+[dic['casConfirmes']]
        else:
            cas=cas+[cas[-1]]
        if ('deces' in dic):
            deces=deces+[dic['deces']]
        else:
            deces=deces+[deces[-1]]
        if ('reanimation' in dic):
            reanimation=reanimation+[dic['reanimation']]
        else:
            reanimation=reanimation+[reanimation[-1]]
        if ('hospitalises' in dic):
            hospitalises=hospitalises+[dic['hospitalises']]
        else:
            hospitalises=hospitalises+[hospitalises[-1]]

#plt.plot(cas, label="casConfirmes")
#plt.plot(deces, label="deces")

#moyenne glissante
n=len(deces)
delta_rea = np.array(reanimation[1:])- np.array(reanimation[0:-1])
delta_deces = np.array(deces[1:])- np.array(deces[0:-1])
x=np.linspace(1,n-1,n-1)

plt.subplot(121)
plt.plot(x,reanimation[1:], 'p:',label="reanimation")
plt.legend()

plt.subplot(122)
plt.plot(x,delta_rea, 'b:',label="delta reanimation")
plt.plot(x,delta_deces,'r:', label="deces/jour")

def lissage(x,y,p):
    '''Fonction qui debruite une courbe par une moyenne glissante sur 2P+1 points'''
    xout=[]
    yout=[]
    xout = x[p: -p]
    for index in range(p, len(y)-p):
        average = np.mean(y[index-p : index+p+1])
        yout.append(average)
    #pour le point suivant la moyenne est faite sur le nb de pts dispo
    for j in range(1,p+1):
        average = np.mean(y[index-p+j : index+p+1])
        yout.append(average)
        xout = np.append(xout,x[-p+j-1])
    return xout,yout

x_lisse, y_lisse = lissage(x,delta_rea, 3)
plt.plot(x_lisse, y_lisse, 'b-',label="lissage")
x_lisse, y_lisse = lissage(x,delta_deces, 3)
plt.plot(x_lisse, y_lisse, 'r-',label="lissage")
plt.legend()
plt.show()
