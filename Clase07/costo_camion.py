from informe_funciones import leer_camion

import csv
def costo_camion(camion_csv):
    
    rows = leer_camion(camion_csv)
   
    
    total = 0.0
    
    for row in rows:
        total +=  row["cajones"] * row["precio"]
    return total

c = costo_camion("../Data/camion.csv")
print ("costo total:", c)

