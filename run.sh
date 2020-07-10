#! /usr/bin/env bash

FILE='/home/mehdi/sordariales/python/sordariales_ITS_phylo.seq'
var1=`date +%s`
python3 test.py
var2=`date +%s`
mafft $FILE > sortie.txt
var3=`date +%s`
temps1=$((var2 - var1))
temps2=$((var3 - var2))
echo "temps d'exécution de test.py : $temps1 seconde(s)" >> "sortie.txt"
echo "temps d'exécution de mafft : $temps2 seconde(s)" >> "sortie.txt"

