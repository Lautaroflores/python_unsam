# rebotes.py
# Archivo de ejemplo
# Ejercicio
#Rebotes.py
altura = 100
num_rebotes = 0

while num_rebotes <= 10:
    print("rebote número:", num_rebotes, "altura:", round(altura, 4))
    num_rebotes = num_rebotes + 1
    altura = altura * (3/5)

#Resultado
""""
rebote número: 0 altura: 100 
rebote número: 1 altura: 60.0
rebote número: 2 altura: 36.0
rebote número: 3 altura: 21.6
rebote número: 4 altura: 12.96
rebote número: 5 altura: 7.776
rebote número: 6 altura: 4.6656
rebote número: 7 altura: 2.7994
rebote número: 8 altura: 1.6796
rebote número: 9 altura: 1.0078
rebote número: 10 altura: 0.6047
"""