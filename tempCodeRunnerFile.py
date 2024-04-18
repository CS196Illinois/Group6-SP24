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

cafe = soup.find('h3', text='Cafe a la Crumb').get_text()
breakf = cafe.find('p', text = 'Breakfast - 03/04/2024').get_text()
print (cafe)
print (breakf)