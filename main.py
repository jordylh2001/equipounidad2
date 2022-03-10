import PyPDF2
from StringClf import Classifier
from getPage import getTextPage

# Links para entrenar al clasificador

training_clas_data = {
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

training_dom_data = {
    "Handball": [
        'https://es.wikipedia.org/wiki/Ciencia',
        'https://es.wikipedia.org/wiki/Qu%C3%ADmica'
    ],
    "Basquetbol": [
        'https://es.wikipedia.org/wiki/Deporte',
        'https://es.wikipedia.org/wiki/Deportes_ol%C3%ADmpicos'
    ],
    "Futbol": [
        'https://es.wikipedia.org/wiki/Tecnolog%C3%ADa',
        'https://es.wikipedia.org/wiki/Rob%C3%B3tica'
    ],
}

dom = ""
pdf = input("Introduce el archivo pdf a clasificar\n")

pdFileObj = open(pdf, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdFileObj)

# Datos extraibles con PyPDF2
# print("Cantidad de paginas: ", pdfReader.numPages)
# print("Encriptado:  ", pdfReader.isEncrypted)
info = pdfReader.documentInfo
# print("Fecha de creacion",info.get('/CreationDate'))
# print("Fecha de modificacion",info.get('/ModDate'))
# print("Creador",info.get('/Creator'))
# pageObj=pdfReader.getPage(0)
# print(pageObj.extractText())

# Se encarga de imprimir el contenido de todas las paginas
# for x in range(0,pdfReader.numPages):
# pageObj=pdfReader.getPage(x)
# print(pageObj.extractText())

clf = Classifier()
for category, urls in training_clas_data.items():  # Entrenamos al clasificador de la clase con el contenido de cada pagina
    for url in urls:
        clf.train(getTextPage(url),
                  category)  # El metodo "getTextPage", recive como argumento una url para extraer su texto

clas = clf.String(info)
print("Clase:", clas)
# Resultados finales
# print("Dominio:  ",dom)
# print("Clase:    ",clase)
