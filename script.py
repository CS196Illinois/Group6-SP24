from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
import requests
import time



driver = webdriver.Chrome()
url = 'https://web.housing.illinois.edu/diningmenus'
driver.get(url)

select_all_you_care_to_eat = driver.find_element(By.ID, 'dineop')
select_all_you_care_to_eat = Select(select_all_you_care_to_eat)
select_all_you_care_to_eat.select_by_visible_text("ISR Dining Center")

select_retail = driver.find_element(By.ID, 'retailop')
select_retail = Select(select_retail)
select_retail.select_by_visible_text("(Select Location)")

select_date = driver.find_element(By.ID, 'mealdate')
select_date.clear()
select_date.send_keys("03182024")

button = driver.find_element(By.CSS_SELECTOR, '.il-button.view')
button.click()


menu = driver.find_element(By.ID, 'menuData')
time.sleep(2)
html = menu.get_attribute('innerHTML')



soup = BeautifulSoup(html, 'lxml')

diningServiceMenus = {}

diningServiceUnits = soup.find_all('h3')

for unit in diningServiceUnits:
    unit_name = unit.text.strip()

    next_h3 = unit.find_next('h3')

    unique_categories = set()

    meal_categories = unit.find_all_next('p', until=lambda tag: tag == next_h3)

    unit_menus = {}

    for category in meal_categories:
        if category.get('style') == 'background-color:var(--il-cloud-1);':
            category_name = category.text.strip()
            
            if category_name not in unique_categories:
                unique_categories.add(category_name)
                menu_items = []

                menu_elements = category.find_all_next('p', until=lambda tag: tag == next_h3)

                for menu_element in menu_elements:
                    menu_items.append(menu_element.text.strip())

                    if (menu_element.find_next('h3')):
                        break
                    

                unit_menus[category_name] = menu_items

    diningServiceMenus[unit_name] = unit_menus

print(diningServiceMenus)










