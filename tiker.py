#!/bin/env python3
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from Bio import Align
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

#Important à noter: l'utilisation du dictionnaire DicoAlign est basé sur le principe que depuis python 3.7 l'ordre d'un dictionnaire est maintenu.

# Scorelist=[]
# def takeScore(elem):
#     return elem[2]

def AlignMeDaddy():
    listresult.delete(0,END)
    aligner = Align.PairwiseAligner()
    Badbois={}
    UsedSequence=[]
    global DicoAlign
    DicoAlign={}
    global Scorelist
    for index1,Sequence in enumerate(listons.curselection()):
        DicoAlign[listons.get(Sequence)[0]]=[]
    for Seq1 in listons.curselection():
        for index2,Seq2 in enumerate(listons.curselection()):
            if listons.get(Seq2)[0] not in UsedSequence:
                ScoreAlign=aligner.score(listons.get(Seq1)[1],listons.get(Seq2)[1])
                DicoAlign[listons.get(Seq1)[0]].append(ScoreAlign)
                print(listons.get(Seq1)[0],listons.get(Seq2)[0],ScoreAlign)
                if Seq1!=Seq2:DicoAlign[listons.get(Seq2)[0]].append(ScoreAlign)
    
    #Pour gérer la correspondance entre les séquence alignée et éviter de refaire l'alignement deux fois pour chaque séquence, Seq1 est stockée dans UsedSequence
        UsedSequence.append(listons.get(Seq1)[0])
    #Les tableau de score de DicoAlign et UsedSequence étant dans le même ordre,insertion dans la liste des score affichée en évitant de répéter la même paire deux fois
    for lines,Seq in enumerate(DicoAlign):
            for line in range(lines,len(DicoAlign)):
                listresult.insert((lines+line),(Seq,UsedSequence[line],DicoAlign[Seq][line]))
    print(list(DicoAlign))
    # for SupaBoi in listons.curselection():
    #     Badbois[SupaBoi]="NastyBoi"
    #     for index,GoodBoi in enumerate(listons.curselection()):
    #         if GoodBoi not in Badbois:
    #             Scorelist.append((listons.get(GoodBoi)[0],listons.get(SupaBoi)[0],aligner.score(listons.get(GoodBoi)[1],listons.get(SupaBoi)[1])))
    # print(Scorelist)
    # Scorelist.sort(key=takeScore)
    # for index,paire in enumerate(Scorelist):
    #     listresult.insert(index,(Scorelist[index][0],Scorelist[index][1],Scorelist[index][2]))

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
         Daddybox.insert(i,listons.get(i)[1])
   Daddybox.pack()

def OpenMe():
    filename = askopenfilename(title="Ouvrir votre document",filetypes=[('fasta files','.fasta'),('all files','.*')])
    fastafile = getfasta(filename)
    for index,sequence in enumerate(fastafile):
        listons.insert(index,(sequence,fastafile[sequence]))

#Afficher le Network
def NetworkThis():
    #ListSeq: Toutes les clés de DicoAlign
    ListSeq=list(DicoAlign)
    Edgelist=[]
    #Rappel,listes de DicoAlign contiennent un alignement supplémentaire (auto-alignement) qui n'est pas pris en compte pour le Network"
    for index1,Sequence in enumerate(DicoAlign):
        for index2 in range(index1+1,len(ListSeq)):
            print(index1,index2)
            Edgelist.append((Sequence,ListSeq[index2],DicoAlign[Sequence][index2]))
    print(Edgelist)
    G=nx.Graph()
    G.add_weighted_edges_from(Edgelist)
    nx.draw(G,with_labels=True)
    plt.show()

def HeatmapThis():
    Heatlist=[]
    [Heatlist.append(DicoAlign[sequence]) for sequence in DicoAlign]
    Heatlist.reverse()
    print(Heatlist)
    shaba=DicoAlign.keys()
    inverse=list(shaba)
    inverse.reverse()
    sns.heatmap(Heatlist,xticklabels=DicoAlign.keys(),yticklabels=inverse)
    plt.show()

def alerteThis():
        print("cocooooooooooooooo")


listAlign=[('babou','ATGC'),('weee','CTAGCTTTAGATTGATCGCGATCGATCGA'),('SHABOUGADA','CAGTAGGGGATCGATCTGGATCGA'),('houhouhou','AGCTAGCTCTTGATCGAGGT'),('Shabadouuuu','AGCTAGCTAGTCTGATCGGTAGTAGTCAGTATGCATGACGGT'),('wagadugou','GGT'),('yapapa','GCGAGGAGCGGTGGATCGAAGCTAGCTGATCGATCGATCGTAT')]


root = Tk()
root.title("Spiderboii")
root.geometry("500x300")


#définition de la fenêtre alignements
AlignFrame = Frame(root)
AlignFrame.place(x=0,y=0,width='500',height='150')

#Sous-frame d'options de selection,alignements
ButtonAlign=Frame(AlignFrame)
AlignMe=Button(ButtonAlign,text='Alignez moi!',command=AlignMeDaddy)
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
Yentry = ttk.Scrollbar(AlignFrame, orient="vertical", command=listons.yview)
Xentry = ttk.Scrollbar(AlignFrame, orient="horizontal", command=listons.xview)
Yentry.pack(side="right", fill="y")
Xentry.pack(side='bottom',fill="x")
listons.configure(yscrollcommand=Yentry.set,xscrollcommand=Xentry.set)
listons.pack()

#Frame de résultat et choix d'impression
ResultFrame=Frame(root)
ResultFrame.place(x=0,y=150,width='500',height='150')

#Sous-frame de choix de mode d'affichage
ChoiceFrame=Frame(ResultFrame)
Heatme=Button(ChoiceFrame,text='Heatmap',command=HeatmapThis)
Phylo=Button(ChoiceFrame,text='Phylo')
Network=Button(ChoiceFrame,text='Network',command=NetworkThis)
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
listresult.configure(yscrollcommand=resultY.set,xscrollcommand=resultX.set)
listresult.pack()



#Menu de sélection des fichiers
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open",command=OpenMe)
filemenu.add_command(label="Restart")

filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu=Menu(menubar,tearoff=0)
root.config(menu=menubar)
root.mainloop()