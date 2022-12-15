#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 16:06:34 2022

@author: datascience
"""

import datetime as dt

def vida_en_segundos(fecha_nac):

    nacimiento=dt.datetime.strptime(fecha_nac, '%d/%m/%Y')

    print('nacimiento=', nacimiento)

    hoy= dt.datetime.now()
    print('hoy:',hoy)
    segundos_vividos=round((hoy-nacimiento).total_seconds(),2)
    return segundos_vividos


print(vida_en_segundos('24/02/2001'),'segundos totales')