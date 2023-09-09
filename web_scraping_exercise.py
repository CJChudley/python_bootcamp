import requests
import bs4


# extract the titles of all 
base_url = "http://books.toscrape.com/catalogue/page-{}.html"

# page_num = 1 # Loop 1-50


# res = requests.get(base_url.format(page_num))
# soup = bs4.BeautifulSoup(res.text,'lxml')

# products = soup.select(".product_pod")

# example = products[0]

# example.select(".star-rating.Two") ==[]

# example.select("a")[1]

# book_title = example.select("a")[1]["title"]

two_star_titles = []
for page_num in range(1,51):
    res = requests.get(base_url.format(page_num))
    soup = bs4.BeautifulSoup(res.text,'lxml')
    products = soup.select(".product_pod")
    for product in products:
        if product.select(".star-rating.Two") != []:
            two_star_titles.append(product.select("a")[1]["title"])



print(two_star_titles)