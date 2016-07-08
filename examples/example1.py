#!/usr/bin/env python3
# coding: utf-8  ## nécessaire si on utilise des caractères spéciaux

f = open('fichier.txt', 'r+')

lines = f.readlines()  ## on obtient un tableau de lignes

line = f.read()  ## lance une exception ici car le fichier a été consommé<br/>par la fonction <b>readline</b> précédente

f.seek(0)  ## permet de revenir au début du fichier
f.write('ajout de caractères\n')

# on ferme le descripteur
f.close()  ## le "garbage collector" de Python peut le faire pour vous
