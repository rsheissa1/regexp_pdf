#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 23:12:12 2022

@author: rsheissa
"""
# Función que realiza depuración de contenido
# Se considera un "filtrado" de datos para no dejar la menor cantidad de información
# innecesaria fuera del proceso.

import re


def lectura_linea(archRead):
    print(archRead)
    
    def proc_linea(linea):
        print(linea)
#        # Se utiliza una Expresión Regular para realizar el filtrado de datos inncesarios
#        linea5 = re.findall(r"[A-Z]*[a-z]*[\w]+[@a-z\.]*", linea)
#        
#        if linea5:
#            tempo=""
#            print(f"Linea5: {linea5}")
#            for i in linea5:
#                tempo = tempo + i + ","
#                #datos1.write(i + ",")
#                tempo = re.sub("\S$", "", tempo)
#                datos1.write(tempo + "\n")
#    
#    datos1 = open("produccion_cientifica_filtrados.txt", "a")
    with open("produccion_cientifica.txt", "r", encoding='utf-8') as f:
#        for line in f:
#            proc_linea(line)
#    
#    datos1.close()
#    f.close()