import requests
import bs4
import lxml

# Lesson 1
result = requests.get("https://www.example.com/")
result.text
soup = bs4.BeautifulSoup(result.text,"lxml")

soup.select('title')[0].getText()

site_paragraphs = soup.select("p")

site_paragraphs[0].getText()
print(result)