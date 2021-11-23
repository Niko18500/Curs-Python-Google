from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/")
table = browser.find_element(By.XPATH, '//*[@id="post-25121"]/div/div/table[1]')
table_text = table.text

# print(table_text)

lista = table_text.split(' ')
# print(lista)

header = browser.find_element(By.XPATH, '//*[@id="post-25121"]/div/div/table[1]/tbody/tr[1]').text
print(header)

dictionar = {i: [] for i in header}
for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        dictionar[header[int(j)]].append(lista[i])
# print(dictionar)

# df = pd.DataFrame(dictionar)
# df.to_csv("BNR_ALL_DATA.csv")


time.sleep(2)
browser.close()
