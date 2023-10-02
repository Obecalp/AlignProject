#!/bin/env python3
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from Bio import pairwise2
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns




#Alignement global des séquences sélectionnées du menu puis insertion dans un dictionnaire dans le format:
#{NomSeq1:[0,ScoreSeq2,ScoreSeq3],NomSeq2;[ScoreSeq2,0,scoreSeq3],NomSeq3:[ScoreSeq1,ScoreSeq2,0]}
#Chaque liste contient les Score des alignement avec les autres séquences, ordonnée dans le même ordre que le dictionnaire DicoAlign. Pour chaque séquence, la valeur 0 est mise à la position correspondant à cette séquence dans le dictionnaire (La première séquence aura 0 en première position, deuxième séquence en deuxième position, etc..)
def AlignThis():
    global DicoAlign
    DicoAlign={} #reset du dictionnaire à chaque nouvel appel de fonction.
    listresult.delete(0,END)
    UsedSequence=[]
    for index1,Sequence in enumerate(listons.curselection()):
        DicoAlign[listons.get(Sequence)[0]]=[]
    for Seq1 in listons.curselection():
        UsedSequence.append(listons.get(Seq1)[0])
        DicoAlign[listons.get(Seq1)[0]].append(0)
        for index2,Seq2 in enumerate(listons.curselection()):
            if listons.get(Seq2)[0] not in UsedSequence:
                ScoreAlign=pairwise2.align.globalxx(listons.get(Seq1)[1], listons.get(Seq2)[1],score_only=True)
                DicoAlign[listons.get(Seq1)[0]].append(ScoreAlign)
                print(listons.get(Seq1)[0],listons.get(Seq2)[0],ScoreAlign)
                if Seq1!=Seq2:DicoAlign[listons.get(Seq2)[0]].append(ScoreAlign)
    
#Pour gérer la correspondance entre les séquence alignée et éviter de refaire l'alignement deux fois pour chaque séquence, Seq1 est stockée dans UsedSequence
#Les tableau de score de DicoAlign et UsedSequence étant dans le même ordre,insertion dans la liste des score affichée en évitant de répéter la même paire deux fois
    for lines,Seq in enumerate(DicoAlign):
            for line in range(lines+1,len(DicoAlign)):
                listresult.insert((lines+line),(Seq,UsedSequence[line],DicoAlign[Seq][line]))
    print(DicoAlign)

#Fonction utilisée en Cours, retourne un dictionnaire contenant les séquences sous le format:
#{Seq1:sequence1,Seq2:sequence2}
def getfasta(fasta_file):
    nameHandle=open(fasta_file,"r")
    fastas={}
    for line in nameHandle:
        if line[0]=='>':
            header=line[1:-1]
            fastas[header]=''
        else:
            fastas[header]+=line.split('\n')[0]
    nameHandle.close()
    return(fastas)

#Sélection de l'intégralité des item à aligner
def selectall():
    if listons.size()>0:listons.selection_set(0,listons.size())
    else:alerteThis("Pas de séquence à sélectionner")

#Déselection des items à aligner"
def deselect():
    listons.selection_clear(0,listons.size())
    



#Ouvre le menu de sélection de fichier fasta
def OpenMe():
    filename = askopenfilename(title="Ouvrir votre document",filetypes=[('fasta files','.fasta'),('all files','.*')])
    fastafile = getfasta(filename)
    for index,sequence in enumerate(fastafile):
        listons.insert(index,(sequence,fastafile[sequence]))

#Afficher le Network
def NetworkThis():
    if len(DicoAlign)<3:
            alerteThis("Pour faire un réseau veuillez aligner au moins trois séquences")
    else:
        print(DicoAlign)
    #ListSeq: Toutes les clés de DicoAlign
        ListSeq=list(DicoAlign)
        Edgelist=[]
        #Rappel,listes de DicoAlign contiennent une valeur supplémentaire (0) qui n'est pas pris en compte pour le Network"
        for index1,Sequence in enumerate(DicoAlign):
            for index2 in range(index1+1,len(ListSeq)):
                print(index1,index2)
                Edgelist.append((Sequence,ListSeq[index2],DicoAlign[Sequence][index2]))
        print(Edgelist)
        G=nx.DiGraph()
        G.add_weighted_edges_from(Edgelist)
        pos=nx.spring_layout(G)
        nx.draw(G,node_color="red",edge_color="green",with_labels=True)
        plt.show()

#Affichage la heatmap
def HeatmapThis():
    print(len(DicoAlign))
    if len(DicoAlign)<3:
            alerteThis("Pour faire une heatmap alignez au moins trois séquences")
    else:
        Heatlist=[]
        [Heatlist.append(DicoAlign[sequence]) for sequence in DicoAlign]
        print(Heatlist)
        mask = np.zeros_like(Heatlist, dtype=np.bool_)
        mask[np.triu_indices_from(mask)] = True
        Yaxe=list(DicoAlign.keys())
        Xaxe=Yaxe
        sns.heatmap(Heatlist,xticklabels=Xaxe,yticklabels=Yaxe,mask=mask)
        plt.show()

#message d'erreur pour les boutons "heatmap" et ""
def alerteThis(*args):
        oupsi=Toplevel(width=300,height=40)
        oupsi.geometry("200x80")
        framons=Frame(oupsi,width=150,height=40)
        coco=Label(framons,text=args[0],wraplength=200).pack(side='top')
        ok=Button(framons,text="Fermer",command=oupsi.destroy).pack(side='bottom')
        framons.pack(side=BOTTOM)

#listAlign=[('babou','ATGC'),('weee','CTAGCTTTAGATTGATCGCGATCGATCGA'),('SHABOUGADA','CAGTAGGGGATCGATCTGGATCGA'),('houhouhou','AGCTAGCTCTTGATCGAGGT'),('Shabadouuuu','AGCTAGCTAGTCTGATCGGTAGTAGTCAGTATGCATGACGGT'),('wagadugou','GGT'),('yapapa','GCGAGGAGCGGTGGATCGAAGCTAGCTGATCGATCGATCGTAT')]

def RestartAll():
     listons.delete(0,END)


##############   Graphismes Tkinter    ###########


root = Tk()
root.title("AlignProject")
root.geometry("500x300")


#définition de la fenêtre alignements
AlignFrame = Frame(root)
AlignFrame.place(x=0,y=0,width='500',height='150')

#Sous-frame d'options de selection,alignements
ButtonAlign=Frame(AlignFrame)
AlignMe=Button(ButtonAlign,text='Alignez moi!',command=AlignThis)
SelectAlign=Button(ButtonAlign,text='Tout sélectionner',command=selectall)
DeselectAlign=Button(ButtonAlign,text='Desélectionner',command=deselect)
SelectAlign.pack(side='left')
DeselectAlign.pack(side='left')
AlignMe.pack(side='right')
ButtonAlign.pack()

#listbox contenant les sequences entrées
listons=Listbox(AlignFrame,selectmode=MULTIPLE,width=100)
# for i in range(0,len(listAlign)):
#    listons.insert(i,listAlign[i])
Yentry = ttk.Scrollbar(AlignFrame, orient="vertical", command=listons.yview)
Xentry = ttk.Scrollbar(AlignFrame, orient="horizontal", command=listons.xview)
Yentry.pack(side="right", fill="y")
Xentry.pack(side='bottom',fill="x")
listons.configure(yscrollcommand=Yentry.set,xscrollcommand=Xentry.set)
listons.pack()

######Frame de résultat et choix d'impression
ResultFrame=Frame(root)
ResultFrame.place(x=0,y=150,width='500',height='150')

#Sous-frame de choix de mode d'affichage
ChoiceFrame=Frame(ResultFrame)
Heatme=Button(ChoiceFrame,text='Heatmap',command=HeatmapThis)
Network=Button(ChoiceFrame,text='Network',command=NetworkThis)
Heatme.pack(side='left')
Network.pack(side='right')
ChoiceFrame.pack()


#affichage des alignements dans le listBox2
listresult=Listbox(ResultFrame,width=250)
resultY = ttk.Scrollbar(ResultFrame, orient="vertical", command=listresult.yview) 
resultX = ttk.Scrollbar(ResultFrame, orient="horizontal", command=listresult.xview)
resultY.pack(side="right", fill="y")
resultX.pack(side='bottom',fill="x")
listresult.configure(yscrollcommand=resultY.set,xscrollcommand=resultX.set)
listresult.pack()

####Fin frame resultat

######Menu de sélection des fichiers
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open",command=OpenMe)
filemenu.add_command(label="Restart",command=RestartAll)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu=Menu(menubar,tearoff=0)
root.config(menu=menubar)

root.mainloop()