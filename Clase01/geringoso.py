cadena = 'Geringoso'
capadepenapa = ''
for c in cadena:
    if c.lower() in 'aeiou':
        capadepenapa += c +'p'+ c
    else:
        capadepenapa +=c

print(capadepenapa)

#Resultado
#Geperipingoposopo