# Se pueden remover espacios adicionales de cadenas utilizando
# re.sub()
# Módulos a usar: Regular Expressions (re), String

import re

# Se trabaja sobre un archivo en modo lectura, indicando el tipo
# de codicación como utf-8 para leer caracteres del alfabeto latino
# con esto se evitan que aparezcan "?" en el proceso de lectura.
# La lectura se realiza línea por línea.

line_Num = 0
check_list = ["1.","2.","3.","4.","5.","6.","7.","8.","9.","10."]
linea_1 = "Datos generales Grados Académicos Experiencia laboral"
linea_2 = "Domicilio de residencia"
linea_2a = "Domicilio de residencia Certificaciones Médicas Estancias de investigacion"
linea_3 = "Publicación de artículos Memorias Desarrollos tecnológicos"
linea_3a = "Otro"
linea_4 = "Publicación de libros Documentos de trabajo Innovación"
linea_5 = "Capítulos publicados Reseñas Desarrollo de software"
linea_6 = "Reportes técnicos Patentes"
linea_7 = "Programas en PNPC Programas en PNPC Diplomados"
linea_8 = "Programas no PNPC Programas no PNPC"
linea_9 = "Publicación de artículos Capítulos publicados Divulgación"
linea_10 = "Publicación de libros Participación en congresos"
linea_11 = "Redes Temáticas CONACYT Proyectos de investigación Evaluaciones CONACYT"
linea_12 = "Redes de investigación Grupos de investigación Evaluaciones no CONACYT"
linea_13 = "Distinciones CONACYT Idiomas"
linea_14 = "Distinciones no CONACYT"
linea_14a = "Distinciones no CONACYT Legunas indígenas"

def filtraTexto(archNom):
    
    filtrado = archNom.split(".")[0] + "_proc.txt"
    filt1 = open(filtrado, "w")

    with open(archNom, "r", encoding='utf-8') as f:
        for line in f:
            # Verifica si es la primera línea de texto leída.
            # En caso de ser cierto, verifica que sea del
            # CVU generado por CONACYT.
            # Si la comparación es VERDADERA, continúa con el
            # proceso de lectura.
            # Si la comparación es FALSA, termina la lectura e
            # indica un mensaje de error.
            # Remueve espacios al incio y final de la
            # línea. Es necesario dada la estructura del
            # documento CVU original.
            # Desde la página 1 hasta la última, cada página tiene
            # como enabezado CURRÍCULUM VITAE ÚNICO. Por lo tanto,
            # se omite para simplificar el proceso de parsing.

            res = line.strip()
            if res == "CURRÍCULUM VITAE ÚNICO":
                continue
            else:
                string2 = ""
                # Se remueven los espacios iniciales y finales de la
                # línea a leer.
                # Además se remueven espacios entre palabras que hacen
                # complicado el proceso. Se deja un espacio sencillo.
                res1 = re.sub(' +', ' ', res)
                # Si encuentra la palabra Página remueve de la línea
                if "Página" in res1:
                    res1 = re.sub(r"(Páginas de: [0-9]* a: [0-9]*)","", res1)
                    res1 = re.sub(r"(Página [0-9]* de [0-9]*)","", res1)
                # Para el caso de encontrar líneas en blanco, se omite
                # y continúa con la siguiente.
                if res1 == "":
                    continue
                # Desde la página 2 hasta la última, la primera línea
                # indica CURRÍCULUM VITAE ÚNICO. Por lo tanto,
                # se omite para simplificar el proceso de parsing.
                #if res1 == "CURRÍCULUM VITAE ÚNICO":
                #continue
                # Se omiten las líneas de la primera página del
                # documento. No son necesarias para el proceso de
                # captura en la base de datos.
                if res1[0:2] in check_list:
                    continue
                if res1 == linea_1 or res1 == linea_2 or res1 == linea_2a:
                    continue
                if res1 == linea_3 or res1 == linea_3a or res1 == linea_4:
                    continue
                if res1 == linea_5 or res1 == linea_6:
                    continue
                if res1 == linea_7 or res1 == linea_8:
                    continue
                if res1 == linea_9 or res1 == linea_10:
                    continue
                if res1 == linea_11 or res1 == linea_12:
                    continue
                if res1 == linea_13 or res1 == linea_14 or res1 == linea_14a:
                    continue
                for i in res1:
                    string2 = string2 + i
                        #string2 = string2.replace(':', '')
                filt1.write(string2 + '\n')

    filt1.close()
    f.close()
    return filtrado