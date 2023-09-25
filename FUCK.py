#!/bin/env python3
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

from tkinter import *
from tkinter import ttk


def Printmedaddy():
   Daddy = Toplevel(root)
   Daddybox=Listbox(Daddy)
   for i in listons.curselection():
         Daddybox.insert(i,listons.get(i))
   Daddybox.pack()
   

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

listAlign=[('babou','ATGC'),('weee','GGCT'),('wagadugou','GGT'),('wagadugou','GGT'),('wagadugou','GGT'),('wagadugou','GGT'),('wagadugou','GGT'),('wagadugou','GGT'),('wagadugou','GGT'),('wagadugou','GGT'),('wagadugou','GGT')]


px=0
py=0
root = Tk()
root.title("Spiderboii")
root.geometry("500x300")

#définition de la fenêtre alignements
AlignFrame = Frame(root)
AlignFrame.place(x=0,y=50,width='250',height='150')
AlignMe=Button(AlignFrame,text='Alignez moi!',width='200')
#OH FUCKING PUTAIN DE YEAH GARDE
listons=Listbox(AlignFrame,selectmode=MULTIPLE,width=100)
for i in range(0,len(listAlign)):
   listons.insert(i,listAlign[i])
yscrollbar = ttk.Scrollbar(AlignFrame, orient="vertical", command=listons.yview)
xscrollbar = ttk.Scrollbar(AlignFrame, orient="horizontal", command=listons.xview)
listons.configure(yscrollcommand=yscrollbar.set,xscrollcommand=xscrollbar.set)
AlignMe.pack()
listons.pack()

#Frame de résultat et choix d'impression
ResultFrame=Frame(root)
ResultFrame.place(x=0,y=200,width='250',height='150')

#Frame de choix d'impression
ChoiceFrame=Frame(ResultFrame)
ChoiceFrame.pack()
Heatme=Button(ChoiceFrame,text='Heatmap',command=Printmedaddy)
Phylo=Button(ChoiceFrame,text='Phylo')
Network=Button(ChoiceFrame,text='Network')
Heatme.pack(side='left')
Phylo.pack(side='right')
Network.pack(side='right')
listresult=Listbox(ResultFrame,width=250)
listresult.pack()




menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Restart", command=donothing)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()