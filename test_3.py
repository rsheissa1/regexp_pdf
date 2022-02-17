#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 21:59:40 2022

@author: rsheissa
"""
# Este programa lee datos filtrados del apartado Datos Generales del CVU
# Se estraen datos que serán guardados en la base de datos.
# Los datos se guardarán en una lista, que a su vez será vaciada en un archivo TXT para poder ser
# procesados por un progrma que lea y guarde estos datos en la base de datos correspondiente.



def lee_Fechas(lineaFecha):
    if lineaFecha[1] != "":
        listaDatos.append(lineaFecha[1])
    else:
        listaDatos.append("")
    if lineaFecha[5] != "":
        listaDatos.append(lineaFecha[5]+"/"+lineaFecha[6]+"/"+lineaFecha[7])
    else:
        listaDatos.append("")
    if lineaFecha[9] != "":
        listaDatos.append(lineaFecha[9])
    else:
        listaDatos.append("")

def lee_Nombre(lineaNombre):
    listaDatos.insert(0,lineaNombre[1])
    if lineaNombre[2] != "Primer":
        listaDatos.insert(1,lineaNombre[2])
        indice = 2
    else:
        indice = 1
    if lineaNombre[indice+3] != "":
        listaDatos.insert(indice,lineaNombre[indice+3])
    else:
        listaDatos.append("")
    if lineaNombre[indice+6] != "":
        listaDatos.insert(indice+1,lineaLista1[indice+6])
    else:
        listaDatos.append("")

def lee_DatosPersonales(lineaPersonal):
    listaDatos.append(lineaPersonal[1])
    listaDatos.append(lineaPersonal[4]+"("+lineaPersonal[5]+")")
    listaDatos.append(lineaPersonal[9])
    
def lee_NumCVU(lineaCvu):
    listaDatos.append(lineaCvu[2])
    listaDatos.append(lineaCvu[4])

def lee_Orcid(lineaOrcid):
    if lineaOrcid[2] != "null":
        listaDatos.append(lineaOrcid[2]+"://"+lineaOrcid[3]+"/"+lineaOrcid[4]+"-"+lineaOrcid[5]+"-"+lineaOrcid[6]+"-"+lineaOrcid[7])

listaDatos = []

if __name__ == "__main__":
    with open("generales_filtrados.txt", "r") as f:
        for line in f:
            lineaLimpia1 = line.strip('\n')
            lineaLista1 = lineaLimpia1.split(",")
            # Revisa si es el renglón donde se encuentra CURP, FechaNacimiento y RFC
            if lineaLista1[0] == "CURP":
                lee_Fechas(lineaLista1)
            # Revisa si es el renglón donde se encuentran los datos de NOMBRE, PRIMER APELLIDO y SEGUNDO APELLIDO
            if lineaLista1[0] == "Nombre" and len(lineaLista1) > 5:
                lee_Nombre(lineaLista1)
            # Revisa si es el renglón donde se encuentra Estado Civil y País de Nacimiento
            if lineaLista1[0] == "Sexo":
                lee_DatosPersonales(lineaLista1)
            # Revisa si es el renglón donde se encuentra entidad de nacimiento y Número de CVU
            if lineaLista1[0] == "Entidad" and lineaLista1[1] == "federativa":
                lee_NumCVU(lineaLista1)
            # Revisa si es el renglón del indicador ORCID
            if lineaLista1[0] == "ORC" and lineaLista1[1] == "ID":
                lee_Orcid(lineaLista1)
    
    print(listaDatos)

f.close()