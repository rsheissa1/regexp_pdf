#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 01:21:29 2022

@author: rsheissa
"""

import os # Módulo del OS
import pdfValido # Módulo creado para validad un PDF CONACYT
import convPDF # Módulo para convertir PDF a TXT
import filtTxt # Módulo para remover datos no útiles
import borraLin # Módulo para filtrar datos
import dataClasificada # Módulo para guardar secciones del CVU en archivo
import procDG # Módulo de procesamiento Datos Generales


# El objetivo de este programa es leer un archivo en formato PDF, leer la información contenida en él,
# convertirla en formato TXT y procesarla para tener un formato adecuado a fin de guardarse en una
# base de datos.

# Ruta del directorio a procesar. La ruta ha sido fijada, sin embargo, puede modificarse el código para
# ser dinámica en tiempo de ejecución.
path = "/support/python/virtual_envs/test_code/regexp_pdf/cvu_referencia"


if __name__ == "__main__":
    # Se dirige al directorio indicado en la línea 17
    os.chdir(path)
    
    # Lectura de archivos en el directorio.
    # Únicamente serán procesados los archivos con extensión PDF y que hayan sido generados por
    # CONACYT.
    
    for file in os.listdir():
        procArch = path + "/" + file
        nombArch = os.path.basename(os.getcwd()+"/"+file).split(".")[0]
        # Verifica que existan archivos PDF
        if file.endswith(".pdf") or file.endswith(".PDF"):
            # Los archivos en formato CVU válido se procesan
            archVal = os.path.getsize(procArch)
            if archVal > 0:
                valido = pdfValido.verificaPDF(procArch)
                if valido == 0:
                    print(f"Arhivo {file} no fue generado por CONACYT")
                    next
                else:
                    archTxt = convPDF.cambiaPDF(procArch, nombArch)
                    archFilt = borraLin.filtraTexto(archTxt)
                    archLista = dataClasificada.procSec(archFilt)
                    dgFilt = filtTxt.lectura_linea(archLista[0]) # Se filtran datos del archivo Datos Generales
                    procDG.procDatosGen(dgFilt)
                    pcFilt = filtTxt.lectura_linea(archLista[3]) # Se filtran datos del archivo Producción Científica
            else:
                print(f"El archivo {file} está dañado o no es válido")
                next
        else:
            next