import requests
import bs4
import lxml

# # Lesson 1
# result = requests.get("https://www.example.com/")
# result.text
# soup = bs4.BeautifulSoup(result.text,"lxml")

# soup.select('title')[0].getText()

# site_paragraphs = soup.select("p")

# site_paragraphs[0].getText()


# Lesson 2
# res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
# soup = bs4.BeautifulSoup(res.text,'lxml')
# soup.select(".vector-toc-numb")
# first_item = soup.select(".vector-toc-numb")[0]
# first_item.text

#  Lesson 3
res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text,'lxml')

soup.select('img')

computer = soup.select('.mw-file-element')[1]
computer['src']
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
image_link.content

f = open('my_computer_image.jpg','wb')

f.write(image_link.content)
f.close

print(computer)