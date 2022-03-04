#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 21:59:40 2022

@author: rsheissa
"""

import re

# Este programa lee datos filtrados del apartado Producción Científica del CVU
# Se extraen datos que serán registrados en la base de datos.
# Serán guardados en una lista, que a su vez será vaciada en un archivo TXT para poder ser
# procesados por un progrma que lea y guarde estos datos en la base de datos correspondiente.

def procPublica(archLec):

    # Función que localiza la línea donde se encuentra la palabra deseada
    def findline(word,arr1):
        #print(f"arr length: {len(arr1)}")
        line = []
        for i in range(len(arr1)):
            #print(f"{arr1[i]}")
            if word in arr1[i]:
                #print(f"line {i+1}, ")
                line.append(i)
        
        return line
    
    # Función que encuentra la posición de palabras clave.
    # Retorna una lista con las posiciones deseadas, esto significa descartar dichas palabras
    # y así únicamente obtener los datos requeridos.
    def leePclave(arr1):
        indices = []
        for i in range(len(arr1)):
            if arr1[i] == "Palabra" and arr1[i+1] == "clave" and arr1[i+2] == "1":
                indices.append(i+3)
            if arr1[i] == "Palabra" and arr1[i+1] == "clave" and arr1[i+2] == "2":
                indices.append(i+3)
            if arr1[i] == "Palabra" and arr1[i+1] == "clave" and arr1[i+2] == "3":
                indices.append(i+3)
                return(indices)
    # Función que encuentra la posición de las palanras Área y Campo.
    # Retorna una lista de su poisición en la línea a procesar. Esto significa obtener
    # las palabras útiles para ser guardadas en la base de datos.
    def leeArea(arr1):
        indices = []
        for i in range(len(arr1)):
            if arr1[i] == "Área":
                indices.append(i)
            if arr1[i] == "Campo":
                indices.append(i)
                return(indices)
    
    # Similar a la función anterior. Encuentra la posición de las palabras Disciplina y Subdisciplina,
    # para ser descartadas y únicamente utilizar los datos útiles.            
    def leeDisciplina(arr1):
        indices = []
        for i in range(len(arr1)):
            if arr1[i] == "Disciplina":
                indices.append(i)
            if arr1[i] == "Subdisciplina":
                indices.append(i)
                return(indices)
                
    def leeCoatuores(arr1):
        pass

    # Función que procesa datos de artículos publicados
    def leeArticulo(arr1,linDatos):
        for i in range(len(linDatos)):
            listaDatos.append("articulo")
#            print("\n")
            if i+1 < len(linDatos):
                for j in range(linDatos[i]+1,linDatos[i+1]):
                    tempo = arr1[j].split(",")
                    # Verifica que tenga valores de ISSN impreso y/o electrónico
                    if tempo[0] == "ISSN":
                        if tempo[2] == "null":
                            listaDatos.append("N/A")
#                            print("N/A")
                            continue
                        else:
#                            print(tempo[2])
                            listaDatos.append(tempo[2])
                        if tempo[5] == "null":
                            listaDatos.append("N/A")
#                            print("N/A")
                            continue
                        else:
                            listaDatos.append(tempo[5])
#                            print(tempo[5])
                    # Verifica que esté capturado el nombre de la revista
                    if tempo[0] == "Nombre":
                        k = 1
                        tempo1 = tempo[k]
                        k = k + 1
                        while k < len(tempo):
                            tempo1 = tempo1 + " " + tempo[k]
                            k = k + 1
                        listaDatos.append(tempo1)
#                        print(tempo1)
                    # Verifica si está capturado el país de origen para la revista
                    if tempo[0] == "País":
                        if len(tempo) > 1:
                            k = 1
                            tempo1 = tempo[k]
                            k = k + 1
                            while k < len(tempo):
                                tempo1 = tempo1 + " " + tempo[k]
                                k = k + 1
                            listaDatos.append(tempo1)
#                            print(tempo1)
                        else:
                            listaDatos.append("N/A")
#                            print("N/A")
                            continue
                    # Verifica que tenga titulo del artículo capturado
                    if tempo[0] == "Título":
                        k = 3
                        tempo1 = tempo[k]
                        k = k + 1
                        while k < len(tempo):
                            tempo1 = tempo1 + " "+ tempo[k]
                            k = k + 1
                        listaDatos.append(tempo1)
#                        print(tempo1)
                    # Verifica número de revista y volumen
                    if tempo[0] == "Número":
                        if tempo[4] == "Volumen":
                            listaDatos.append("N/A")
                        else:
                            if tempo[4] == "" or tempo[4] == "null":
                                listaDatos.append("N/A")
                            else:
                                listaDatos.append(tempo[4])
                                if len(tempo) == 10:
                                    listaDatos.append(tempo[9])
                                if len(tempo) == 9:
                                    if tempo[8] == "revista":
                                        listaDatos.append("N/A")
                                    else:
                                        listaDatos.append(tempo[8])
                    # Verifica si tiene año de edición capturado
                    # También verifica si cuenta con año de publicación
                    if tempo[0] == "Año":
                        if tempo[3] == "Año":
                            listaDatos.append("N/A")
#                            print("N/A")
                            listaDatos.append(tempo[6])
#                            print(tempo[6])
                        else:
                            listaDatos.append(tempo[3])
#                            print(tempo[3])
                            listaDatos.append(tempo[7])
#                            print(tempo[7])
                    # Obtiene las palabras clave. En caso de no capturarse se
                    # registra como N/A
                    if tempo[0] == "Palabra":
                        test1 = leePclave(tempo)
                        if test1[0] != "" or test1[0] != "null":
                            test2 = " ".join(tempo[test1[0]:test1[1]-3])
                        else:
                            test2 = "N/A"
                        listaDatos.append(test2)
#                        print(test2)
                        if test1[1] != "" or test1[1] != "null":
                            test2 = " ".join(tempo[test1[1]:test1[2]-3])
                        else:
                            test2 = "N/A"
                        listaDatos.append(test2)
#                        print(test2)
                        if test1[2] != "" or test1[2] != "null":
                            test2 = " ".join(tempo[test1[2]:])
                        else:
                            test2 = "N/A"
                        listaDatos.append(test2)
#                        print(test2)
                    # Obtiene la información sobre Área y Campo del artículo
                    if tempo[0] == "Área":
                        if tempo[1] == "Campo":
                            continue
                        else:
                            test1 = leeArea(tempo)
                            test2 = ""
                            if tempo[1] != "" or tempo[1] != "null":
                                for k in range(test1[0]+1,test1[1]):
                                    test2 = test2 + " " + tempo[k]
                                test2 = test2.strip()
                            else:
                                test2 = "N/A"
                                listaDatos.append(test2)
#                        print(test2)
                            test2 = ""
                            if tempo[test1[1]+1] != "" or tempo[test1[1]+1] != "null":
                                for k in range(test1[1]+1,len(tempo)):
                                    test2 = test2 + " " + tempo[k]
                                test2 = test2.strip()
                            else:
                                test2 = "N/A"
                                listaDatos.append(test2)
#                        print(test2)
                    # Obtiene información sobre Disciplina y Subdisciplina
                    if tempo[0] == "Disciplina":
                        if tempo[1] == "Subdisciplina":
                            continue
                        else:
                            test1 = leeDisciplina(tempo)
                            test2 = ""
                            if tempo[1] != "" or tempo[1] != "null":
                                for k in range(test1[0]+1,test1[1]):
                                    test2 = test2 + " " + tempo[k]
                                test2 = test2.strip()
                            else:
                                test2 = "N/A"
                            listaDatos.append(test2)
#                        print(test2)
                            test2 = ""
                            if tempo[test1[1]+1] != "" or tempo[test1[1]+1] != "null":
                                for k in range(test1[1]+1,len(tempo)):
                                    test2 = test2 + " " + tempo[k]
                                test2 = test2.strip()
                            else:
                                test2 = "N/A"
                                listaDatos.append(test2)
#                        print(test2)
                    # Obtiene la información del (o los) autor(es)
                    if tempo[0] == "Coautor":
                        for k in range(j+1,linDatos[i+1]):
                            test1 = re.sub(r",[A-Z]+,[A-Z][a-z]+","",arr1[k])
                            test1 = re.sub(r",null","",test1)
                            test1 = test1.replace(",", " ")
                            listaDatos.append(test1)
#                            print(test1)
                        

    # Función que procesa datos de memorias publicadas
    def leeMemorias(arr1,linDatos):
        for i in range(len(linDatos)):
            listaDatos.append("memorias")
#            print("\n")
            if i+1 < len(linDatos):
                for j in range(linDatos[i]+1,linDatos[i+1]):
                    tempo = arr1[j].split(",")
                    # Verifica que contenga valores de Título de memoria
                    if tempo[0] == "Título" and tempo[3] == "memoria":
                        if tempo[4] == "":
                            listaDatos.append("N/A")
#                            print("N/A")
                        else:
                            k = 4
                            tempo1 = tempo[k]
                            k = k + 1
                            while k < len(tempo):
                                tempo1 = tempo1 + " "+ tempo[k]
                                k = k + 1
                            listaDatos.append(tempo1)
#                            print(tempo1)
                    # Verifica que contenga valores de Título de obra
                    if tempo[0] == "Título" and tempo[3] == "obra":
                        if len(tempo) <= 4:
                            listaDatos.append("N/A")
#                            print("N/A")
                            continue
                        else:
                            k = 4
                            tempo1 = tempo[k]
                            k = k + 1
                            while k < len(tempo):
                                tempo1 = tempo1 + " "+ tempo[k]
                                k = k + 1
                            listaDatos.append(tempo1)
#                            print(tempo1)
                    # Verifica que contenga valores en Autor de la obra
                    if tempo[0] == "Autor" and tempo[3] == "obra":
                        if len(tempo) <= 4:
                            listaDatos.append("N/A")
#                            print("N/A")
                            continue
                        if tempo[4] == "NO":
                            listaDatos.append("N/A")
#                            print("N/A")
                            continue
                        else:
                            k = 4
                            tempo1 = tempo[k]
                            k = k + 1
                            while k < len(tempo):
                                tempo1 = tempo1 + " "+ tempo[k]
                                k = k + 1
                            listaDatos.append(tempo1)
#                            print(tempo1)
                    # Verifica que contenga valores en Título de la publicación
                    if tempo[0] == "Título" and tempo[3] == "publicación":
                        if len(tempo) <= 4:
                            listaDatos.append("N/A")
#                            print("N/A")
                            continue
                        else:
                            k = 4
                            tempo1 = tempo[k]
                            k = k + 1
                            while k < len(tempo):
                                tempo1 = tempo1 + " "+ tempo[k]
                                k = k + 1
                            listaDatos.append(tempo1)
#                            print(tempo1)
                    # Verifica que contenga valores en Año de publicación
                    if tempo[0] == "Año" and tempo[2] == "publicación":
                        if len(tempo) <= 4:
                            listaDatos.append("N/A")
#                            print("N/A")
                            continue
                        else:
                            listaDatos.append(tempo[3])
#                            print(tempo[3])
                        if tempo[5] != "":
                            listaDatos.append(tempo[5])
#                            print(tempo[5])
                    
                    # Obtiene las palabras clave. En caso de no capturarse se
                    # registra como N/A
                    if tempo[0] == "Palabra":
                        test1 = leePclave(tempo)
                        if test1[0] != "" or test1[0] != "null":
                            test2 = " ".join(tempo[test1[0]:test1[1]-3])
                        else:
                            test2 = "N/A"
                        listaDatos.append(test2)
#                        print(test2)
                        if test1[1] != "" or test1[1] != "null":
                            test2 = " ".join(tempo[test1[1]:test1[2]-3])
                        else:
                            test2 = "N/A"
                        listaDatos.append(test2)
#                        print(test2)
                        if test1[2] != "" or test1[2] != "null":
                            test2 = " ".join(tempo[test1[2]:])
                        else:
                            test2 = "N/A"
                        listaDatos.append(test2)
#                        print(test2)
                    # Obtiene la información sobre Área y Campo del artículo
                    if tempo[0] == "Área":
                        test1 = leeArea(tempo)
                        test2 = ""
                        if tempo[1] != "" or tempo[1] != "null":
                            for k in range(test1[0]+1,test1[1]):
                                test2 = test2 + " " + tempo[k]
                            test2 = test2.strip()
                        else:
                            test2 = "N/A"
                        listaDatos.append(test2)
#                        print(test2)
                        test2 = ""
                        if tempo[test1[1]+1] != "" or tempo[test1[1]+1] != "null":
                            for k in range(test1[1]+1,len(tempo)):
                                test2 = test2 + " " + tempo[k]
                            test2 = test2.strip()
                        else:
                            test2 = "N/A"
                        listaDatos.append(test2)
#                        print(test2)
                    # Obtiene información sobre Disciplina y Subdisciplina
                    if tempo[0] == "Disciplina":
                        test1 = leeDisciplina(tempo)
                        test2 = ""
                        if tempo[1] != "" or tempo[1] != "null":
                            for k in range(test1[0]+1,test1[1]):
                                test2 = test2 + " " + tempo[k]
                            test2 = test2.strip()
                        else:
                            test2 = "N/A"
                        listaDatos.append(test2)
#                        print(test2)
                        test2 = ""
                        if tempo[test1[1]+1] != "" or tempo[test1[1]+1] != "null":
                            for k in range(test1[1]+1,len(tempo)):
                                test2 = test2 + " " + tempo[k]
                            test2 = test2.strip()
                        else:
                            test2 = "N/A"
                        listaDatos.append(test2)
#                        print(test2)
                    # Obtiene la información del (o los) autor(es)
                    if tempo[0] == "Participantes":
                        for k in range(j+1,linDatos[i+1]):
                            test1 = re.sub(r",[A-Z]+,[A-Z][a-z]+","",arr1[k])
                            test1 = re.sub(r",null","",test1)
                            test1 = test1.replace(",", " ")
                            listaDatos.append(test1)
#                            print(test1)
                    

    listaDatos = []
    

    # Abre el archivo para lectura
    df = open(archLec,"r")

    # Lee archivo
    read = df.read()
#        contenido = df.readlines()
    
    # Se posiciona el lector al inicio del archivo
    df.seek(0)
    read
    
    # Se crea una lista vacía para guardar las líneas del archivo
    arr = []
    # Se crea una lista vacía para guardar los números de línea de cada documento.
    # Únicamente se guardan las secciones no vacías
    secciones = []
    
    # Se cuentan los números de línea que contiene el archivo a procesar
    line = 1
    for word in read:
        if word == '\n':
            line += 1
    
    #print(f"Número de líneas en el archivo: ", line)
    
    for i in range(line):
        # Se utiliza método readline() method para leer una línea a la vez,
        # además se remueven los indicadores de nueva línea (\n)
        temp = df.readline()
        arr.append(temp.strip('\n'))
        
    
    # Busca las líneas donde se encuentran capturados artículos
    pub_art = findline("Publicación,de,artículos", arr)
#    print(f"Líneas artículos: {pub_art} \n")
    # Busca las líneas donde se encuentran capturados libros
    pub_lib = findline("Publicación,de,libros", arr)
#    print(f"Líneas libros: {pub_lib} \n")
    # Busca las líneas donde se encuentran capturados capítulos
    pub_cap = findline("Capítulos,publicados", arr)
#    print(f"Líneas capítulos: {pub_cap} \n")
    # Busca las líneas donde se encuentran capturados reportes técnicos
    pub_rep = findline("Reportes,técnicos", arr)
#    print(f"Líneas reportes: {pub_rep} \n")
    # Busca las líneas donde se encuentran capturadas memorias
    pub_mem = findline("Memorias", arr)
#    print(f"Líneas Memorias: {pub_mem} \n")
    # Busca las líneas donde se encuentran capturados documentos de trabajo
    pub_trab = findline("Documentos,de,trabajo", arr)
#    print(f"Líneas documentos de trabajo: {pub_trab} \n")
    # Busca las líneas donde se encuentran capturadas reseñas
    pub_res = findline("Reseñas", arr)
#    print(f"Líneas reseñas: {pub_res} \n")
    
    
    
    # Verifica que la categoría tenga al menos un elemento para procesar
    # Se guardan los números en una lista de listas
    # La identificación dentro de la lista es para realizar los ajustes de
    # lectura según sea el tipo.
    if pub_art:
        pub_art.insert(0,"articulos")
        secciones.append(pub_art)
    
    if pub_lib:
        pub_lib.insert(0,"libros")
        secciones.append(pub_lib)
    
    if pub_cap:
        pub_cap.insert(0,"capitulos")
        secciones.append(pub_cap)
    
    if pub_rep:
        pub_rep.insert(0,"reportes")
        secciones.append(pub_rep)
    
    if pub_mem:
        pub_mem.insert(0,"memorias")
        secciones.append(pub_mem)
    
    if pub_trab:
        pub_trab.insert(0,"trabajo")
        secciones.append(pub_trab)
    
    if pub_res:
        pub_res.insert(0,"reseña")
        secciones.append(pub_res)
        
        
    for i in range(len(secciones)):
        if i < (len(secciones)-1):
            secciones[i].append(secciones[i+1][1])
        else:
            secciones[i].append(line-1)

    # Se lee el primer componente de la lista de listas y se compara con las publicaciones a procesar
    for i in range(len(secciones)):
        if secciones[i][0] == 'articulos':
            leeArticulo(arr,secciones[i][1:len(secciones[i])])
        if secciones[i][0] == 'memorias':
            leeMemorias(arr,secciones[i][1:len(secciones[i])])

    
    procesado = archLec.split(".")[0]
    archSal = procesado + "_db.txt"            
    archivo_ordenado = open(archSal, "w")
    test1 = ",".join(listaDatos)
    archivo_ordenado.write(test1)

    archivo_ordenado.close()
    
    df.close()
