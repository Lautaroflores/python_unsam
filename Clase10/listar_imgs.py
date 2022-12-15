#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:53:32 2022

@author: datascience
"""

import os
import sys


def archivos_png(archivo):
    lista=[]
    for root, dirs, files in os.walk(archivo):
       for name in files:
           if '.png' in name:
               lista.append(os.path.join(name))
       for name in dirs:
           if '.png' in name:
               lista.append(os.path.join(name))
    return lista
    

if __name__ == '__main__':
    print(archivos_png(sys.argv[1])) 
    