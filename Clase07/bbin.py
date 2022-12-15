# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 16:21:30 2022

@author: master
"""
def insertar(lista,x):
    izq = 0
    der = len(lista) - 1
    pos = -1
    while izq <= der:
        medio = (izq + der) // 2
        
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
        
    if pos == -1:
        lista.append(x)
        lista  = sorted(lista)

        pos = lista.index(x)

    return pos
