import csv
from pprint import pprint
 #FuncionCamion
#%%
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
    
camion = leer_camion('../Data/camion.csv')


total= 0.0
for s in camion:
    
    total += s['cajones']*s['precio']
            


#FuncionPrecio
#%%
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
#%%

#Calculo totales y clase 4
total2 = 0.0
cambio = [] 
for s in camion:
    
    nombre = s['nombre']
    cajon=s['cajones']
    price= s['precio']
    cambio_t = ()
    cambio_t=nombre, cajon, price, precios[s['nombre']]-s['precio']
    
    cambio.append(cambio_t)
    total2+= s['cajones']*precios[s['nombre']]
    

print('Costo camión: $',total)
print('Total venta: $', total2)
print ('Ganancia: $', round(total2-total, 2))



#Defino encabezados
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
header = []
header.append(headers)

#Barra separadora
barras = ['------']


def tabla_informe(x, z, barra):
    for a,b,c,d in z:
        print(f'{a:>10s}{b:>10s}{c:>10s}{d:>10s}')
        
    for bar in barra:
        print(f'{bar:>10s} {bar:>10s} {bar:>10s} {bar:>10s}')
    for nombre,cajon, price, cambio_v in x:
        print(f'{nombre:>10s}{cajon:>10d}     ${price:>.2f} {cambio_v:>10.2f}')
tabla_informe(cambio, header, barras) 