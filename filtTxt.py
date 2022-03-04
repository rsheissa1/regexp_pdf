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


def lectura_linea(archLec):
    
    def proc_linea(linea):
        
        # Se utiliza una Expresión Regular para realizar el filtrado de datos innecesarios
        linea5 = re.findall(r"[A-Z]*[a-z]*[\w]+[@a-z\.]*", linea)
        
        if linea5:
            tempo=""
#            print(f"Linea5: {linea5}")
            for i in linea5:
                tempo = tempo + i + ","
                #datos1.write(i + ",")
            tempo = re.sub("\S$", "", tempo)
            datos1.write(tempo + "\n")
    
    procesado = archLec.split(".")[0]
    archSal = procesado + "_filtrado.txt"
    datos1 = open(archSal, "a")
    with open(archLec, "r", encoding='utf-8') as f:
        for line in f:
            proc_linea(line)
    
    datos1.close()
    f.close()
    
    return archSal