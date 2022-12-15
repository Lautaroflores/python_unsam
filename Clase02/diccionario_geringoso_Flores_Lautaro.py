def geringoso(lista):
    frutas = {}
    for fruta in lista:
        frutas[fruta] = ''
        for c in fruta:
            frutas[fruta] += c
            if c in 'aeiou':
                frutas[fruta]+= ( 'p' + c)
    
    return frutas

lista = ['banana', 'manzana','mandarina']
diccionario = geringoso(lista)
for fruta in lista:
    print (f'{fruta} en geringoso es: {diccionario[fruta]}')