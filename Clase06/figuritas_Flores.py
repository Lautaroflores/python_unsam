# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 16:32:52 2022

@author: master
"""

import random
import numpy as np
#Creo el album vacío con figus total como cantidad de figus a pegar
def crear_album(figus_total):
    return  np.zeros(figus_total)
     

#Si falta alguna figurita, devuelve true
def album_incompleto(A):  
    if min(A)== 0:
        return True
    return False
    
    
#Numeros de figuritas random 
def comprar_figu(figus_total):
    aleatoria = random.randint(0, figus_total)
    return aleatoria


def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    i = 0
    while album_incompleto(album):
        album[comprar_figu(figus_total)-1] = 1
        i+=1
    return i
    
def experimento_figus(n_repeticiones,figus_total):
    l = [ cuantas_figus(figus_total) for rep in range(n_repeticiones) ]
    return np.mean(l)

n_repeticiones = 1000
figus_total = 670
prom = experimento_figus(n_repeticiones, figus_total)
print(f'Se tuvieron en cuenta {n_repeticiones} álbumes  de {figus_total} figuritas para calcular que se compra en promedio {prom} figuritas para llenar un álbum')

#%% ahora con paquetes
def comprar_paquete(figus_total, figus_paquete):
  figus = []
  for _ in range(figus_paquete):
    figus.append(random.randint(0,figus_total))
  return np.array(figus)

def cuantos_paquetes(figus_total, figus_paquete):
  album = crear_album(figus_total)
  global paquetes
  paquetes = 0
  while album_incompleto(album):
    paquetes += 1
    for figu in comprar_paquete(figus_total, figus_paquete):
      album[figu - 1] = 1
  return paquetes

figus_paquete = 5
n_repeticiones = 100
figus_total = 670
results = []

for i in range(n_repeticiones):
  results.append(cuantos_paquetes(figus_total, figus_paquete))
print(f'se tuvieron en cuenta {n_repeticiones} álbumes de {figus_total} figuritas, para estimar que se deberían comprar {sum(results)/len(results)} paquetes de {figus_paquete} para llenar el album')
