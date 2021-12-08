# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 15:34:46 2020

@author: GVIGE000

Test d'appel à un script depuis la ligne de commande avec passage d'arguments
Lancer deouis la ligne de commande

python cmd_arg.py "Thibaut a " 20 "ans"

"""

import sys

print(f"Name of the script      : " + str(sys.argv[0]))
print(f"Arguments of the script : " + str(sys.argv[1:]))

