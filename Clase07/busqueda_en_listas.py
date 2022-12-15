# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:52:47 2022

@author: master
"""

def busqueda_lineal_ordenada(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = 'no existe'  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista):
        if  z > e:
            pos = False
            break# recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos