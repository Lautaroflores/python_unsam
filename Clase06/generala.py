
import random

def tirar(n_dados):
    """
    devuelve una lista con n_dados dados generados aleatoriamente
    """

    tirada = [random.randint(1,6) for _ in range(n_dados)]

    return tirada


def es_generala(tirada):
    """
    devuelve True si y sólo si los cinco dados de la lista tirada son iguales
    """
    
    return max(tirada) == min(tirada)


def guardo(tirada):
    """
    devuelve una lista con los valores que coinciden de una tirada
    """

    cuenta = [0] * 6
    for dado in tirada:
        cuenta[dado - 1] += 1
  
    lista = []
    dado_max = cuenta.index(max(cuenta)) + 1
    for dado in tirada:
        if dado == dado_max: lista.append(dado)

    return lista



N = 100000 # ó 1000000

print(""" E 5.1 : generala servida """)
G = sum([es_generala(tirar(5)) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {100 * prob:.6f} %')
print()

#%%
print(""" Generala no necesariamente servida """)
G = []
for k in range(N):

    l = [] 
    n = 5
    i = 0
    while (i < 3):
        dados = tirar(n)
        dados = dados + l
        check = es_generala(dados)
        if check == True: break

        l = guardo(dados)

        n = 5 - len(l)

        i += 1
    
    G.append(check)

prob = sum(G) / N

print(f'Tiré {N} veces, de las cuales {sum(G)} saqué generala en, como máximo, tres tiradas')
print(f'Podemos estimar la probabilidad de sacar generala en tres tiros como {100 * prob:.6f} %')