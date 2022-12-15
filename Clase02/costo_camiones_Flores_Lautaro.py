import csv

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

costo = costo_camion('../Data/camion.csv')

print('Costo total: ', costo)