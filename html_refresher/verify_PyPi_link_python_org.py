from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.python.org/')

current_title = driver.title 
expected_title = 'Welcome to Python.org'

if current_title != expected_title:
    raise Exception(f'Went to python.org but got wrong title. Current title: {current_title}')

pypi_header_link_locator = '#top > nav > ul > li.pypi-meta > a'
pypi_header_link_element = driver.find_element(By.CSS_SELECTOR, pypi_header_link_locator) 
pypi_header_link_element.click()

curent_url = driver.current_url
expected_url = 'https://pypi.org/'
assert curent_url == expected_url, f'Clicked on PYPi but the url opened was: {curent_url}'
print('passed')