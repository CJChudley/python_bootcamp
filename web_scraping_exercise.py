import requests
import bs4

# base_url = "http://quotes.toscrape.com/"
# res = requests.get(base_url)
# soup = bs4.BeautifulSoup(res.text,'lxml')

# authors_set = set()
# author_class = soup.select(".author")
# for item in author_class:
#     authors_set.add(item.text)

# quotes_list = list()
# quotes_class = soup.select(".text")
# for item in quotes_class:
#     quotes_list.append(item.text)

# tags_list = list()
# tags_class = soup.select(".tag-item")
# for item in tags_class:
#     tags_list.append(item.text)


base_url = "http://quotes.toscrape.com/page/{}"
page_num = 1
res = requests.get(base_url.format(page_num))
soup = bs4.BeautifulSoup(res.text,'lxml')
authors_set = set()

while "No quotes found" not in soup.select(".col-md-8")[1].text:
    author_class = soup.select(".author")
    for item in author_class:
        authors_set.add(item.text)

    page_num += 1
    res = requests.get(base_url.format(page_num))
    soup = bs4.BeautifulSoup(res.text,'lxml')



print("test")