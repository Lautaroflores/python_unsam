class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0



#torre de control

class TorreDeControl:

    def __init__(self):
        self.cola_arribos = Cola()
        self.cola_partidas = Cola()

    def nuevo_arribo(self, vuelo):
        self.cola_arribos.encolar(vuelo)    

    def nueva_partida(self, vuelo):
        self.cola_partidas.encolar(vuelo)

    def ver_estado(self):
        print('Vuelos esperando para aterrizar', self.cola_arribos.items)
        print('Vuelos esperando para despegar', self.cola_partidas.items)

    def asignar_pista(self):
        if not self.cola_arribos.esta_vacia():
            print('El vuelo', self.cola_arribos.desencolar(),"ha aterrizado con exito")
        elif not self.cola_partidas.esta_vacia():
            print('El vuelo', self.cola_partidas.desencolar(),"ha despegado con exito")
        else:
            print('No hay vuelos en espera.')