#!/bin/env python3
from Bio import Align
import sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import time

#
def oupsi(Mistake):
    CLEAR = '\x1b[5K'
    print(Mistake)
    for i in range(9, 0, -1):
        print("                       \n  /|\         \n /_o_\@       \n   |__|__|     \n      |       \n     / \      \n    /   \     ",end='\r')
        print('\033[6A',end=CLEAR)
        time.sleep(0.5)
        print("   /|\       \n  /_o_\      \n    | @      \n     \|__|    \n      |     \n     / \     \n    /   \    \n")
        time.sleep(0.5)
        if i != 1: print('\033[8A',end=CLEAR)


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

def AlignMeDaddy(dico):
    for SupaBoi in dico:
        Badbois[SupaBoi]="NastyBoi"
        for GoodBoi in dico:
            if GoodBoi not in Badbois:
                ListBoi.append((GoodBoi,SupaBoi,aligner.score(dico.get(GoodBoi),dico.get(SupaBoi))))
    return ListBoi

def WhereSmyFasta(file):
    answer=''
    if "fasta" not in file:
            while(answer!='y' and answer!='n'):
                oupsi("Warning: L'extension du fichier n'est pas fasta, continuer? (y/n)")
                answer=input()
    if answer=="y":
            return 0
    else: exit(0)

aligner = Align.PairwiseAligner()

G=nx.Graph()


nodeFamily=[]
# WhereSmyFasta(sys.argv[1])
dico=getfasta(sys.argv[1])
# listDico=list(dico.keys())

Badbois={}
ListBoi=[]

#T=nx.from_dict_of_dicts()
dicoAlign=AlignMeDaddy(dico)
print(dicoAlign)
    # for i in range(0,len(dico.keys())):
    #     pinpin=dico[listDico[i]]
    #     for minilist in range(i+1,len(listDico)):
    #         panpan=dico[listDico[minilist]]
    #         score=aligner.score(pinpin,panpan)
    #         nodeFamily.append(score)
    #         print(score,listDico[i],listDico[minilist])

    #     if i>len(listDico)-1: break

# [print(i) for i in dicoAlign]

# print(dico.keys())
#G.add_nodes_from(nodeFamily)
#G.add_nodes_from(list(dico.keys()))
G.add_weighted_edges_from(dicoAlign)
#G.add_nodes_from(['A','B','C'])
#G.add_weighted_edges_from([('A','B',100),('B','C',1),('A','C',1)])
#nx.set_edge_attributes(G,{('A','B'):{'cost':1},('B','C'):{'cost':100},('A','C'):{'cost':50}})

#nx.draw_networkx_edges(G,{'A':1,'B':2,'C':3};)
print(G.nodes())
#G.add_edges_from(nodeFamily)
#G.add_edges_from([(1,2),(2,3),(18,20)])

nx.draw(G,with_labels=True)
plt.show()
