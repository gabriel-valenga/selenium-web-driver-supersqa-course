from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com')
print(driver.title)