#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 15:34:06 2022

@author: rsheissa
"""

#import string

def findline(word):
    #print(f"{word} en líneas: ")
    for i in range(len(arr)):
        if word in arr[i]:
            #print(f"line {i+1}, ")
            return i+1

if __name__ == "__main__":
    # READ FILE
    df = open("filtrado.txt")
    
    # read file
    read = df.read()
    
    # return cursor to
    # the beginning
    # of the file.
    df.seek(0)
    read
    
    # create empty list
    arr = []
    #arr1 = []
 
    # count number of
    # lines in the file
    line = 1
    for word in read:
        if word == '\n':
            line += 1
    
    #print("Number of lines in file is: ", line)
    
    for i in range(line):
        # readline() method,
        # reads one line at
        # a time
        arr.append(df.readline())
        #arr1.append(df.tell())
    
    # Busca la línea donde se encuentra la sección Datos generales
    dg = findline("Datos generales")
    print(f"dg = {dg} \n")
    # Busca la línea donde se encuentra la sección Formación académica
    fa = findline("Formación académica")
    print(f"fa = {fa} \n")
    # Busca la línea donde se encuentra la sección Trayectoria profesional
    tp = findline("Trayectoria profesional")
    print(f"tp = {tp} \n")
    # Busca la línea donde se encuentra la sección Producción científica, tecnológica y de innovación
    pc = findline("Producción científica, tecnológica y de innovación")
    print(f"pc = {pc} \n")
    # Busca la línea donde se encuentra la sección Formación de capital humano
    fc = findline("Formación de capital humano")
    print(f"fc = {fc} \n")
    # Busca la línea donde se encuentra la sección Lenguas e idiomas
    li = findline("Lenguas e idiomas")
    print(f"li = {li} \n")
    
    dg1 = open("datos_generales.txt", "w")
    for i in arr[dg:(fa-1)]:
        dg1.write(i)
    dg1.close()
    
    fa1 = open("formacion_academica", "w")
    for i in arr[fa:(tp-1)]:
        fa1.write(i)
    fa1.close()
    
    tp1 = open("trayectoria_profesional.txt", "w")
    for i in arr[tp:(pc-1)]:
        tp1.write(i)
    tp1.close()
    
    pc1 = open("produccion_cientifica.txt", "w")
    for i in arr[pc:(fc-1)]:
        pc1.write(i)
    pc1.close()
    
    fc1 = open("formacion_capital_humano.txt", "w")
    for i in arr[fc:(li-1)]:
        fc1.write(i)
    fc1.close()
    
    li1 = open("lenguas_idiomas.txt", "w")
    for i in arr[li:]:
        li1.write(i)
    li1.close()
    
    print()
    
    df.close()