from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
import inquirer
import api
from api import get_data

inquiry = [
  inquirer.List('Location',
                message="Dinning Hall?",
                choices=['PAR Dining Hall', 'Ikenberry Dining Center', 'ISR Dining Center', 'Field of Greens', 'Lincoln/Allen Dining Hall', 'Kosher Kitchen'],
            ),
]
answers = inquirer.prompt(inquiry)

user_dinning_hall = answers["Location"]
user_date = input("Please enter your date:" )
print(user_date)

driver = webdriver.Chrome()
url = 'https://web.housing.illinois.edu/diningmenus'
driver.get(url)

select_all_you_care_to_eat = driver.find_element(By.ID, 'dineop')
select_all_you_care_to_eat = Select(select_all_you_care_to_eat)
select_all_you_care_to_eat.select_by_visible_text(user_dinning_hall)

select_retail = driver.find_element(By.ID, 'retailop')
select_retail = Select(select_retail)
select_retail.select_by_visible_text("(Select Location)")

select_date = driver.find_element(By.ID, 'mealdate')
select_date.clear()

select_date.send_keys(user_date)

button = driver.find_element(By.CSS_SELECTOR, '.il-button.view')
button.click()




menu = driver.find_element(By.ID, 'menuData')

html = menu.get_attribute('innerHTML')
soup = BeautifulSoup(html, 'lxml')
location = soup.find('h2').get_text()


def lunch_id_filter(tag):
    return tag.name == 'p' and 'Lunch' in tag.get('id', '')

def dinner_id_filter(tag):
    return tag.name == 'p' and 'Dinner' in tag.get('id', '')

def breakfast_id_filter(tag):
    return tag.name == 'p' and 'Breakfast' in tag.get('id', '')

lunch_paragraphs = soup.find_all(lunch_id_filter)
lunch_menu_items = []
for paragraph in lunch_paragraphs:
    text = ''.join(paragraph.stripped_strings).strip()
    
    # Remove text under the b tag
    text = text.replace(paragraph.b.string, '').strip()
    
    # Split text by comma and add each item to the lines list
    items = [item.strip() for item in text.split(',')]
    lunch_menu_items.extend(items)

dinner_paragraphs = soup.find_all(dinner_id_filter)
dinner_menu_items = []
for paragraph in dinner_paragraphs:
    text = ''.join(paragraph.stripped_strings).strip()
    
    # Remove text under the b tag
    text = text.replace(paragraph.b.string, '').strip()
    
    # Split text by comma and add each item to the lines list
    items = [item.strip() for item in text.split(',')]
    dinner_menu_items.extend(items)


breakfast_paragraphs = soup.find_all(breakfast_id_filter)
#another method to get text: breakfast_menu_items = [p.get_text() for p in breakfast_paragraphs]
breakfast_menu_items = []
for paragraph in breakfast_paragraphs:
    text = ''.join(paragraph.stripped_strings).strip()
    
    # Remove text under the b tag
    text = text.replace(paragraph.b.string, '').strip()
    
    # Split text by comma and add each item to the lines list
    items = [item.strip() for item in text.split(',')]
    breakfast_menu_items.extend(items)


#print(dinner_menu_items)
#print(lunch_menu_items)
print(breakfast_menu_items)

result = get_data(breakfast_menu_items)
print(result)

with open('CurrentMenu.txt', 'w') as file:
    file.write(location + '\n' + '\n')
    file.write("Lunch" + '\n' + '\n')    
    for line in lunch_menu_items:
        file.write(line + '\n')
    file.write('\n' + "Dinner" + '\n' + '\n')
    for line in dinner_menu_items: 
        file.write(line + '\n')
    file.write('\n' + "Breakfast" +'\n' + '\n')
    for line in breakfast_menu_items:
        file.write(line + '\n')

#print(list)
#print(menu)
print(location)
