# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 18:16:55 2022

@author: infolab
"""


import pandas as pd
import os

directorio = '../Data'
archivo1 = 'arbolado-en-espacios-verdes.csv'
fname1 = os.path.join(directorio,archivo1)
df_parques = pd.read_csv(fname1)


directorio = '../Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)
df_veredas = pd.read_csv(fname)
#Filtro por tipas y me quedo solo con las columnas que me pide
cols_sel =  ['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol']
df_tipas_veredas=df_veredas[df_veredas['nombre_cientifico']=='Tipuana tipu'][cols_sel].copy()
df_tipas_parques=df_parques[df_parques['nombre_cie']=='Tipuana Tipu'][['nombre_cie','altura_tot','diametro']].copy()

#Renombro columnas
df_tipas_parques=df_tipas_parques.rename(columns={'nombre_cie':'nombre_cientifico', 'altura_tot':'altura_arbol','diametro':'diametro_altura_pecho'})

#Agrego columna ambiente que identifique a que dataset pertenece cada arbol
df_tipas_parques['ambiente']='parque'
df_tipas_veredas['ambiente']='vereda'

#Junto los datasets
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

#Grafico diámetro
df_tipas.boxplot('diametro_altura_pecho',by = 'ambiente')
df_tipas.boxplot('altura_arbol',by = 'ambiente')


