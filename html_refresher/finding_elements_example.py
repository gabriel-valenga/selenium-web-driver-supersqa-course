from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

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
my_products = driver.find_elements(By.CLASS_NAME, 'product')

my_products[0].click()

# driver.implicitly_wait(60) - to wait implicity 60 seconds vefore try to get an element
product_zoom_image = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="product-13"]/div[1]/a'))) #to wait explicity 30 seconds before try to get an element (returns a element)

product_zoom_image.click()
procuct_zoom_image_caption =  driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[4]/div') 
print(f'Product image caption: {procuct_zoom_image_caption.text}')

sleep(10)

driver.quit()
# driver.close()





