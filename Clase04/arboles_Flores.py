#%% 4.13
import csv
from pprint import pprint
from collections import Counter
def leer_parque(nombre_archivo, parque):
    ls= []
    with open(nombre_archivo, 'rt',  encoding="utf8") as f:
        rows=csv.reader(f)
        headers=next(rows)
        for nrow, row in enumerate(rows, start=1):
            record=dict(zip(headers,row))
            if parque == record['espacio_ve']:
                for arbol in record:
                    ls.append(record)
                    break
                
    return ls

lista_arboles = leer_parque('../Data/arbolado.csv', 'GENERAL PAZ')

pprint(lista_arboles) 
#%% 4.14
def especies (lista_arboles):
    especies = []
    
    for item in lista_arboles:
        especies.append(item['nombre_com'])
        ls_especies = set(especies)
    return ls_especies

funcion_especies = especies(lista_arboles)

pprint(funcion_especies)

#%% 4.15
def contar_ejemplares(lista_arboles):
    e = []
    for item in lista_arboles:
        
        e.append(item['nombre_com'])
        
        ejemplares = Counter(e)
        
    return ejemplares

contador = contar_ejemplares(lista_arboles)
commons = contador.most_common(5)
pprint(commons)
 
#%% 4.16
def obtener_alturas(lista_arboles, especie):
    alt=[]
   
    for esp in lista_arboles:
        if esp['nombre_com'] == especie:
            for arb in esp:
                altura =float(esp['altura_tot'])
                
                alt.append(altura)
    return alt

alturas = obtener_alturas(lista_arboles, 'Jacarandá')
max_altura= max(alturas)
prom_altura = sum(alturas)/len(alturas)
print(f'Altura máxima:{max_altura}. Promedio altura: {prom_altura}')
        
#%% 4.17
def obtener_inclinaciones(lista_arboles, especie):
    inc=[]
   s
    for esp in lista_arboles:
        if esp['nombre_com'] == especie:
            for arb in esp:
                inclinacion = float(esp['inclinacio'])
                
                inc.append(inclinacion)

    return inc
inclinaciones = obtener_inclinaciones(lista_arboles, 'Jacarandá')

pprint(inclinaciones)
        
#%% 4.18
