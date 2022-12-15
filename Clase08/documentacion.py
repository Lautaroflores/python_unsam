def valor_absoluto(n):
    '''
    Devuelve el valor absoluto de n (|n|) 
    Precondición: n es un valor real
    Poscondición: n positivo
    '''

    if n >= 0:
        return n
    else:
        return -n
#%%
def suma_pares(l):
    '''
    Suma los valores pares de una lista
    Precondición: lista con valores reales
    Poscondición: suma de los numeros pares de la lista
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res
#res = 0 es invariante
#%%
def veces(a, b):
    '''
    Multiplico a y b
    Precondición: a es un número real, b es un valor entero
    Poscondición: Producto entre a y b
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res
#res = 0 es invariante
#%%
def collatz(n):
    '''
    Devuelve el numero de operaciones que se realizan para que
    el número ingresado llegue a 1
    Precondición: n entero positivo
    Poscondición: Cantidad de repeticiones del bucle
    '''
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res
#res = 1 es invariante