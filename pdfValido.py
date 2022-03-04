import PyPDF2 # MÃ³dulo para leer archivos PDF

# Función que verifica si el documento fue creado por el sistema
# del CONACYT. En caso de no serlo, el valor será 0.
def verificaPDF(file):
    with open(file, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        pdf_producer = pdf_reader.getDocumentInfo()
        if "iText" in pdf_producer.producer:
            return 1
        else:
            return 0