#!/usr/bin/python3

'''
A faire:
 - generer un executable
 - regex
 - effacer les fichiers temporaires *.o ...
 - faire un prg avec tkinter
 - generer ce fichier sous forme de html
 - logging
 - autre site meteo
'''
import os
import platform

if platform.system()=='Linux':
    os.chdir("/media/guillaume/ESD-ISO/Perso/python/")
else:
    os.chdir("E:\Programmation\python")

class Parag:
    def __init__(self): # Notre methode constructeur
        self.num = [0,0,0]
    def new(self,level,titre):
        print("") #print ajoute automatiquement un retour a la ligne
        self.num = self.num[:level-1]+[self.num[level-1]+1]+[0] * (len(self.num)-level)
        s = ".".join(list(map(str, self.num[:level])))
        print(s+". "+titre)
        if level==1:
            print("====================================================================")

parag=Parag()

#----------------------------------------------------------------------------------
parag.new(1,"Introduction")
print("On peut lancer un programme python depuis une console avec 'python prog_name.py' (ou 'python3 prog_name.py')")
print("Pour les commentaires on utilise '#'")
import sys
print ("Version courante : "+sys.version)

parag.new(2,"Mode interactif")
print("On peut egalement entrer en mode interactif en tapant \"python\"")
print("Pour lancer un script 'demo.py', taper 'import demo.py'")
print("Pour lancer une fonction 'fib' contenue dans un fichier 'fibo.py', taper:")
print("   'from fibo import fib'")
print("   fib(500)")

parag.new(2,"Import")
print("Pour importer un module : import nom_module")
print("Pour importer une fonction d'un module : from module import nom_fonction")
print("Importer un sous-module 1ere methode : from urllib import request")
print("   Acces direct : mine = request()")
print("Importer un sous-module 2eme methode : import urllib.request")
print("   Acces via le module : urllib.request()")

parag.new(2,"Linux")
parag.new(3,"Version")
print("Par defaut Ubuntu contient 2 versions de Python (2 et 3) ")
print("Commande pour lancer la version 2: 'python'. Version: 'python -V'")
print("Commande pour lancer la version 3: 'python3'. Version: 'python3 -V'")

parag.new(3,"IDE")
print("J'ai essaye Eric. Mais pas trouve comment utiliser numpy (No module named 'numpy')")
print("Pyzo fonctionne nickel")

parag.new(3, "Ligne de shebang")
print("#!/usr/bin/python3 est une ligne de shebang.")
print("Une ligne de shebang definit ou se trouve l\'interpreteur.")
print("Dans ce cas, l\'interpreteur python3 se trouve dans /usr/bin/python3.")
print("Une ligne shebang peut egalement etre un interpreteur bash, ruby, perl")
print("ou tout autre langage de script, par exemple: #!/Bin/bash.")
print("Sans la ligne shebang, le systeme d\'exploitation ne sait pas qu\'il s\'agit")
print("d\'un script python, meme si vous definissez le flag d\'execution sur le script")
print("et l\'executez comme ./script.py.")
print("Pour que le script s'execute par defaut dans python3, appelez-le en tant que python3 script.py ou definissez la ligne shebang.")

parag.new(3,"Installer un package sous linux")
print("python2:")
print("   sudo apt install python-pip")
print("   pip install numpy")
print("   pip install scipy")
print("python3:")
print("   J\'ai des soucis avec pip, utiliser plutot:")
print("   sudo apt-get install python3-numpy")
print("   sudo apt-get install python3-matplotlib")
print("   sudo apt-get install python3-scipy")

parag.new(2,"Windows")
parag.new(3,"Installation")
print("Aller sur le site : https://www.python.org/")
#Attention: dans la version 32 bits, l'antivirus CEA bug sur la lib numpy
print("Telecharger python pour windows (via installeur web, ne necessite pas de droit admin)")
print("Lancer l\'exe en configurant le dossier E:\Apps\Python38")
print("Installer des packages: ")
print("python -m pip install numpy")
print("python -m pip install matplotlib")
print("python -m pip install pytest")

parag.new(3,"Les IDE")
print("PyCharm est tres complet mais tres lourd (700Mo) et complexe a utiliser")
print("pyzo est parfait: leger et facile. Se veut une alternative a Matlab")
print("J'ai utilise Spyder au cours du projet Persee. Bien.")

#----------------------------------------------------------------------------------
parag.new(1,"Types de donnees")

parag.new(2,"Chaines de caracteres")

parag.new(3,"Manipulations de base")
word = 'Py'+'thon'
print("Concatener 2 chaines avec +  --> " + word)
print("Premier caractere : word[0]   --> " + word[0])
print("Dernier caractere : word[-1] --> " + word[-1])
print("Caracteres 2 a 4 : word[1:3] --> " + word[1:3])
print("Caracteres a partir du 3eme : word[2:] --> " + word[2:])
print("Conversion d\'un nombre en chaine : str --> " + str(3.14))
print("Conversion d\'une chaine en nombre: float --> ", float('3.14'))
print("Longueur d\'une chaine : len -> " + str(len(word)))
print("Transformer une chaine en une liste de mots : chaine.split(char)")
print("La simplicite est la sophistication ultime.".split(" "))

parag.new(3,"Formatage: str.format()")
print("Accolade / numero argument / ':' / format")
print("Geeks :{0:2d}, Portal :{1:8.2f}".format(12, 0.546))

parag.new(3,"Regex")
import re
found =  re.search('bla_(.+?)_zip',"bla_28_zip")
print(found.group(1))

parag.new(2,"Listes")
carres = [1,2,49,16,25]
print("carres = [1,2,49,16,25]")
print("Liste constante    : liste = [0]*7")
print("Ajout d'un element : carres.append(36)")
print("Acces a un element : carres[2]  --> " + str(carres[2]))
print("Utilisation de ':' : carres[2:] --> " + str(carres[2:]))
print("Utilisation de ':' : carres[:2] --> " + str(carres[:2]))
print("Concatenation : squares + [36, 49, 64, 81, 100] -> " + str(carres + [36, 49, 64, 81, 100]))
print("Longueur d'une liste : len -> " + str(len(carres)))
carres.sort()
print("Tri : carres.sort() -> " + str(carres))
def cube(x): return x*x*x
#en python 2, map retourne une liste. En python 3 map retoune un iterateur
z=map(cube, range(1, 11))
print("Appliquer une fonction a une liste : map -> " + str(list(z)))
print("Alternative : z = [cube(x) for x in range(1, 11)]")
z = [cube(x) for x in range(1, 11)]
print(str(z))
liste = ["John", "Peter", "Vicky"]
print("Concatener une liste de chaine : separ.join(liste) -> " + "_".join(liste))
a = [1,4,2,7,1,9,0,3,4,6,6,6,8,3]
print("Filtrage des valeurs > 5 de la liste 'a': [x for x in a if x > 5]")
print("Noter les crochets qui reconstruisent une liste")
print([x for x in a if x > 5])

parag.new(2,"Tableaux = liste de liste")
print("Initialisation : tab = [0]*3")
print("z = [[i for i in range(10)] for j in range(10)]")
print("liste[0] = [1,2,3]; liste[1] = [4,5,6]")

parag.new(2,"Dictionnaire")
print("Initialisation d'un dictionnaire vide --> nombre_de_pneus = {}")
print("ajout d'un element                    --> nombre_de_pneus['voiture'] = 4")

nombre_de_pneus = {}
nombre_de_pneus["voiture"] = 4
nombre_de_pneus["vélo"] = 2

print("Parcourir un dictionnaire:")
for cle, valeur in nombre_de_pneus.items():
    print("l'élément de clé", cle, "vaut", valeur)
#----------------------------------------------------------------------------------
import re #regular expression
text = '        mModel->add(mOn(t) - mState(t) <= 0,CName("cOn",t));'
str1 = '->add\('
str2 = '\);'
strsearch=str1+'(.+?)'+str2
#found est la chaine comprise entre str1 et str2
found = re.search(strsearch, text).group(1)

#----------------------------------------------------------------------------------
parag.new(1,"Iterateurs")
print("Un iterateur est un objet qui implemente les methodes __iter__() et __next__()")
print("Ne pas confondre un iterateur et un iterable")
print("Un iterable est un objet qui peut renvoyer un iterateur (liste, set, dictionary,...)")
print("Exemple dans 'for c in carres : print(str(c))', 'c' est un iterateur de liste")
c = iter(carres)

#----------------------------------------------------------------------------------
parag.new(1,"Fonctions")
parag.new(2,"Fonction generale")
print("Le module 'fibo' contient une fonction 'fib'")
print("Soit on importe uniquement le module avec 'import fibo' et on accede a la fonction par fibo.fib()")
print("Soit on importe directement la fonction par 'from fibo import fib' et on appelle fib()")
import fibo
f = fibo.fib(2000)
print(f)

parag.new(2,"Plusieurs sorties")
def func(x,y):
   f1 = x+2*y
   f2 = x^2-y
   return [f1,f2]

x=3; y=5
[f1,f2] = func(x,y)
print("[f1,f2]=" + str([f1, f2]))
print("Ignorer des sorties : _,f3 = func(4,6)")
_,f3 = func(4,6)
print("f3 = " + str(f3))

parag.new(2,"Nombre d\'arguments variable : '*'")
def concat(*args):
    return "/".join(args)
print("def concat(*args) met les arguments dans la liste 'arg'")
s = concat("earth", "mars", "venus")
print(s)

parag.new(2,"Fonctions particulieres")
parag.new(3,"Fonction 'range'")

print(range(1,10,2))
s=""
for i in range(1, 10, 2):
    s=s+str(i)+" "
print(s)

parag.new(3,"Fonction 'type'")
print("type([1,2,3])       ="+ str(type([1,2,3])))
print("type({1,2,3})       ="+ str(type({1,2,3})))
print("type(range(1,10,3)) ="+ str(type(range(1,10,3))))

#----------------------------------------------------------------------------------
parag.new(1,"Standard Library")
parag.new(2,"Maths (import math)")
import math
print("math.cos(math.pi / 4) -->" + str(math.cos(math.pi / 4)))

#----------------------------------------------------------------------------------
parag.new(1,"Appel a la ligne de commande")
parag.new(2,"Commande simple")
import subprocess
cmdCommand = 'ipconfig'   #specify your cmd command
process = subprocess.Popen(cmdCommand, stdin = subprocess.PIPE, stdout = subprocess.PIPE)
output, error = process.communicate()
print(output)

parag.new(2,"Commande avec arguments")
#la commande suivante ne marche pas car je n'ai pas de dossier svn mais le msg d'erreur signifie
#que la commande a été appelée par windows
run_args = ['svn', 'commit', '-m', 'Automatic reference update', 'demo.py'] 
process2 = subprocess.Popen(run_args, stdout=subprocess.PIPE)
output, error = process2.communicate()
print(output)

#----------------------------------------------------------------------------------

parag.new(1,"Fichiers et Datatime")
parag.new(2,"Commandes de base")
print("Pour ecrire dans un fichier, il faut utiliser 'open(xxx,a/w)' puis 'write()'")
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
print("Pour lire une ligne d\'un fichier, il faut utiliser 'open(xxx,r)' puis 'read()'")
f = open("demofile2.txt", "r")
print(f.read())
f.close()


import datetime as dt
from pathlib import Path

# Datatime comporte des classes Date, DateTime et Timedelta

path = Path("demofile2.txt")
timestamp = dt.date.fromtimestamp(path.stat().st_mtime)
print(timestamp)
if dt.date.today() == timestamp:
    print("Le fichier a ete modifie aujourd'hui")
    
dt1 = dt.datetime.fromtimestamp(path.stat().st_mtime)
dt2 = dt.datetime.now()
delta = dt2 - dt1
if delta < dt.timedelta(seconds=5):
   print('Le fichier a ete cree il y a moins de 5 secondes')

print("Pour supprimer un fichier, il faut utiliser 'os.remove()'")

if os.path.exists("demofile2.txt"):
    os.remove("demofile2.txt")
else:
    print("The file does not exist")


#----------------------------------------------------------------------------------
parag.new(2,"Serialisation - Pickle")
print("Le but est d'écrire des structures de données complexes dans des fichiers pour pouvoir les relire plus tard.")
print("On utilise la bibliothèque Pickle")

import pickle
dict1 = {"Guillaume":718, "Romain":1055, "Pierre":711}
dict2 = {"Florian":782, "Francois":699, "Donatella":963}

fh = open('out.ser','wb') #format binaire
pickle.dump(dict1, fh)
pickle.dump(dict2, fh)
fh.close()
fh = open('out.ser','rb')
dict3 = pickle.load(fh)
dict4 = pickle.load(fh)
fh.close()
print(dict3)
#----------------------------------------------------------------------------------
parag.new(1,"Bases de données")
try:
    import sqlite3
    fichierDonnees ="bd_test.sq3"
    if os.path.isfile(fichierDonnees) :
        os.remove(fichierDonnees) #on supprime le fichier de la bdd pour pouvoir le recreer
    #creation de la bdd via requete sql
    conn = sqlite3.connect(fichierDonnees)
    cur = conn.cursor()
    cur.execute("CREATE TABLE passages (date TEXT, heure TEXT, id_point INT, id_titre INT)")
    cur.execute("INSERT INTO passages(date,heure,id_point,id_titre) VALUES('2014-10-29','08:34:15', 1, 1)")
    cur.execute("INSERT INTO passages(date,heure,id_point,id_titre) VALUES('2014-07-29','09:34:15', 2, 2)")
    cur.execute("INSERT INTO passages(date,heure,id_point,id_titre) VALUES('2014-08-29','10:34:15', 3, 3)")
    
    cur.execute("CREATE TABLE points(id INT, zone INT, ligne INT)")
    cur.execute("INSERT INTO points(id,zone,ligne) VALUES(1,7,12)")
    cur.execute("INSERT INTO points(id,zone,ligne) VALUES(2,2,8)")
    cur.execute("INSERT INTO points(id,zone,ligne) VALUES(3,6,1)")
    
    cur.execute("CREATE TABLE titres(id INT, zone_min INT, zone_max INT)")
    cur.execute("INSERT INTO titres(id,zone_min,zone_max) VALUES(1,2,4)")
    cur.execute("INSERT INTO titres(id,zone_min,zone_max) VALUES(2,1,4)")
    cur.execute("INSERT INTO titres(id,zone_min,zone_max) VALUES(3,1,5)")
    
    conn.commit()
    cur.close()
    conn.close()
    
    #lecture via requete sql
    conn = sqlite3.connect("bd_test.sq3")
    conn.execute
    cur = conn.cursor()
    cur.execute("SELECT * FROM passages")
    print(type(cur))
    
    for l in cur:
        print(l)
    
    #Jointure
    cur.execute("\
    SELECT passages.date,passages.heure \
    FROM passages \
    JOIN points ON passages.id_point = points.id \
    WHERE date>='2014-07-01' AND date <='2014-08-31' AND ligne=1")
    for l in cur:
        print(l)
    print("\n")
    
    #Double jointure
    cur.execute("\
    SELECT COUNT (*) \
    FROM points \
    JOIN titres ON passages.id_titre = titres.id \
    JOIN passages ON passages.id_point = points.id \
    WHERE points.zone>titres.zone_max OR points.zone<titres.zone_min \
    ")
    
    for l in cur:
        print(l[0])
    print("\n")
    
    cur.close()
    conn.close()

except:
    print("Unexpected error:", sys.exc_info()[0])

#----------------------------------------------------------------------------------
parag.new(1,"NumPy")
import numpy as np #np est un alias pour numpy
import matplotlib.pyplot as plt

print("NumPy est une bibliotheque Python pour travailler sur des tableaux")
print("Les operations sur les tableaux NumPy sont 50 fois plus rapides qu\'avec les listes car les tableaux NumPy stockent les donnees de facon contigue en memoire")

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print("attention le '+' pour concatener les listes ne marche pas sur des array")
print("il faut utiliser 'numpy.concatenate'")
print(np.concatenate([[7], arr, [8]]))
x = np.linspace(3, 9, 10)
print("linspace(3, 9, 10) : " + str(x))
print("Fonction appliquee a un tableau : np.sin(x) -> " )
print(np.sin(x))
print("Matrice (array)")
a = np.array([[1, 3, 3],[1, 4, 3],[1, 3, 4]])
print(a)
print("type(a) = "+ str(type(a)))
print("a[1,2] = " + str(a[1, 2]))
print("Inverse (linalg.inv):")
z=np.linalg.inv(a)
print(z)
print("Produit scalaire (a@b) : " +str(arr@arr));
print("Produit matriciel (dot(M1,M2)) ou M1.dot(M2):")
print(np.dot(a, z))
print("np.arange(12).reshape((3,4)) = ")
a = np.arange(12).reshape((3,4))
print(a)
print(type(a))

parag.new(2,"Manipulation de matrices")
print("A.size renvoie le nombre total d elements")
print("A.shape renvoie un tuple les dimensions")
print("M = np.zeros((N,N)) (tuple en arg car la matrice n'est pas forcement carree")
print("M = eye(n)")
print("Manipulation de bloc : M[i:i+n,i:i+n] = A")
print("Les notations des listes sont valides : V[5:]")
print("A = np.random.rand(n,n)")
print("A=B A et B referencent la meme matrice")
print("A=B.copy()")

def genereM(A):
    #avec des np_array
    dim = A.shape
    n = dim[0]
    N=n*n
    M = np.zeros((N,N))
    for i in range(0,N-n+1,n):
        M[i:i+n,i:i+n]=A
    for i in range(0,N-2*n+1,n):
        M[i:i+n,i+n:i+2*n]=-np.eye(n)
        M[i+n:i+2*n,i:i+n]=-np.eye(n)
    return M

n=10
A = np.ones((n,n))
M = genereM(A)

parag.new(2,"Tracer des courbes (matplotlib.pyplot)")
print("subplot(nb lignes, nb col, numero plot courant)")
plt.subplot(1,2,1)
x = np.linspace(0, 2*np.pi, 30)
y1 = np.cos(x)
y2 = np.sin(x)
plt.xlabel('time (s)')
plt.title("Courbes");
#---
plt.plot(x, y1, label="cos(x)")
plt.plot(x, y2, label="sin(x)")
plt.legend()

plt.subplot(1,2,2)
plt.spy(M)
plt.show()

#----------------------------------------------------------------------------------
parag.new(1,"Pytest")
print("Il faut ajouter le chemin de pytest.exe dans le path (dossier Python38\Scripts)")
print("Le fichier py.bat contient la ligne suivante:")
print("   set path=%PATH%;%CD%Apps\Python38;%CD%Apps\Python38\Scripts\n")
print("Depuis une console dans E:\perso\python, taper 'pytest test_simple.py'")
print("Alternative pour lancer tous les tests de tous les fichiers test_xxx.py du dossier courant:")
print("   python -m pytest")
print("L\'appel a pytest appelle toutes les fonctions test_xxx dans le fichier en argument")
print("Chaque fonction test_xxx appelle 'assert'\n")

print("Utilisation de marqueurs personalises (custom marker):")
print("On peut 'marquer' une fonction test avec une ligne")
print("   @pytest.mark.webtest")
print("puis on execute seulement les fonctions marquees avec la commande:")
print(   "pytest -v -m webtest")

#----------------------------------------------------------------------------------
parag.new(1,"Acces internet")
import urllib.request  #Used to make requests
x = urllib.request.urlopen("http://www.meteofrance.com/previsions-meteo-france/voiron/38500")
respData=x.read()
respData = respData.decode('UTF8')
print("Meteo Voiron")
dates = re.findall(r'<dt><a>(.*?)</a></dt>',str(respData))
min=re.findall(r'<span class="min-temp">(.*?)Minimale</span>',str(respData))
max=re.findall(r'<span class="max-temp">(.*?)Maximale</span>',str(respData))
title=re.findall(r'<li title="(.*?)">',str(respData))
for i in range (0,len(dates)-1):
    print("%6s %5s %5s %20s" % (dates[i], min[i], max[i], title[i]))
print("")

#----------------------------------------------------------------------------------
parag.new(1,"Pandas")
import pandas as pd
print("Pandas est une bibliotheque Python pour l'analyse de donnees")
print("On peut faire les memes operations que sur une table de base de donnees (count, join,...)")
print("Un dataframe est un tableau a 2 dimensions dont les donnees sont potentiellement heterogenes")
print("Les lignes et les colonnes peuvent avoir un nom")
print("Un dataframe se comporte comme un dictionnaire dont les clefs sont les noms des colonnes et les valeurs sont des séries.")
print("\n")
print("Creer des donnees")
df = pd.DataFrame([[1, 8], [4, 5], [7, 2]], index=['cobra', 'viper', 'sidewinder'], columns=['max_speed', 'shield'])
print(df)
print(type(df))
print("Chaque colonne d'un datafrane est une serie --> s = df['max_speed']")
s=df['max_speed']
print(type(s))

parag.new(2,"Selection des donnees")
print("liste des colonnes --> list(df.columns)")
print(list(df.columns))
print("liste des lignes --> list(df.index)")
print(list(df.index))
print('\ntri par en-tete de colonne decroissant (axis=1 : colonne)')
print(df.sort_index(axis=1, ascending=False))
print('\ntri par valeur de colonne croissante :')
print(df.sort_values(by='shield'))
print('\nExtraire un bloc par label:')
print(df.loc[['viper','cobra'], ['max_speed']])
print(df.loc[:, ['max_speed']])
print('\nExtraire un bloc par position:')
print(df.iloc[1, 1:2])
print('\nExtraire sur des booleens')
print(df[df>4])
print('\nAssignement conditionnel')
df.loc[df['max_speed']>4,'shield'] = -1
print('\nAjouter une colonne (age en col 1):')
df.insert(1, "age", [6, 4, 9])
print(df)
print('\nSupprimer une colonne:')
df1=df.drop(columns=['shield'])
print(df1)
print("\n")

parag.new(2,"csv")
print("Lire un fichier csv --> pd.read_csv()")
rs = pd.read_csv(".\\CogenSortie.csv", sep=';', decimal=',',skiprows=[1,2], na_values=['nan'], na_filter=True)
print("\n")

print("Ecrire un df dans un fichier csv --> df.to_csv()")
df = pd.DataFrame([[720, 'St Jean'], [710, 'St Jean'], [900, 'St Jean']], index=['Guillaume', 'Pierre', 'Jean-Luc'], columns=['Points', 'club'])
df.to_csv('ping.csv', sep=';')
print("\n")

parag.new(2,"Plot")
print("tracer une colonne avec matplotlib --> rs['Power'].plot()")
rs['Power'].plot()
print("les 20 premieres lignes --> rs['Power'][:20].plot()")
plt.figure()
rs['Power'][:20].plot()
plt.show()

parag.new(2,"Operations")
print("Join:")
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
print(left)
print('------')
print(right)
print('------')
tot = pd.merge(left, right, on='key')
print(tot)
print('------')
print("Ajout de col:")
tot['sum'] = tot['lval']+tot['rval']
print(tot)
print('------')
print("Groupby:")
data = {"Team": ["Red Sox", "Red Sox", "Red Sox", "Red Sox", "Red Sox", "Red Sox", "Yankees", "Yankees", "Yankees", "Yankees", "Yankees", "Yankees"],
		"Pos": ["Pitcher", "Pitcher", "Pitcher", "Not Pitcher", "Not Pitcher", "Not Pitcher", "Pitcher", "Pitcher", "Pitcher", "Not Pitcher", "Not Pitcher", "Not Pitcher"],
		"Age": [24, 28, 40, 22, 29, 33, 31, 26, 21, 36, 25, 31]}
df = pd.DataFrame(data)
print(df)
# group by Team, get mean, min, and max value of Age for each value of Team.
grouped_single = df.groupby('Team').agg({'Age': ['mean', 'min', 'max']})
print(grouped_single)


