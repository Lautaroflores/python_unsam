# -*- coding: utf-8 -*-
"""
Created on Fri Nov 8 19:26:08 2022

@author: master
"""
#Canguros buenos
class Canguro:

    def __init__(self, nombre, lista=[]):
        self.nombre = nombre
        self.lista = lista.copy()
        contenido = self.lista
        self.contenido_marsupio = contenido

    def meter_en_marsupio(self, lo_que_se_va_a_meter):
        self.contenido_marsupio.append(lo_que_se_va_a_meter)

    def __str__(self):
        return f'El canguro se llama {self.nombre} y tiene {self.lista}'


madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)
print(cangurito)

#%%
class Canguro:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = contenido.copy()#Corrijo
        
#Los elementos que se agreguen a Madre, se le agregaban tambien a 'gurito'


    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)


madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)
print(cangurito)
# Al ejecutar este código todo parece funcionar correctamente.
# Para ver el problema, imprimí el contenido de cangurito.
