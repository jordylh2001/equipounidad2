import PyPDF2
from StringClf import Classifier
from Info import getTextPage

# Links para entrenar al clasificador de dominio

training_dom_data = {
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
        'https://es.wikipedia.org/wiki/Rob%C3%B3tica'
    ],
}

#Links para entrenar al clasificador de clases
training_clas_data = {
    "Futbol": [
        'https://es.wikipedia.org/wiki/F%C3%BAtbol',
        'https://www.euston96.com/futbol/'
    ],
    "Tenis": [
        'https://es.wikipedia.org/wiki/Tenis'
    ],
    "Basquetbol":[
        'https://es.wikipedia.org/wiki/Baloncesto'
    ]

}

#Se le soilicta el documento a clasificar
pdf = input("Introduce el archivo pdf a clasificar\n")

pdFileObj = open(pdf, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdFileObj, strict=False)

# Datos extraibles con PyPDF2
info = pdfReader.documentInfo
text=""
#Obtenemos toda la informacion dentro del pdf es decir
#junto con urls y demas
for x in range(0, pdfReader.numPages):
    pageObj = pdfReader.getPage(x)
    #Utilizar el siguiente print en caso de error para ver si no esta encriptado el pdf

    #print(pageObj.extractText())
    text = pageObj.extractText()

#Empezamos con el clasificador de dominio y lo entrenamos
clf = Classifier()
for category, urls in training_dom_data.items():
    for url in urls:
        #Se encarga de obtener el contenido del URL
        clf.train(getTextPage(url),
                  category)

#Obtenemos el dominio del texto del pdf
dom = clf.String(text)

#Empezamos con el clasificador de dominio y lo entrenamos
clf2 = Classifier()
for category, urls in training_clas_data.items():
    for url in urls:
        # Se encarga de obtener el contenido del URL
        clf2.train(getTextPage(url),
                  category)

#Obtenemos la clase del texto del pdf
clas = clf2.String(text)

#Imprimimos los resultados
print("Dominio:", dom)
print("Clas:", clas)

