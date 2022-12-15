# -*- coding: utf-8 -*-

import random
#%% Generala servida 6.1

tirada = []
def tirar():
    for i in range(5):
        tirada.append(random.randint(1, 6))
    return tirada
tiro= tirar()
print(tiro)

def es_generala(tirada):
    for dado in tirada:
        if dado != tirada[0]:
            return False
    return True

mucha_suerte= es_generala(tirada)
print(mucha_suerte)

#%% intermedio
N = 1000000
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
#%% 6.2 Generala no necesariamente servida
tirada = []
N=3
def prob_generala():
    for i in range (N):
        tirar()
    
        
p = prob_generala()
print(p)

