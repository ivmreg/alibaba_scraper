import requests, pprint
import pandas as pd
from bs4 import BeautifulSoup

#Get HTML file
url = r'https://www.alibaba.com/Communication-Equipment_pid100002951?spm=a2700.8190021-509.199005.29.J1Lu7S'
res = requests.get(url)

#List of items
item_list = []
price_list = []

#Parse all items
soup = BeautifulSoup(res.text, 'html.parser')

for itemclass in soup.find_all('h2', class_='title'):
	item_list.append(itemclass.text)

#Parse item prices
for price in soup.find_all('div', class_='price'):
	price_list.append(price.text)

#Join items and prices together
item_price_list = zip(item_list, price_list)

#Put list of tuples into a dataframe and export as csv
df = pd.DataFrame(item_price_list, columns=['item', 'price'])
df.to_csv('alibaba_itemlist.csv', index=False)