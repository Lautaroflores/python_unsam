#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.5. Función tiene_a()

#El error estaba en la línea ' if expresion[i] == 'a':' ya que solo
#chequeaba que la primer letra sea una 'a'

#Se modifició por un 'if in' que verifica si la 'a' se encuentra en la palabra
#Versión corregida:

def tiene_a(expresion):

    if 'A' or 'a' in expresion:
        return True
    else:
        return False
    
tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.6

#El error es semántico, le faltaban ':', '=' y estaba mal escrito
#Versión corregida:

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n: #Agrego :
        if expresion[i] == 'a': #Agrego un = y :
            return True
        i += 1
    return False #Cambio 'Falso' por 'False'

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.7

#El error se encuentra en '1984', que es tipo 'int'
#Lo arreglo transformando 'expresion' a 'str'

#Versión corregida:

def tiene_uno(expresion):
    expresion=str(expresion) #Pido que 'expresion' sea string
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#%%
#Ejercicio 3.8

#El error está en 'c' que es una variable local.
#Le agrego un return que me devuelva 'c' para poder usarla
#Versión corregida:

def suma(a,b):
    c = a + b
    return c 
a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
#Ejercicio 3.9


#El problema estaba en la asignación de la variable 'registro',
#se solucionó colocándola dentro del ciclo
#Resuelto
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={} #Defino el diccionario adentro del for
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
