from bs4 import BeautifulSoup
import requests 

website = 'https://en.wikipedia.org/wiki/Dookie'
website2 = 'https://ollivere.co/'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
#print(soup.prettify())
box = soup.find('span', class_='mw-headline')
title = soup.p.get_text()
print(box)
#print()