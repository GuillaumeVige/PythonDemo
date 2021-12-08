# -*- coding: utf-8 -*-
"""
G. Vigé 23/11/2021
Depuis l'agence CS il faut configurer le proxy pour accéder à internet via Python
Pour celà :
Paramètre windows / Reseau& internet / Proxy /
Enregistrer => télécharge le script pac, l'éditer et chercher l'addresse du serveur de proxy

"""

import requests
from bs4 import BeautifulSoup  #pip install BeautifulSoup4


proxies = {'http' : 'http://proxy-grenoble.si.c-s.fr:3128/',
           'https': 'http://proxy-grenoble.si.c-s.fr:3128/'
           }

url = "https://www.meteoblue.com/fr/meteo/semaine/voiron_france_2967758"

#html = requests.get(url,  proxies=proxies).content
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

def read_class(div, s):
    try:
        return div.find('div', attrs={'class',s}).text.split()[0]
    except AttributeError:
        s = s.replace('_','-')
        return div.find('div', attrs={'class',s}).text.split()[0]


for div in soup.find_all('div'):
    if div.has_attr('id') and div['id'].startswith('day'):
        # on cherche la valeur du champ
        jour = read_class(div, 'tab_day_short')
        tmin = read_class(div, 'tab_temp_min')
        tmax = read_class(div, 'tab_temp_max')

        # on cherche la valeur d'un attribut
        meteo = div.find('div', attrs={'class':"weather_pictogram_wrapper day"}).find('img').get('title')
        print('{0:6s}  {1:2s}°C   {2:2s}°C   {3:30s}'.format(jour,tmin,tmax,meteo))

input()

#url = "https://www.terre-net.fr/meteo-agricole/previsions-10-jours/isere/3012715#days-table-meteo-5j"
#html = requests.get(url).content
#soup = BeautifulSoup(html, 'html.parser')
#a=1
