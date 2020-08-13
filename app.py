from urllib.request import urlretrieve
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

search = input('어떤 사진을 원하느냐: ')
url = f'https://www.google.com/search?q={quote_plus(search)}'

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

img = soup.select("rg_i Q4LuWd")
n = 1
imgUrl = []

for i in img:
    try:
        imgUrl.append(i.atttrs["src"])
    except KeyError:
        imgUrl.append(i.atttrs['data-src'])

for i in imgUrl:
    urlretrieve(i, "크롤링사진/" + search + str(n) + ".jpg")
    n += 1

driver.close()