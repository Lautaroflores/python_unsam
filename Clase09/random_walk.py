# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 22:39:44 2022

@author: master
"""

from matplotlib import pyplot as plt
import numpy as np
import random as random

def cm2inch(value):
    return value/2.54


def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)
        
    return pasos.cumsum()

N = 100000


recorridos=[]
i_max = 0
i_min = 0
#Gráfico arriba
fig = plt.figure(figsize=(cm2inch(19.1), cm2inch(10.2)))
plt.subplot(2, 1, 1)

for n in range(12):
    #Para cada caminata, le defino un color al azar
    r = random.random() 
    b = random.random() 
    g = random.random() 
    caminatas = randomwalk(N)
    recorridos.append(caminatas)
    col = (r, g, b) 
    plt.plot(caminatas, color=col) #12 lineas de distintos colores
    max_min =np.abs(recorridos[n]).max()
   
# =============================================================================
# Busco el valor máximo de todas las caminatas y guardo el índice, lo mismo
# con el valor mínimo
# =============================================================================
    if max_min > np.abs(recorridos[i_max]).max():

        i_max = n

    elif max_min < np.abs(recorridos[i_min]).max():
        i_min = n
        

#Sigo graficando las 12 caminatas
plt.title("12 caminatas al azar")
plt.ylim(-1000,1000)
plt.xticks([]), plt.yticks([-500,0,500])

#Gráfico abajo a la izquierda
plt.subplot(2, 2, 3)
plt.title('La caminata que más se aleja')
plt.plot(recorridos[i_max])
plt.ylim(-1000, 1000)
plt.xticks([]), plt.yticks([-500,0,500])

#Gráfico abajo a la derecha
plt.subplot(2, 2, 4)
plt.title('La caminata que menos se aleja')
plt.plot(recorridos[i_min])
plt.ylim(-1000, 1000)
plt.xticks([]), plt.yticks([])

plt.show()



