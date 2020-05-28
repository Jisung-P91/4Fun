import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt

import random
import time
from tqdm import tqdm, trange ## let you know how much progress made
import re

# base_url = f'https://listfist.com/list-of-one-piece-manga-chapters'
# response = requests.get(base_url)

# # print (response)
# print(response.text)

# if response.status_code == 410:
##print (response.status_code) should return 200 but in this case we didn't get that, so tried below.

url = 'https://listfist.com/list-of-one-piece-manga-chapters'
headers = {'User-Agent': 'whatever'}

r = requests.get(url, headers=headers)

# print(r.text)

html = bs(r.text, "html.parser")
datadiv = html.find("table", {"id": "igsv-1mGtvb_1HownoAPQt3NftgtB7fM96toIQ8UnnwpNnJcs"})
elementsfull = []
row = 0
for tr in datadiv.findAll("tr"):
    elements = []
    columns = 0
    for td in tr.findAll("td"):
        if(td.text!=""):
            elements.append(td.text)
            columns+=1
    elementsfull.append(elements)
    row+=1

op_df = pd.DataFrame(data=elementsfull)
print (op_df.head())

op_df.to_csv("datasets/OP_list.csv")

coltitle = html.find("tr", {"id": "igsv-1mGtvb_1HownoAPQt3NftgtB7fM96toIQ8UnnwpNnJcs-row-1"})
titlesfull = []
row = 0
for th in coltitle.findAll("th"):
    titles = []
    columns = 0
    for div in th.findAll("div"):
        if(div.text!=""):
            titles.append(div.text)
            columns+=1
    titlesfull.append(titles)
    row+=1

print(titlesfull)

op_title_df = pd.DataFrame(data=titlesfull)
print(op_title_df.head())

op_title_df = op_title_df.transpose()
print(op_title_df.head())


op_title_df.to_csv("datasets/OP_list_title.csv")

op_df = op_df.drop([0]) # to remove the first row
op_df = pd.concat([op_title_df,op_df])
## or you can do this --> op_df = op_title_df.append(op_df)

header_row = 0
op_df.columns = op_df.iloc[header_row]
op_df = op_df.drop(header_row)
op_df["Date"] = pd.to_datetime(op_df["Date"]) #to make date as numeric
op_df = op_df.set_index("Date")
print(op_df.head(3))

##op_df.info(): we see hat pages and # are not numberic but objects, so we need to conver it

op_df["#"]=pd.to_numeric(op_df["#"])
op_df["Pages"]=pd.to_numeric(op_df["Pages"])

op_df["#"].plot()
plt.show()







