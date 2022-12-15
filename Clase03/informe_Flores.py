import csv
from pprint import pprint
 #FuncionCamion
def leer_camion(nombre_archivo):
    
    camion = []
   
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        for row in rows:
            try:
                cajon={}
                cajon['nombre']=row[0]
                cajon['cajones']=int(row[1])
                cajon['precio']=float(row[2])
                camion.append(cajon)
            except ValueError:
                print('none')
        
    return camion

camion = leer_camion('../Data/camion.csv')

pprint(camion)
total= 0.0
for s in camion:
    total += s['cajones']*s['precio']
            
print(total)

#FuncionPrecio

def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        
        for row in rows:
            try:
                precios[row[0]]=float(row[1])
            except IndexError:
                print('none')
    return precios

precios = leer_precios('../Data/precios.csv')


pprint(precios)

#Calculo totales
total2 = 0.0
for s in camion:
    total2+= s['cajones']*precios[s['nombre']]
print('Costo camión: $',total)
print('Total venta: $', total2)
print ('Ganancia: $', round(total2-total, 2))

