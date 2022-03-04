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

# Función que procesa datos de artículos
def leeArticulo(arr1,linDatos):
    for i in range(len(linDatos)):
        print("\n")
        if i+1 < len(linDatos):
            for j in range(linDatos[i]+1,linDatos[i+1]):
                tempo = arr1[j].split(",")
                # Verifica que tenga valores de ISSN impreso y/o electrónico
                if tempo[0] == "ISSN":
                    if tempo[2] == "null":
                        print("N/A")
                    else:
                        print(tempo[2])
                    if tempo[5] == "null":
                        print("N/A")
                    else:
                        print(tempo[5])
                # Verifica que esté capturado el nombre de la revista
                if tempo[0] == "Nombre":
                    k = 1
                    tempo1 = tempo[k]
                    k = k + 1
                    while k < len(tempo):
                        tempo1 = tempo1 + " " + tempo[k]
                        k = k + 1
                    print(tempo1)
                # Verifica si está capturado el país de origen para la revista
                if tempo[0] == "País":
                    if len(tempo) > 1:
                        k = 1
                        tempo1 = tempo[k]
                        k = k + 1
                        while k < len(tempo):
                            tempo1 = tempo1 + " " + tempo[k]
                            k = k + 1
                        print(tempo1)
                    else:
                        print("N/A")
                # Verifica que tenga titulo del artículo capturado
                if tempo[0] == "Título":
                    k = 3
                    tempo1 = tempo[k]
                    k = k + 1
                    while k < len(tempo):
                        tempo1 = tempo1 + " "+ tempo[k]
                        k = k + 1
                    print(tempo1)
                # Verifica número de revista y volumen
                if tempo[0] == "Número":
                    if tempo[4] != "" and tempo[4] != "null":
                        print(tempo[4])
                    else:
                        print("N\A")
                    if tempo[9] != "" and tempo[9] != "null":
                        print(tempo[9])
                    else:
                        print("N\A")
                # Verifica si tiene año de edición capturado
                # También verifica si cuenta con año de publicación
                if tempo[0] == "Año":
                    if tempo[3] == "Año":
                        print("N/A")
                        print(tempo[6])
                    else:
                        print(tempo[3])
                        print(tempo[7])
                # Obtiene las palabras clave. En caso de no capturarse se
                # registra como N/A
                if tempo[0] == "Palabra":
                    test1 = leePclave(tempo)
                    if test1[0] != "" or test1[0] != "null":
                        test2 = " ".join(tempo[test1[0]:test1[1]-3])
                    else:
                        test2 = "N/A"
                    print(test2)
                    if test1[1] != "" or test1[1] != "null":
                        test2 = " ".join(tempo[test1[1]:test1[2]-3])
                    else:
                        test2 = "N/A"
                    print(test2)
                    if test1[2] != "" or test1[2] != "null":
                        test2 = " ".join(tempo[test1[2]:])
                    else:
                        test2 = "N/A"
                    print(test2)
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
                    print(test2)
                    test2 = ""
                    if tempo[test1[1]+1] != "" or tempo[test1[1]+1] != "null":
                        for k in range(test1[1]+1,len(tempo)):
                            test2 = test2 + " " + tempo[k]
                        test2 = test2.strip()
                    else:
                        test2 = "N/A"
                    print(test2)
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
                    print(test2)
                    test2 = ""
                    if tempo[test1[1]+1] != "" or tempo[test1[1]+1] != "null":
                        for k in range(test1[1]+1,len(tempo)):
                            test2 = test2 + " " + tempo[k]
                        test2 = test2.strip()
                    else:
                        test2 = "N/A"
                    print(test2)
                if tempo[0] == "Coautor":
                    for k in range(j+1,linDatos[i+1]):
                        test1 = re.sub(r",[A-Z]+,[A-Z][a-z]+","",arr1[k])
                        test1 = re.sub(r",null","",test1)
                        test1 = test1.replace(",", " ")
                        print(test1)
                    #test1 = ','.join(map(str,tempo))
                    #test2=[]
                    #test2 = re.sub(r"Palabra,[a-z]+,[0-9],", "", test1)
                    #print(test1)


if __name__ == "__main__":
    # Abre el archivo para lectura
    df = open("produccion_cientifica_filtrados.txt")
    
    # Se lee el archivo
    read = df.read()
    contenido = df.readlines()
    
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
    print(f"Líneas artículos: {pub_art} \n")
    # Busca las líneas donde se encuentran capturados libros
    pub_lib = findline("Publicación,de,libros", arr)
    print(f"Líneas libros: {pub_lib} \n")
    # Busca las líneas donde se encuentran capturados capítulos
    pub_cap = findline("Capítulos,publicados", arr)
    print(f"Líneas capítulos: {pub_cap} \n")
    # Busca las líneas donde se encuentran capturados reportes técnicos
    pub_rep = findline("Reportes,técnicos", arr)
    print(f"Líneas reportes: {pub_rep} \n")
    # Busca las líneas donde se encuentran capturadas memorias
    pub_mem = findline("Memorias", arr)
    print(f"Líneas Memorias: {pub_mem} \n")
    # Busca las líneas donde se encuentran capturados documentos de trabajo
    pub_trab = findline("Documentos,de,trabajo", arr)
    print(f"Líneas documentos de trabajo: {pub_trab} \n")
    # Busca las líneas donde se encuentran capturadas reseñas
    pub_res = findline("Reseñas", arr)
    print(f"Líneas reseñas: {pub_res} \n")
    
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
    
    
    
    #df.seek(12797)
    #read1 = df.readline()
    #temp1 = arr[13]
    #print(temp1.replace("Correo / Teléfono", "Correo/Teléfono"))
    #print("\n")
    #print(temp1.split())
    
#    dg1 = open("datos_generales.txt", "w")
#    for i in arr[dg:(fa-1)]:
#        dg1.write(i)
#    dg1.close()
#    
#    fa1 = open("formacion_academica", "w")
#    for i in arr[fa:(tp-1)]:
#        fa1.write(i)
#    fa1.close()
#    
#    tp1 = open("trayectoria_profesional.txt", "w")
#    for i in arr[tp:(pc-1)]:
#        tp1.write(i)
#    tp1.close()
#    
#    pc1 = open("produccion_cientifica.txt", "w")
#    for i in arr[pc:(fc-1)]:
#        pc1.write(i)
#    pc1.close()
#    
#    fc1 = open("formacion_capital_humano.txt", "w")
#    for i in arr[fc:(li-1)]:
#        fc1.write(i)
#    fc1.close()
#    
#    li1 = open("lenguas_idiomas.txt", "w")
#    for i in arr[li:]:
#        li1.write(i)
#    li1.close()
#    
#    print()
    
    df.close()


#def lee_Fechas(lineaFecha):
#    if lineaFecha[1] != "":
#        listaDatos.append(lineaFecha[1])
#    else:
#        listaDatos.append(" ")
#    if lineaFecha[5] != "":
#        listaDatos.append(lineaFecha[5]+"/"+lineaFecha[6]+"/"+lineaFecha[7])
#    else:
#        listaDatos.append(" ")
#    if lineaFecha[9] != "":
#        listaDatos.append(lineaFecha[9])
#    else:
#        listaDatos.append(" ")
#
#def lee_Nombre(lineaNombre):
#    listaDatos.insert(0,lineaNombre[1])
#    if lineaNombre[2] != "Primer":
#        listaDatos.insert(1,lineaNombre[2])
#        indice = 2
#    else:
#        indice = 1
#    if lineaNombre[indice+3] != "":
#        listaDatos.insert(indice,lineaNombre[indice+3])
#    else:
#        listaDatos.append(" ")
#    if lineaNombre[indice+6] != "":
#        listaDatos.insert(indice+1,lineaLista1[indice+6])
#    else:
#        listaDatos.append(" ")
#
#def lee_DatosPersonales(lineaPersonal):
#    listaDatos.append(lineaPersonal[1])
#    listaDatos.append(lineaPersonal[4]+"("+lineaPersonal[5]+")")
#    listaDatos.append(lineaPersonal[9])
#    
#def lee_NumCVU(lineaCvu):
#    listaDatos.append(lineaCvu[2])
#    listaDatos.append(lineaCvu[4])
#
#def lee_Orcid(lineaOrcid):
#    listaDatos.append(lineaOrcid[2]+"://"+lineaOrcid[3]+"/"+lineaOrcid[4]+"-"+lineaOrcid[5]+"-"+lineaOrcid[6]+"-"+lineaOrcid[7])
#        
#def lee_Direccion(lineaDireccion):
#    i = 4
#    
#    tempo1 = lineaDireccion[i]
#    i = i+1
#    while i < len(lineaDireccion):
#        if lineaDireccion[i] == "Municipio":
#            i = i + 3
#            break
#        else:
#            tempo1 = tempo1 + " " + lineaDireccion[i]
#            i = i + 1
#            
#    tempo2 = lineaDireccion[i]
#    i = i + 1
#    while i < len(lineaDireccion):
#        tempo2 = tempo2 + " "+ lineaDireccion[i]
#        i = i+1
#        
#    listaDatos.append(tempo1)
#    listaDatos.append(tempo2)
#
#def lee_CP(lineaCp):
#    i=1
#    
#    tempo1 = lineaCp[i]
#    i = i+1
#    while i < len(lineaCp):
#        if lineaCp[i] == "Código":
#            i = i + 2
#            break
#        else:
#            tempo1 = tempo1 + " " + lineaCp[i]
#            i = i + 1
#    
#    listaDatos.append(tempo1)
#    listaDatos.append(lineaCp[i])
#    
#    #print(i)
#
#def lee_Asentamiento(lineaAsentamiento):
#    tempo1 = lineaAsentamiento[1] + "-"
#    for i in range(2,len(lineaAsentamiento)):
#        tempo1 = tempo1 + " " + lineaAsentamiento[i]
#    
#    listaDatos.append(tempo1)
#    
#def lee_Vialidad(lineaVialidad):
#    tempo1 = lineaVialidad[0]
#    for i in range(1,len(lineaVialidad)):
#        tempo1 = tempo1 + " " + lineaVialidad[i]
#    
#    listaDatos.append(tempo1)
#    
#def lee_Exterior(lineaExterior):
#    if lineaExterior[4] != "":
#        listaDatos.append(lineaExterior[4])
#    
#    if lineaExterior[7] != "":
#        listaDatos.append(lineaExterior[7])
#    
#
#listaDatos = []
#banderaVialidad = 0
#
#if __name__ == "__main__":
#    with open("generales_filtrados.txt", "r") as f:
#        for line in f:
#            lineaLimpia1 = line.strip('\n')
#            lineaLista1 = lineaLimpia1.split(",")
#            # Revisa si es el renglón donde se encuentra CURP, FechaNacimiento y RFC
#            if lineaLista1[0] == "CURP":
#                lee_Fechas(lineaLista1)
#            # Revisa si es el renglón donde se encuentran los datos de NOMBRE, PRIMER APELLIDO y SEGUNDO APELLIDO
#            if lineaLista1[0] == "Nombre" and len(lineaLista1) > 5:
#                lee_Nombre(lineaLista1)
#            # Revisa si es el renglón donde se encuentra Estado Civil y País de Nacimiento
#            if lineaLista1[0] == "Sexo":
#                lee_DatosPersonales(lineaLista1)
#            # Revisa si es el renglón donde se encuentra entidad de nacimiento y Número de CVU
#            if lineaLista1[0] == "Entidad" and lineaLista1[1] == "federativa":
#                lee_NumCVU(lineaLista1)
#            # Revisa si es el renglón del indicador ORCID
#            if lineaLista1[0] == "ORC" and lineaLista1[1] == "ID":
#                if lineaLista1[2] != "null":
#                    lee_Orcid(lineaLista1)
#                else:
#                    listaDatos.append(" ")
#            # Revisa los datos de residencia, en caso de que se hayan capturado en el CVU
#            if lineaLista1[0] == "Estado" and lineaLista1[2] == "distrito":
#                if lineaLista1 != "null":
#                    lee_Direccion(lineaLista1)
#            # Revisa datos de residencia, Localidad y Código Postal
#            if lineaLista1[0] == "Localidad":
#                lee_CP(lineaLista1)
#            # Revisa datos de Asentamiento
#            if lineaLista1[0] == "Asentamiento":
#                lee_Asentamiento(lineaLista1)
#            # Revisa si existe el apartado Nombre de vialidad, si existe banderaVialidad = 1
#            if lineaLista1[0] == "Nombre" and len(lineaLista1) > 1 and lineaLista1[2] == "vialidad" and banderaVialidad == 0:
#                banderaVialidad = 1
#                next
#            else:
#                if banderaVialidad == 1:
#                    lee_Vialidad(lineaLista1)
#                    banderaVialidad = 2
#            # Revisa si existen datos del número exterior del domicilio
#            if lineaLista1[0] == "Número" and lineaLista1[1] == "exterior":
#                lee_Exterior(lineaLista1)
#                
#                
#    archivo_ordenado = open("datos_personales_db.txt", "w")
#    test1 = ",".join(listaDatos)
#    archivo_ordenado.write(test1)
#
#    archivo_ordenado.close()    
#
#    f.close()