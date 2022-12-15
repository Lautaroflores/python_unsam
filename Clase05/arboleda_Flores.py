#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:16:43 2022

@author: datascience
"""
#%% 6.11
import os
import matplotlib.pyplot as plt
import numpy as np
import csv

def leer_arboles(nombre_archivo):
    arboleda= []
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        rows=csv.reader(f)
        headers=next(rows)
        for nrow, row in enumerate(rows, start=1):
            record=dict(zip(headers,row))
            for arbol in record:
                arboleda.append(record)
    return arboleda
arboleda = leer_arboles('C:/Users/master/Desktop/UNSAM/Programación I/Ejercicios/ejercicios_python/Data/arbolado.csv')

H =[float(arbol["altura_tot"]) for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]

os.path.join('..', 'Data', 'arboles.csv')

altos=[float(arbol['altura_tot']) for arbol in arboleda]

plt.hist(altos ,bins=100) 
plt.ylabel('Cantidad de árboles')
plt.xlabel("Alto (m)")
plt.title('Altura de Jacarandás')
#%% 6.12

ayd = np.array([(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == "Jacarandá"])
plt.figure()
plt.scatter(ayd[:,1], ayd[:,0], c=np.random.rand(len(ayd)), alpha=0.5)
plt.xlabel('Diámetro [cm]')
plt.ylabel('Alto [m]')
plt.title('Relación diámetro-altura de Jacarandás')