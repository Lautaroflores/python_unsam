from fileparse import parse_csv
import gzip
import lote
from costo_camion import Camion
import formato_tabla

def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    with open(nombre_archivo, 'rt') as file:
        camiondicts = parse_csv(file,select=['nombre', 'cajones', 'precio'],  types= [str, int, float],has_headers=True)
        camion =  [lote.Lote(d["nombre"], d["cajones"], d["precio"]) for d in camiondicts]


    return Camion(camion)

def leer_precios(nombre_archivo): 
    with open(nombre_archivo, 'rt') as file:
        venta = parse_csv(file ,types=[str,float], has_headers=False)
        header = ['producto', 'precio'] # Asigno header
        precios = [dict(zip(header,ven)) for ven in venta]
 
    return precios

def hacer_informe(camion, precios):
    lista = []
    for c in camion:
        precio_venta = precios[c.nombre]
        cambio = precio_venta - c.precio
        t = (c.nombre, c.cajones, c.precio, cambio)
        lista.append(t)
    return lista

def imprimir_informe(data_informe, formateador):
    
    formateador.encabezado(["Nombre", "Cantidad", "Precio", "Cambio"])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f"${precio:0.2f}", f"{cambio:0.2f}"]
        formateador.fila(rowdata)

def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es .txt
    Alternativas: .csv o .html
    '''
    # Lee archivos de datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Crea la data del informe
    data_informe = hacer_informe(camion, precios)

    # Imprime el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)
         
def f_principal(argumentos, fmt="txt"):
    # informe_camion(argumentos[1], argumentos[2], fmt)
    informe_camion("../Data/camion.csv", "../Data/precios.csv")


if __name__ == "__main__":
    import sys

    f_principal(sys.argv)

    
