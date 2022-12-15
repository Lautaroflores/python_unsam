from collections import Counter 
#Abro el archivo
def abrir_archivo(nombre_archivo):
        lista = [] 
        with open(nombre_archivo, "rt", encoding='utf8') as f: 
            line=f.read()
            line=line.lower()
            line=line.replace('\n', '')
            line=line.replace(' ','')
            for palabra in line:#para cada palabra de cada linea
                for letra in palabra: #para cada letra de cada palabra
                    lista.append(letra)
        return lista


def counter(nombre_archivo, n): 
    contador = Counter(nombre_archivo).most_common(n)
    for item in contador:
        print(f'{item[0]} aparece {item[1]} veces') 


def main(nombre_archivo,n):
    archivo = abrir_archivo(nombre_archivo)
    contador= counter(archivo,n)
    return contador
nombre = main("ejercicio2 (1).txt",5)

if name == "main":
    import sys
    main(sys.argv[1], sys.argv[2])

    