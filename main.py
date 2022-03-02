import PyPDF2

# Links para entrenar al clasificador
training_data = {
    "Ciencia": [
        'https://es.wikipedia.org/wiki/Ciencia',
        'https://es.wikipedia.org/wiki/Qu%C3%ADmica'
    ],
    "Deportes": [
        'https://es.wikipedia.org/wiki/Deporte',
        'https://es.wikipedia.org/wiki/Deportes_ol%C3%ADmpicos'
    ],
    "Tecnologia": [
        'https://es.wikipedia.org/wiki/Tecnolog%C3%ADa',
        'https://es.wikipedia.org/wiki/Rob%C3%B3tica'
    ],
}

dom = ""
clase = ""
pdf = input("Introduce el archivo pdf a clasificar\n")

pdFileobj = open(pdf, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdFileobj)
# Datos extraibles con PyPDF2
print("Cantidad de paginas: ", pdfReader.numPages)
print("Encriptado:  ", pdfReader.isEncrypted)
info = pdfReader.documentInfo
print("Fecha de creacion",info.get('/CreationDate'))
print("Fecha de modificacion",info.get('/ModDate'))
print("Creador",info.get('/Creator'))
#pageObj=pdfReader.getPage(0)
#print(pageObj.extractText())
for x in range(0,pdfReader.numPages):
    pageObj=pdfReader.getPage(x)
    print(pageObj.extractText())
# print("Dominio:  ",dom)
# print("Clase:    ",clase)
