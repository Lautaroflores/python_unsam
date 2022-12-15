# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 22:01:24 2022

@author: master
"""

import random
import matplotlib.pyplot as plt
import numpy as np


def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su 
    primer aparición, de lo contrario devuelve -1.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom
#%%Búsqueda binaria
def busqueda_binaria(lista,x):
    izq = 0
    der = len(lista) - 1
    pos = -1
    comps = 0
    while izq <= der:
        medio = (izq + der) // 2
        comps+=1
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

    return pos,comps


def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom
    
m = 10000
n = 100
k = 1000
lista = generar_lista(n, m)

largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
prom_comps_sec = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
prom_comps_bin = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
#%% Gráficos
for i, n in enumerate(largos):
    lista = generar_lista(n, m) # genero lista de largo n
    prom_comps_sec[i] = experimento_secuencial_promedio(lista, m, k)
    prom_comps_bin[i] = experimento_binario_promedio(lista, m, k)


 # ahora grafico largos de listas contra operaciones promedio de búsqueda.

plt.plot(largos,prom_comps_bin,color='red',linestyle='--')
# 
plt.plot(largos,prom_comps_sec,color='blue',linestyle='-.')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")
plt.title("Complejidad de la Búsqueda")
plt.ylim(8,10)
plt.xlim(0,260)
plt.legend()
plt.show()

