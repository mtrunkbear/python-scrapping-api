from requests_html import HTMLSession
from bs4 import BeautifulSoup
from textblob import TextBlob
# import chromedriver_binary

import os
absolute_path = os.path.dirname(__file__)


def get_products(url="http://www.coolblue.nl/en/washer-dryer-combos/filter"):
    name = url.split("/")[4]
    # Crear una sesión de requests-html
    session = HTMLSession()
    # Hacer una solicitud GET para obtener el contenido HTML de la página web que contiene elementos con lazy loading
    # url = "http://www.coolblue.nl/en/washer-dryer-combos/filter"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    response = session.get(url, headers=headers)
    print(response)
    product_classname = "product-grid__card"

    # Desplazarse hacia abajo en la página web para cargar los elementos con lazy loading
    # response.html.render()
    # print(response.html.html)

    # Crear un objeto BeautifulSoup a partir del contenido HTML actualizado
    soup = BeautifulSoup(response.html.html, 'html.parser')

    # Buscar los elementos que necesitas utilizando las funciones de BeautifulSoup
    product_cards = soup.select("div[class*="+product_classname+"]")
    # images = product_cards.find_all('img')

    products = [dict() for card in product_cards]
    for i,  card in enumerate(product_cards):
        # Print image source
        if card.a:

            try:
                url = card.a["href"]

                session = HTMLSession()
                response = session.get("https://www.coolblue.nl"+url)
                soup = BeautifulSoup(response.html.html, 'html.parser')
                try:

                    description = soup.find(
                        id="product-information").select_one("div[class*=cms-content]").text

                    blob = TextBlob(description)
                    translated_text = blob.translate(from_lang="en", to='es')
                    description = str(translated_text)
                except Exception as e:
                    print(e)
                    pass
                print(description)

            except Exception as e:
                print(e)
                pass
        if card.find(class_="product-card__title"):

            try:
                title = card.find(class_="product-card__title").a["title"]
            except Exception:
                pass
        if card.strong:

            try:
                price = card.strong.text
            except Exception:
                pass
        if card.img:
            try:
                url_img = card.img["src"]
            except Exception:
                pass
            try:
                url_img = card.img["data-srcset"]
            except Exception:
                pass
            try:
                url_img = card.img["srcset"]
            except Exception:
                pass

        products[i] = {"title": title, "url_img": url_img,
                   "url": url, "price": price, "description": description or "not found"}
    return products
