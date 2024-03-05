from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
import requests



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
select_date.send_keys("03042024")

button = driver.find_element(By.CSS_SELECTOR, '.il-button.view')
button.click()


menu = driver.find_element(By.ID, 'menuData')

html = menu.get_attribute('innerHTML')



# beautifulsoup part


soup = BeautifulSoup(html, 'lxml')
resTitle = soup.find(id = 'resTitle').get_text()

# cafe = soup.find('h3', text='Cafe a la Crumb').get_text()
# breakf = cafe.find('p', text = 'Breakfast - 03/04/2024').get_text()
# print (cafe)
# print (breakf)


# -----------------------------------------------------
# Find the div with class 'menuData'
menu_data = BeautifulSoup(html, 'lxml')

# Initialize a dictionary to store dining service units and their menus
dining_service_units = {}

# Find all h3 elements within the menu_data_div
h3_elements = menu_data.find_all('h3', class_='diningserviceunit')

# Iterate through each h3 element
for h3_element in h3_elements:
    # Get the text of the h3 element (dining service unit name)
    dining_service_unit = h3_element.get_text().strip()
    
    # Initialize a dictionary to store categories and their menus for this dining service unit
    categories_menu = {}
    
    # Find the next sibling p element after the h3 element
    next_sibling = h3_element.find_next_sibling('p')
    
    # Iterate through sibling p elements until the next h3 element is encountered
    while next_sibling and next_sibling.name == 'p':
        # Get the category (e.g., breakfast, lunch) from the p element text
        category = next_sibling.get_text().strip().split(' - ')[0]
        # Get the menu items for this category
        menu_items = next_sibling.find_next_sibling('p')
        for menu_item in menu_items:
            menu_item.get_text().strip()
        # Store the category and its menu items in the dictionary
        categories_menu[category] = menu_items
        # Move to the next sibling
        next_sibling = next_sibling.find_next_sibling()
    
    # Store the dining service unit and its categories/menus in the dictionary
    dining_service_units[dining_service_unit] = categories_menu

# Now you have a dictionary where each key is a dining service unit
# and the corresponding value is a dictionary containing categories and their menus
# -----------------------------------------------



# diningServiceUnits = soup.find_all(class_='diningserviceunit')

# if isinstance(diningServiceUnits, list):  # Check if it's a list (multiple elements)
#     for diningServiceUnit in diningServiceUnits:
#         print(diningServiceUnit.get_text())
# else:  # It's a single element
#     print(diningServiceUnits.get_text())

# menu = soup.find_all('p')
# breakfasts = soup.find_all('p', string = 'Breakfast - 03/04/2024')
# lunchs = soup.find_all('p', string = 'Lunch - 03/04/2024')
# dinners = soup.find_all('p', string = 'Dinner - 03/04/2024')

# for breakfast in breakfasts:
#         print(breakfast.get_text())
# for lunch in lunchs:
#         print(lunch.get_text())
# for dinner in dinners:
#         print(dinner.get_text())