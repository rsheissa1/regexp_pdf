#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 23:12:12 2022

@author: rsheissa
"""

import re


def lectura_linea(linea):
    
    #print(linea[0:4])
    
    #if linea[0:4] != "null":
    #linea1 = re.findall(r"([A-Z]*[\w]+[\S]+[A-Z]+[^\:])", linea)
    #linea2 = re.findall(r"([A-Z]+[0-9]+[A-Z]+[0-9]+)", linea)
    #linea3 = re.findall(r"[A-Z]*[a-z]*[0-9_\.-]*@[0-9a-z\.-]+\.[a-z]{2,6}", linea)
    #linea4 = re.findall(r"[a-z]+\://orcid.org/[0-9]+-[0-9]+-[0-9]+-[0-9]+", linea)
    linea5 = re.findall(r"[A-Z]*[a-z]*[\w]+[@a-z\.]*", linea)
    
    #if linea1:
            #print(f"Linea1: {linea1}")
    #    pass
        
    #if linea2:
            #print(f"Linea2: {linea2}")
    #    pass
        
    #if linea3:
            #print(f"Linea3: {linea3}")
    #    pass
        
    #if linea4:
            #print(f"Linea4: {linea4}")
    #    pass
    
    if linea5:
        tempo=""
        print(f"Linea5: {linea5}")
        for i in linea5:
            tempo = tempo + i + ","
            #datos1.write(i + ",")
        tempo = re.sub("\S$", "", tempo)
        datos1.write(tempo + "\n")
    #else:
        #print("Linea con valor null")
        #pass


if __name__ == "__main__":
    
    datos1 = open("produccion_filtrados.txt", "a")
    with open("produccion_cientifica.txt", "r", encoding='utf-8') as f:
        for line in f:
            lectura_linea(line)
    #print("prueba")
    datos1.close()
    f.close()