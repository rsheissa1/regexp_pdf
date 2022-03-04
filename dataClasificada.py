#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 15:34:06 2022

@author: rsheissa
"""

# Función que separa las diversas secciones del CVU, guardándolas en archivos por separado.

def procSec(archLec):
    
    procesado = archLec.split(".")[0]

    def findline(word):
        #print(f"{word} en líneas: ")
        for i in range(len(arr)):
            if word in arr[i]:
                #print(f"line {i+1}, ")
                return i+1


    # Abre el archivo en modo lectura
    df = open(archLec,"r")
    
    # Lee el archivo
    read = df.read()
    
    # Regresa el cursor al inicio del archivo.
    df.seek(0)
    read
    
    # Inicializa una lista
    arr = []
 
    # Cuenta el número de líneas del archivo
    line = 1
    for word in read:
        if word == '\n':
            line += 1
    
    #print("Number of lines in file is: ", line)
    
    for i in range(line):
        # Utiliza el método readline(), para leear una línea a la vez
        arr.append(df.readline())
        
    # Busca la línea donde se encuentra la sección Datos generales
    dg = findline("Datos generales")
#    print(f"dg = {dg} \n")
    # Busca la línea donde se encuentra la sección Formación académica
    fa = findline("Formación académica")
#    print(f"fa = {fa} \n")
    # Busca la línea donde se encuentra la sección Trayectoria profesional
    tp = findline("Trayectoria profesional")
#    print(f"tp = {tp} \n")
    # Busca la línea donde se encuentra la sección Producción científica, tecnológica y de innovación
    pc = findline("Producción científica, tecnológica y de innovación")
#    print(f"pc = {pc} \n")
    # Busca la línea donde se encuentra la sección Formación de capital humano
    fc = findline("Formación de capital humano")
#    print(f"fc = {fc} \n")
    # Busca la línea donde se encuentra la sección Lenguas e idiomas
    li = findline("Lenguas e idiomas")
#    print(f"li = {li} \n")
    
    # Se crea una lista para guardar los nombres de los archivos
    # esto supone facilitar el seguimiento de los datos a procesar
    listArch = []
    
    # Datos generales se guardan en el archivo correspondiente
    datGen = procesado + "_dg.txt"
    listArch.append(datGen)
    dg1 = open(datGen, "w")
    for i in arr[dg:(fa-1)]:
        dg1.write(i)
    dg1.close()
    
    # Formación académica se guadan en el archivo correspondiente
    forAc = procesado + "_fa.txt"
    listArch.append(forAc)
    fa1 = open(forAc, "w")
    for i in arr[fa:(tp-1)]:
        fa1.write(i)
    fa1.close()
    
    # Trayectoria profesional se guarda en el archivo correspondiente
    trayPro = procesado + "_tp.txt"
    listArch.append(trayPro)
    tp1 = open(trayPro, "w")
    for i in arr[tp:(pc-1)]:
        tp1.write(i)
    tp1.close()
    
    # Producción científica se guarda en el archivo correspondiente
    prodCien = procesado + "_pc.txt"
    listArch.append(prodCien)
    pc1 = open(prodCien, "w")
    for i in arr[pc:(fc-1)]:
        pc1.write(i)
    pc1.close()
    
    # Formación de capital humano se guarda en el archivo correspondiente
    capHum = procesado + "_ch.txt"
    listArch.append(capHum)
    fc1 = open(capHum, "w")
    for i in arr[fc:(li-1)]:
        fc1.write(i)
    fc1.close()
    
    # Lenguas e idiomas se guardan en el archivo correspondiente
    lengIdiom = procesado + "_li.txt"
    listArch.append(lengIdiom)
    li1 = open(lengIdiom, "w")
    for i in arr[li:]:
        li1.write(i)
    li1.close()
    
    print()
    
    df.close()
    
    return listArch