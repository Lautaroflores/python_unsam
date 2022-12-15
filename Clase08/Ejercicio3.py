def minimo(lista):
    '''Devuelve el minimo de una lista, 
    la lista debe ser no vacía.
    '''
    # m guarda el mínimo de los elementos a medida que recorro la lista. 
    m = lista[0] # Lo inicializo en el primer elemento de lista
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e < m:
            m = e
    return m

def invertir_lista(lista):
    '''
    Devuelve la lista invertida.
    '''
    invertida = []
    for i in range(len(lista), 0, -1): # Recorro la lista
        invertida.append(lista[i - 1])
    return invertida

def busqueda_con_index(lista, e):
    '''Busca un elemento e en la lista.

    Si e está en lista devuelve el índice,
    de lo contrario devuelve -1.
    '''
    if e in lista:
        pos = lista.index(e)
    else:
        pos = -1
    return pos


class Ordenador:
    def __init__(self, nombre_archivo = None):
        if nombre_archivo:
            with open(nombre_archivo, 'rt') as file:
                data = file.read()
                lis = [int(num) for num in data.split(',')]
                
            self.lis = lis
        
    def leer_archivo(self, nombre_archivo):
        '''
        Lee el archivo dado y almacena su contenido en el objeto
        
        Precondiciones: Se debe pasar un nombre de archivo válido y este debe contener numeros separados
        por comas.
        '''
        with open(nombre_archivo, 'rt') as file:
            data = file.read()
            lis = [int(num) for num in data.split(',')]
            
        self.lis = lis
    
    def ordenar(self, desc = False):
        '''
        Ordena la lista de forma ascendente o descendente. 
        La forma predeterminada es ascendente, se puede especificar orden descendente 
        pasando True al parametro desc
        
        Precondiciones: Se debe haber utilizado leer_archivo() con anterioridad para
        tener una lista que odenar.
        '''
        lis_temp = self.lis.copy()
        lis_ord = []
        for i in range(len(self.lis)):
            min_index = busqueda_con_index(lis_temp, minimo(lis_temp))
            lis_ord.append(lis_temp.pop(min_index))
            
        if desc:
            lis_ord = invertir_lista(lis_ord)
            
        self.lis = lis_ord
        
    def imprimir(self):
        for num in self.lis:
            print(num)
            
    def __str__(self):
        return '\n'.join([str(num) for num in self.lis])

def main(parametros):
    nombre_archivo = parametros[1]
    lista = Ordenador()
    lista.leer_archivo(nombre_archivo)
    
    if len(parametros) == 3:
        if parametros[2] == 'a':
            ord = False
        elif parametros[2] == 'd':
            ord = True
            
        lista.ordenar(ord)
    else:
        lista.ordenar()
    
    #lista.imprimir()
    print(lista)
   
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'nombre_archivo orden (a = ascendente, d = descendiente. Es opcional y si no se especifica el orden será ascendente)')
    main(sys.argv)
    
    
'python3 Ejercicio2.py Ejercicio2.txt d'

'python3 Ejercicio2.py Ejercicio2.txt a'