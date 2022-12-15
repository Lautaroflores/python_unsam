import sys
num_rebotes = 0
if len(sys.argv)==2:
    altura = float(sys.argv[1])
else: 
    altura = 100

while num_rebotes <= 10:
    print("rebote número:", num_rebotes, "altura:", round(altura, 4))
    num_rebotes = num_rebotes + 1
    altura = altura * (3/5)

