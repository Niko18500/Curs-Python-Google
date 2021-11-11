import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://www.emag.ro/#opensearch")

get_element = browser.find_element(By.ID, "searchboxTrigger")
get_element.send_keys("telefon")
get_element.submit() # pt "enter"

# product = browser.find_element(By.ID, 'card_grid')
# print(product.text)

product = browser.find_element(By.CLASS_NAME, 'card-item')
print(product.text)

time.sleep(10)  # pt ca se inchide browser-ul (nush dc)

# selenium -> pt testare automata in browser-e