import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://www.bnr.ro/Cursul-de-schimb--7372.aspx")
link = BeautifulSoup(r.text, "html.parser")
# print(link)

# Vrem sa luam tabelul
title = link.find_all('div', attrs={'class': 'contentDiv'})[0]
# print(title)
header = []
dataset = []
for tr_index in title.find_all('table'):
    # print(tr_index)
    for td_index in tr_index.find_all('tr'):
        # print(td_index)
        td_list = []
        # Daca gasim th
        if td_index.find_all('th'):
            # Salvam lista de header-e
            header = [th_index.get_text() for th_index in td_index.find_all('th')]
            # print(header)
        # enumerate ia si index ul si valoarea
        for index, td_value in enumerate(td_index.find_all('td')):
            # print(item.get_text()) get_text() -> ca sa scapam de '<_>'
            # print(index, td_value)
            # daca indexul este 0, avem data -> pastram asa
            # altfel, avem numar cu ',' si vrem '.' in loc (pt excel)
            if index == 0:
                td_list.append(td_value.get_text())
            else:
                # print(td_value.get_text().lstrip('   ').replace(',', '.'))
                td_list.append(float(td_value.get_text().lstrip('   ').replace(',', '.')))
        dataset.append(td_list) # fiecare lista td_list -> un rand din tabelul de pe site
print(dataset)

# dataframe -> "matrice"
df = pd.DataFrame(dataset, columns=header)
df.to_csv("CursBNR.csv", header=header)
