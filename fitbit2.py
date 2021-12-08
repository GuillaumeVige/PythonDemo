# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 13:47:33 2021

@author: Guillaume Vigé
Analyse des données Fitbit
"""
from zipfile import ZipFile
import pandas as pd
import json
import datetime

# lecture des scores de sommeil
# les données sur le score de sommeil commencent au 2019-08-22
with ZipFile(r'D:\Programmation\python\Fitbit\MyFitbitData.zip') as myzip:
    df_score = pd.read_csv(myzip.open('Guillaume/Sleep/sleep_score.csv'))

#=============================================================================

def analyse_spectrale(col):
    import numpy as np
    import matplotlib.pyplot as plt
    nobs = len(col)
    y_fft = np.abs(np.fft.rfft(col))
    freq = np.fft.rfftfreq(nobs)
    plt.figure(figsize=(10, 7))
    plt.plot(freq[2:], y_fft[2: ])
    plt.xlabel('frequency (1/day)')
    plt.show()

archive = ZipFile(r'D:\Programmation\python\Fitbit\MyFitbitData.zip', 'r')
list_of_files = archive.namelist()
df=pd.DataFrame(columns =['dateOfSleep', 'minutesAsleep', 'minutesDeep'])
for elem in list_of_files:
    if 'sleep-' in elem:
        jsonFile = archive.open(elem) #ouvre le fichier dans le zip
        data = jsonFile.read()  #lit le fichier et met le contenu dans une liste
        d = json.loads(data)
        for i in range(len(d)):
            if 'deep' in d[i]["levels"]["summary"].keys():
                date = datetime.datetime.strptime(d[i]["dateOfSleep"], "%Y-%m-%d")
                df.loc[len(df)] = [ date,
                                    d[i]["minutesAsleep"],
                                    d[i]["levels"]["summary"]["deep"]["minutes"]
                                  ]

#rechercher s'il y a des dates en double dans df
# df2 = df[df.duplicated('dateOfSleep', keep=False)].sort_values('dateOfSleep')

#df.plot(x='dateOfSleep', y='minutesAsleep', style='o')
# moyenne glissante
w = 20
df['minutesAsleepGlissante'] = df["minutesAsleep"].rolling(window=w).mean()
df['minutesAsleepGlissante'] /= df['minutesAsleepGlissante'].mean()
df['minutesDeepGlissante'] = df["minutesDeep"].rolling(window=w).mean()
df['minutesDeepGlissante'] /= df['minutesDeepGlissante'].mean()
df.plot(x='dateOfSleep', y=['minutesAsleepGlissante','minutesDeepGlissante'],style=['b','r'])

# analyse_spectrale(df2['minutesAsleep'])

# convertir les dates des scores et fusionner avec df

