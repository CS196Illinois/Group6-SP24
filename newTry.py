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

# Initialize a dictionary to store dining service menus
dining_service_menus = {}

# Find all dining service units (h3 elements) in the HTML
dining_service_units = soup.find_all('h3', class_='diningserviceunit')

# Loop through each dining service unit
for unit in dining_service_units:
    unit_name = unit.text.strip()  # Extract the unit name
    unit_menus = {}  # Initialize a dictionary to store menus for the current unit
    
    # Find all sibling elements following the current h3 element until the next h3 or end of document
    next_element = unit.find_next_sibling()
    while next_element and next_element.name != 'h3':
        # Check if the element is a p element indicating a meal category
        if next_element.name == 'p' and 'background-color' in next_element.get('style', ''):
            category_name, date = next_element.text.split(' - ')  # Extract category name and date
            menu_items = []  # Initialize a list to store menu items
            
            # Find the next sibling p elements (menu items) until the next meal category or dining service unit
            next_menu_item = next_element.find_next_sibling('p')
            while next_menu_item and ('background-color' not in next_menu_item.get('style', '') or next_menu_item.get('style', '').startswith('background-color:var(--il-cloud-1);')):
                menu_items.append(next_menu_item.text.strip())  # Append the menu item to the list
                next_menu_item = next_menu_item.find_next_sibling('p')
            
            # Store the list of menu items in the unit_menus dictionary under the category name
            unit_menus.setdefault(category_name, []).extend(menu_items)
        
        # Move to the next sibling element
        next_element = next_element.find_next_sibling()
    
    # Store the unit_menus dictionary in the dining_service_menus dictionary under the unit name
    dining_service_menus[unit_name] = unit_menus

# Print the resulting dictionary
print(dining_service_menus)