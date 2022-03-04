import PyPDF2 # Módulo para leer archivos PDF

# Funci�n que verifica si el documento fue creado por el sistema
# del CONACYT. En caso de no serlo, el valor ser� 0.
def verificaPDF(file):
    with open(file, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        pdf_producer = pdf_reader.getDocumentInfo()
        if "iText" in pdf_producer.producer:
            return 1
        else:
            return 0