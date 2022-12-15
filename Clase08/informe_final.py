
import csv
from fileparse import parse_csv
import gzip

def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    with open(nombre_archivo, 'rt') as file:
        camion = parse_csv(file,select=['nombre', 'cajones', 'precio'],  types= [str, int, float],has_headers=True)


    return camion

def leer_precios(nombre_archivo): 
    with open(nombre_archivo, 'rt') as file:
        venta = parse_csv(file ,types=[str,float], has_headers=False)
        header = ['producto', 'precio'] # Asigno header
        precios = [dict(zip(header,ven)) for ven in venta]
 
    return precios

def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        precio_venta = precios[lote['nombre']]
        cambio = precio_venta - lote['precio']
        t = (lote['nombre'], lote['cajones'], lote['precio'], cambio)
        lista.append(t)
    return lista


def informe_camion(cam,prec):
     camion = leer_camion(cam)
     precios = leer_precios(prec)
     informe = hacer_informe(camion, precios)
  
     print('    Nombre    Cajones     Precio     Cambio')
     print('---------- ---------- ---------- ----------')
     for nombre, cajones, precio, cambio in informe:
         precio = f'${precio}'
         print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
     return camion, precios,informe
         

    
