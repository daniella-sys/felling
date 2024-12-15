import requests
from lxml import html
#Import libraries

#URL Web-pages
url = 'https://www.bbc.com/news'

#Send me NTML-code pages
response = requests.get(url) #Отримуємо посилання
html_content = response.content

#Парсинг NTML за допомогою lxml
tree = html.fromstring(html_content)

#Знаходження заголовків
news_headlines = tree.xpath('//h2[@class="news-title"]/text()')

#Вивід заголовків
for headline in news_headlines:
    print(headline)