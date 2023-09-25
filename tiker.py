#!/bin/env python3
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *

def getfasta(fasta_file):
    nameHandle=open(fasta_file,"r")
    fastas={}
    for line in nameHandle:
        if line[0]=='>':
            header=line[1:-2]
            fastas[header]=''
        else:
            fastas[header]+=line.split('\n')[0]
    nameHandle.close()
    return(fastas)

def selectall():
    listons.selection_set(0,listons.size())

def deselect():
    listons.selection_clear(0,listons.size())
    
def Printmedaddy():
   Daddy = Toplevel(root)
   Daddybox=Listbox(Daddy)
   for i in listons.curselection():
         Daddybox.insert(i,listons.get(i))
   Daddybox.pack()

def OpenMe():
   filename = askopenfilename(title="Ouvrir votre document",filetypes=[('fasta files','.fasta'),('all files','.*')])
   fastafile = getfasta(filename)
   for index,sequence in enumerate(fastafile):
        listons.insert(index,sequence,"\t",fastafile[sequence])


listAlign=[('babou','ATGC'),('weee','GGCT'),('wagadugou','GGT'),('wagadugou','GGT'),('wagadugou','GGT'),('wagadugou','GGT'),('wagadugou','GGT'),('wagadugou','GGT'),('wagadugou','GGT'),('wagadugou','GGT'),('wagadugou','GGT')]


root = Tk()
root.title("Spiderboii")
root.geometry("500x300")


#définition de la fenêtre alignements
AlignFrame = Frame(root)
AlignFrame.place(x=0,y=0,width='500',height='150')

#Sous-frame d'options de selection,alignements
ButtonAlign=Frame(AlignFrame)
AlignMe=Button(ButtonAlign,text='Alignez moi!',command=OpenMe)
SelectAlign=Button(ButtonAlign,text='Tout sélectionner',command=selectall)
DeselectAlign=Button(ButtonAlign,text='Desélectionner',command=deselect)
SelectAlign.pack(side='left')
DeselectAlign.pack(side='left')
AlignMe.pack(side='right')
ButtonAlign.pack()

#listbox contenant les sequences entrées
listons=Listbox(AlignFrame,selectmode=MULTIPLE,width=100)
for i in range(0,len(listAlign)):
   listons.insert(i,listAlign[i])
yscrollbar = ttk.Scrollbar(AlignFrame, orient="vertical", command=listons.yview)
xscrollbar = ttk.Scrollbar(AlignFrame, orient="horizontal", command=listons.xview)
yscrollbar.pack(side="right", fill="y")
xscrollbar.pack(side='bottom',fill="x")
listons.configure(yscrollcommand=yscrollbar.set,xscrollcommand=xscrollbar.set)
listons.pack()
####################################


#
#
#
#
#
#
#
##############################
#Frame de résultat et choix d'impression
ResultFrame=Frame(root)
ResultFrame.place(x=0,y=150,width='500',height='150')

#Sous-frame de choix de mode d'affichage
ChoiceFrame=Frame(ResultFrame)
Heatme=Button(ChoiceFrame,text='Heatmap',command=Printmedaddy)
Phylo=Button(ChoiceFrame,text='Phylo')
Network=Button(ChoiceFrame,text='Network')
Heatme.pack(side='left')
Phylo.pack(side='right')
Network.pack(side='right')
ChoiceFrame.pack()

#affichage des alignements
listresult=Listbox(ResultFrame,width=250)
resultY = ttk.Scrollbar(ResultFrame, orient="vertical", command=listresult.yview) 
resultX = ttk.Scrollbar(ResultFrame, orient="horizontal", command=listresult.xview)
resultY.pack(side="right", fill="y")
resultX.pack(side='bottom',fill="x")
listresult.configure(yscrollcommand=yscrollbar.set,xscrollcommand=xscrollbar.set)
listresult.pack()


########################################
#Menu de sélection des fichiers
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open",command=OpenMe)
filemenu.add_command(label="Restart")

filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()