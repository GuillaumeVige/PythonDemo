'''
Ce script extrait les donnees sur les fichiers csv exportés depuis fitbit
G Vigé - 27/08/2021

Ouvrir une console
Installer pandas:
d:\Apps\Python38\python.exe -m pip install pandas
puis lancer
d:\Apps\Python38\python.exe d:\Programmation\python\Fitbit\fitbit.py
'''



import pandas as pd
import regex as re
from io import StringIO
import matplotlib.pyplot as plt

filename = "f:\\Programmation\\python\\Fitbit\\fitbit_export_20210827.csv"
fich = open(filename, "r")
contenu = fich.read()
fich.close()

# '.' comme separateur decimal
contenu = re.sub(r'(\d),(\d)',r'\1.\2',contenu)

# suppression des guillemets
contenu = contenu.replace('"','')

corps = contenu.split('Aliments')[0]

z = StringIO(corps)
df = pd.read_csv(z,skiprows=1)


#print(df)

df['Poids'].plot()
plt.show()

# Extraction de la table Aliments
aliments = re.findall(r'Aliments(.*?)Activit', contenu, re.DOTALL)[0]
aliments = aliments.replace('Teneur calorique de','Calories')
# on vire les caractères spéciaux
aliments = str(aliments.encode('ascii','ignore'))
aliments = aliments.replace('\\n','\n')
#print(aliments)

z = StringIO(aliments)
df = pd.read_csv(z,skiprows=1)

df['Calories'].plot()
plt.show()