from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option("detach", True) #keep browser open after run this script
driver = webdriver.Chrome(options=driver_options)
driver.get('http://demostore.supersqa.com')

#By.ID

cart = driver.find_element(By.ID, 'site-header-cart')
print(cart)
print(type(cart))
cart_text = cart.text
print(cart_text)

search_field = driver.find_element(By.ID, 'woocommerce-product-search-field-0')
search_field.send_keys('Hoodie')
search_field.send_keys(Keys.ENTER)

#By.CSS_SELECTOR

my_account_menu = driver.find_element(By.CSS_SELECTOR, '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9')
# my_account_menu = driver.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]' )
# my_account_menu = driver.find_element(By.XPATH, '/html/body/div[2]/header/div[2]/div/nav/div[1]/ul/li[4]' )
# my_account_menu.click()

#By.CLASS_NAME
my_products = driver.find_elements(By.CLASS_NAME, 'woocommerce-LoopProduct-link woocommerce-loop-product__link')

# driver.quit()
# driver.close()





