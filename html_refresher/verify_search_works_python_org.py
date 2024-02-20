from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.python.org/')
driver.implicitly_wait(10)

current_title = driver.title 
expected_title = 'Welcome to Python.org'

if current_title != expected_title:
    raise Exception(f'Went to python.org but got wrong title. Current title: {current_title}')

search_field_id = 'id-search-field'
search_field_element = driver.find_element(By.ID, search_field_id)
search_field_element.send_keys('testing')

go_button_id = 'submit'
go_button_element = driver.find_element(By.ID, go_button_id)
go_button_element.click()

first_result_xpath = '//*[@id="content"]/div/section/form/ul/li[1]'
first_result_element = driver.find_element(By.XPATH, first_result_xpath)

if not first_result_element.is_displayed():
    raise Exception(f'After searching the element result is not displayed')
print('passed')