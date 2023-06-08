import requests
from bs4 import BeautifulSoup


def scrap_one_category(categorylink):
    book_links = []
    while True:
        category_page = requests.get(categorylink)
        soup = BeautifulSoup(category_page.text, 'html.parser')
        books_url = soup.find_all('h3')
        for book_url in books_url:
            book_url = f"http://books.toscrape.com/catalogue/{book_url.find('a')['href'][9:]}"
            book_links.append(book_url)

        next = soup.find('li', {'class' : 'next'})
        if (next is not None):
            x = category_page.url.split("/")
            url_base = x[0] + "//" + x[2] + "/" + x[3] + "/" + x[4] + "/" + x[5] + "/" + x[6] + "/"
            categorylink = url_base + next.find('a')['href']
        else:
            return book_links