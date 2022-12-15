# -*- coding: utf-8 -*-

import random

tirada = []

def tirar():
   
    for i in range(5):
        tirada.append(random.randint(1, 6))
    return (tirada)
lista= tirar()
def es_generala(t):
    if len(set(t)) ==1:
        resultado=True
    else: resultado = False
    return (resultado)

llamar_res= es_generala(lista)

N = 100000
G = sum([llamar_res for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
#%% 6.2 Generala no necesariamente servida
