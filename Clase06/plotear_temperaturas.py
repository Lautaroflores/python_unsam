# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 13:02:17 2022

@author: master
"""

import matplotlib.pyplot as plt
import  numpy as np

def plotear_temperaturas():
    temp= np. load('C:/Users/master/Desktop/UNSAM/Programación I/Ejercicios/ejercicios_python/Data/temperaturas.npy')
    plt.hist(temp, bins = 100)
    plt.show()
    
plotear_temperaturas()
