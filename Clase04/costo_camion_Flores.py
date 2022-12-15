import csv

def costo_camion(archivo):
    total = 0

    with open(archivo, 'rt') as file:
        filas = csv.reader(file)
        encabezados = next(filas)
       
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                total+=ncajones * precio
            except ValueError:
                print(f'Fila {n_fila}: No puede interpretar {fila}')

    return total

costo = costo_camion('../Data/fecha_camion.csv')

print('Costo total: ', costo)