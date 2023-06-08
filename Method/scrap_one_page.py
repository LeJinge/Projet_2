import requests
from bs4 import BeautifulSoup


def scrap_one(booklink):
    page = requests.get(booklink)
    page.encoding = "utf-8"

    # Récupération de l'URL de la page
    product_page_url = page.url

    # Récupération des données de la page dans BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser')

    # Récupération du titre du livre
    title = soup.find("h1").string

    # Récupération du texte de description
    product_description = soup.find("div", {"id": "product_description"})
    if product_description is not None:
        product_description = product_description.find_next("p").string
    else:
        product_description = ''

    # Récupération de la catégorie
    category = soup.find("ul", {"class": "breadcrumb"}).find_all_next("a")

    # Récupération des données du tableau pour UPC, price_including_tax et price_excluding_tax
    data_table = []
    info_table = soup.find('table', {'class': 'table table-striped'})
    rows = info_table.find_all('tr')

    for row in rows:
        data = row.find_all('td')

        cell = data[0]
        data_table.append(cell.text)

    # Récupération review_rating
    rate_star = soup.find("p", {'class': 'star-rating'})

    rate = (rate_star['class'][1])

    # Récupération image_url
    image = soup.find("img")
    image = image['src']
    image_url = f"http://books.toscrape.com{image[5:]}"

    # Création dictionnaire pour résultat
    book = {

        "product_page_url": product_page_url,
        'universal_product_code(upc)': data_table[0],
        "title": title,
        'price_including_tax': data_table[2],
        'price_excluding_tax': data_table[3],
        'number_available': data_table[5],
        "product_description": product_description,
        "category": category[2].text,
        'review_rating': rate,
        'image_url': image_url
    }
    print(book["title"])
    print(book["price_including_tax"])
    return book
