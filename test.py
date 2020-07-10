#! /usr/bin/env python3


###Ce programme :
###(1)donne la longeur de chaque séquence
###(2)affiche la distribution de tailles sous forme d'histogramme
###(3) recherche le motif 58S

from matplotlib import pyplot
import numpy
from Bio import SeqIO

#Partie (1)

liste = [];
for sequence in SeqIO.parse("sordariales_ITS_phylo.seq", "fasta"):
    liste.append(len(sequence)) #on stocke les tailles des séquences
print(liste[:]) #affiche tous les éléments de la liste


#Partie (2) on affiche les données avec un histogramme

array = numpy.array(liste)
fig,ax = pyplot.subplots(1,1)
ax.hist(array)
ax.set_title("distribution des longueurs des séquences")
ax.set_xlabel("taille")
ax.set_ylabel("nombre de séquences")
pyplot.savefig('distrib.png')

#Partie (3) on recherche un même motif dans les séquences

from Bio.SeqIO.FastaIO import SimpleFastaParser #SimpleFastaParser pour avoir la sequence en String
import regex

motif_58s = '(AAATGCGATAAG){e<=2}'
liste = []
count = 0
tot = 0
with open("sordariales_ITS_phylo.seq") as inp:
    for title, sequence in SimpleFastaParser(inp):
        a = regex.search(motif_58s, sequence, regex.BESTMATCH)
        tot= tot + 1
        if (a!=None):
            count= count + 1
        print(a)
        liste.append(a)
    
pourcent = (count/tot)*100 # le pourcentage de sequence comprenant à peu près l'ITS
print(pourcent)
