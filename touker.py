#!/bin/env python3
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

def callback():
    if messagebox.askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
        messagebox.showwarning('Titre 2', 'Tant pis...')
    else:
        messagebox.showinfo('Titre 3', 'Vous avez peur!')
        messagebox.showerror("Titre 4", "Aha")

Button(text='Action', command=callback).pack()
fenetre = Tk(baseName="blabla")

label = Label(fenetre, text="Hello World")
label.pack()
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()
# radiobutton
value = StringVar() 
bouton1 = Radiobutton(fenetre, text="Oui", variable=value, value=1)
bouton2 = Radiobutton(fenetre, text="Non", variable=value, value=2)
bouton3 = Radiobutton(fenetre, text="Peu être", variable=value, value=3)
bouton1.pack()
bouton2.pack()
bouton3.pack()
liste = Listbox(fenetre)
liste.insert(1, "Python")
liste.insert(2, "PHP")
liste.insert(3, "jQuery")
liste.insert(4, "CSS")
liste.insert(5, "Javascript")
Button(text='Action', command=callback).pack()
liste.pack()
fenetre.mainloop()