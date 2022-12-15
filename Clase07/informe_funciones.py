
# tabla_informe.py

from fileparse import parse_csv

def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    camion = parse_csv(nombre_archivo, types= [str, int, float],has_headers=True)
# =============================================================================
#     camion = []
# 
#     with open(nombre_archivo, 'rt') as f:
#         filas = csv.reader(f)
#         encabezados = next(filas)
#         
#         for n_fila, fila in enumerate(filas, start = 1):
#             record = dict(zip(encabezados, fila))
#             try:
#                 record['cajones'] = int(record['cajones'])
#                 record['precio'] = float(record['precio'])
#                 camion.append(record)
#             except ValueError:
#                 print('Faltan datos en la línea', n_fila, 'del archivo.')
# =============================================================================

    return camion

def leer_precios(nombre_archivo):
    precios  = dict(parse_csv(nombre_archivo, types = [str,float]))
# =============================================================================
#     precios = {}
#     with open(nombre_archivo, 'rt') as f:
#         rows = csv.reader(f)
#         for i, row in enumerate(rows):
#             
# #            try:
# #                precios[row[0]] = float(row[1])
# #            except IndexError:
# #                print('En la línea', i, 'faltan datos')
#             
#             if row: #### en vez del try-except se puede usar un if
#                 precios[row[0]] = float(row[1])
# =============================================================================
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

#informe_camion('../Data/camion.csv','../Data/precios.csv' )
         

    
