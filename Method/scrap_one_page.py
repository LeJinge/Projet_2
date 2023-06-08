import requests
from bs4 import BeautifulSoup


def scrap_one():
    page = requests.get("http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
    page.encoding = "utf-8"

    # Récupération de l'URL de la page
    product_page_url = page.url
