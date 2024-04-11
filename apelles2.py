from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Justice_League_Warworld-27687527'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())
box = soup.find('article', class_='main-article')
# print(box)
title = box.find('h1').get_text()
# transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

print(title)
# print(transcript)

# with open(f'{title}.txt', 'w') as file:
#   file.write(transcript)