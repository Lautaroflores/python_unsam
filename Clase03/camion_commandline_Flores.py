import csv
import sys
def costo_camion(archivo):
    total = 0

    with open(archivo, 'rt') as file:
        filas = csv.reader(file)
        next(filas)
        for fila in filas:
            try:
                total+=int(fila[1])*float(fila[2])
            except ValueError:
                print('try again')

    return total

if len(sys.argv) == 2:
    archivo = sys.argv[1]
else:
    archivo = '../Data/camion.csv'

costo = costo_camion(archivo)

print('Costo total: ', costo)