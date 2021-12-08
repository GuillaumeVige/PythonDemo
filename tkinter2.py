import tkinter

def compute():
	lab= tkinter.label(root, text = 'You pressed the button')
	lab.pack()

racine=tkinter.Tk()
retour=tkinter.IntVar() # cree une variable entiere pour recevoir la valeur retour
bouton1=tkinter.Radiobutton(racine, text="Oui", variable=retour, value=1)
bouton2=tkinter.Radiobutton(racine, text="Bof", variable=retour, value=3)
bouton3=tkinter.Radiobutton(racine, text="Non", variable=retour, value=2)
bouton1.grid(row=0, column=0)
bouton2.grid(row=1, column=0)
bouton3.grid(row=2, column=0)


print(retour.get()) # retourne 1, 2 ou 3 selon le bouton choisi, ou 0 si pas de choix

racine.mainloop()
