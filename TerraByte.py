from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup



driver = webdriver.Chrome()
url = 'https://web.housing.illinois.edu/diningmenus'
driver.get(url)

select_all_you_care_to_eat = driver.find_element(By.ID, 'dineop')
select_all_you_care_to_eat = Select(select_all_you_care_to_eat)
select_all_you_care_to_eat.select_by_visible_text("(Select Location)")

select_retail = driver.find_element(By.ID, 'retailop')
select_retail = Select(select_retail)
select_retail.select_by_visible_text("Caffeinator")

select_date = driver.find_element(By.ID, 'mealdate')
select_date.clear()
select_date.send_keys("03262024")

button = driver.find_element(By.CSS_SELECTOR, '.il-button.view')
button.click()


menu = driver.find_element(By.ID, 'menuData')

html = menu.get_attribute('innerHTML')
soup = BeautifulSoup(html, 'lxml')
location = soup.find('h2').get_text()

def food_filter(tag):
    return tag.name == 'p' and 'DailyMenu' in tag.get('id', '')

    

food_items_paragraph = soup.find_all(food_filter)
#print(food_items)
food_items = []
for paragraph in food_items_paragraph: 
    text = ''.join(paragraph.stripped_strings).strip()
    print(text)
    # Remove text under the b tag
    text = text.replace(paragraph.b.string, '').strip()
    
    # Split text by comma and add each item to the lines list
    items = [item.strip() for item in text.split("<br>")]
    print(items)
    food_items.extend(items)
#list = food_items.get_text(separator="<br>").split("<br>")
menu = soup.find('p').get_text()
#list = [line.strip() for line in list]

with open('TerraByte.txt', 'w') as file:
    for line in food_items:
        file.write(line + '\n')

print(menu)
print (food_items)
#print(soup.prettify())
print(location)
