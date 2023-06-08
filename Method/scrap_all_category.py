import requests
from bs4 import BeautifulSoup

def scrap_all_category():
    home_page = requests.get("http://books.toscrape.com/index.html")

    soup = BeautifulSoup(home_page.text, "html.parser")

    category_links = []
    categories_url = soup.find("ul", {"class" : "nav nav-list"})


    categories_url = categories_url.find_next("li").find("ul").find_all("li")

    for category_url in categories_url:
        category_url = f"http://books.toscrape.com/{category_url.find('a')['href']}"
        category_links.append(category_url)


    return category_links