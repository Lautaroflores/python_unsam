import csv
from pprint import pprint
 #FuncionCamion
def leer_camion(nombre_archivo):
    
    camion = []
   
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        for n_row, row in enumerate(rows, start =1 ):
            record = dict(zip(headers, row))
            try:
                cajon={}
                cajon['nombre']=row[0]
                cajon['cajones']= int(record['cajones'])
                cajon['precio']=float(record['precio'])
                camion.append(cajon)
            except ValueError:
                print('none')
        
    return camion

camion = leer_camion('../Data/fecha_camion.csv')


total= 0.0
for s in camion:
    total += s['cajones']*s['precio']
            


#FuncionPrecio

def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        
        for row in rows:
            try:
                precios[row[0]]=float(row[1])
            except IndexError:
                print('')
    return precios

precios = leer_precios('../Data/precios.csv')


#Calculo totales
total2 = 0.0
for s in camion:
    total2+= s['cajones']*precios[s['nombre']]
print('Costo camión: $',total)
print('Total venta: $', total2)
print ('Ganancia: $', round(total2-total, 2))

