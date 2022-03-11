import re
from collections import defaultdict
import requests
from bs4 import BeautifulSoup as bs4


def getWords(text):  # Obtenemos todo el texto y lo dividimos por palabras
    assert type(text) in (str, bytes)
    return [word for word in map(lambda x: x.lower(), re.findall("[a-z]{2,}", re.sub("https?://[^\s]+", "", text), re.I))]


def wordFreq(text):  # Claculamos la frecuencia con la cual se repite una palabra
    words = getWords(text)
    count = defaultdict(int)
    for word in words:
        count[word] += 1
    return count


def getPageContent(url):  # Función que devuelve todo el contenido HTML de una URL
    return requests.get(url).content


def html_to_text(html):
    return bs4(html, 'html.parser').get_text()


def getTextPage(url):  # Función para extraer todo el texto del contenido HTML de la pagina
    print("Aprendiendo de:", url)
    return  html_to_text(getPageContent(url))