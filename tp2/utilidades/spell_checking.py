import requests
from bs4 import BeautifulSoup


def obtener_correccion(busqueda):
    url_def = "https://www.google.com/search?q="
    url_busqueda = url_def + busqueda
    pagina = requests.get(url_busqueda)

    soup = BeautifulSoup(pagina.text, "html.parser")
    correccion = soup.find(id='scc')

    if correccion is None:
        return busqueda
    return correccion.find('a').get_text()
