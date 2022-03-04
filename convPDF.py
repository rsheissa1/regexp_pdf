import pdftotext # Módulo de conversión PDF a TXT

# Función que realiza la conversión del formato PDF a TXT
def cambiaPDF(leeArch,escribArch):
    # El archivo PDF se abre para lectura
    with open(leeArch,  'rb') as f1:
        pdf = pdftotext.PDF(f1)

    # Archivo convertido se guarda con extensión TXT
    guarda = escribArch + ".txt"
    with open(guarda, 'w') as f2:
        f2.write("\n\n".join(pdf))

    f2.close()
    f1.close()
    return guarda