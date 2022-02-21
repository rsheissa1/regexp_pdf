#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 21:59:40 2022

@author: rsheissa
"""

# Este programa lee datos filtrados del apartado Producción Científica del CVU
# Se extraen datos que serán guardados en la base de datos.
# Los datos se guardarán en una lista, que a su vez será vaciada en un archivo TXT para poder ser
# procesados por un progrma que lea y guarde estos datos en la base de datos correspondiente.

def findline(word,arr1):
    #print(f"arr length: {len(arr1)}")
    line = []
    for i in range(len(arr1)):
        #print(f"{arr1[i]}")
        if word in arr1[i]:
            #print(f"line {i+1}, ")
            line.append(i+1)
    
    return line

if __name__ == "__main__":
    # READ FILE
    df = open("produccion_cientifica_filtrados.txt")
    
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
        temp = df.readline()
        arr.append(temp.strip('\n'))
        #arr.append(df.readline())
        #arr1.append(df.tell())
    
    #print(f"arr length: {len(arr)}")
    
    # Busca la línea donde se encuentra la sección Datos generales
    pub_art = findline("Publicación,de,artículos", arr)
    print(f"Líneas artículos: {pub_art} \n")
    # Busca la línea donde se encuentra la sección Formación académica
    pub_mem = findline("Memorias", arr)
    print(f"Líneas Memorias: {pub_mem} \n")
    
    #df.seek(121)
    print(arr[1])
    
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