def fruta(x):
    with open('../Data/precios.csv', 'rt') as file:
        for line in file:
            line = line.split(',')
            if x.lower() == line[0].lower():
                print(f'El precio de un cajón de {x} es ${line[1]}')
                return
        print(f'{x} no figura en el listado de precios')

fruta(input('Elegí la fruta: '))
