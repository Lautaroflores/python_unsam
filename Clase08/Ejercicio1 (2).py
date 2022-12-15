#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Ejercicio 1. Interpretar lo que quiso hacer lx programadorx y corregir los dos bugs 
#Obs: Se puede resolver modificando solo unos pocos caracteres.
#Obs: Va a tener que explicar por qué fallaba y por qué lo resolvió así.


def geringosar(palabra):
    traduccion = ''
    l = len(palabra)
    for i in range(l-1):
        c = palabra [i]
        if c in 'aeiou':
            traduccion = traduccion + c + 'p' + c
        else:
            traduccion = traduccion + c
    
    return traduccion
        

palabra = "camion"
print(palabra)
print (geringosar(palabra))

palabra = "Abecedario"
print(palabra)
print (geringosar(palabra))

palabra = "Alcachofa"
print(palabra)
print (geringosar(palabra))

palabra = "manzana"
print(palabra)
print (geringosar(palabra))

