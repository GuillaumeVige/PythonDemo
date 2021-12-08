from tkinter import *
fen   = Tk()
text1 = Label(fen, text='Bonjour !')
entr1 = Entry(fen)
bout1 = Button(fen, text='Quitter', command=fen.quit)
text1.grid( row=1, column=1)
entr1.grid( row=1, column=2)
bout1.grid( row=2, column=1)
fen.mainloop()
