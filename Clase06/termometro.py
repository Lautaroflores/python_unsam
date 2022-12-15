# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 12:42:51 2022

@author: master
"""

import random
import statistics
import numpy as np
def resumen_temp(n):
    global temps
    temps = np.empty(n, dtype='float')
    importantes = []
    for i in range(n):
        x = round(random.normalvariate(37.5,0.2), 2)
        temps[i] = x
    importantes.append( [max(temps), min(temps),round(sum(temps)/len(temps), 2),round(statistics.median(temps), 2)])
    return temps, importantes

resumen = resumen_temp(30)
print(resumen)



np.save('C:/Users/master/Desktop/UNSAM/Programación I/Ejercicios/ejercicios_python/Data/temperaturas.npy', temps)