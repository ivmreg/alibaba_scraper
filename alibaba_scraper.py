import requests, pprint
import pandas as pd
from bs4 import BeautifulSoup

#Get HTML file
url = r'https://www.alibaba.com//Gym-Equipment_pid100006579?spm=a2700.8270666-18.201612262000.106.RCusGd'
res = requests.get(url)

#List of items
item_list = []
price_list = []
moq_list = []

#Parse all items
soup = BeautifulSoup(res.text, 'html.parser')

for itemclass in soup.find_all('h2', class_='title'):
	item_list.append(itemclass.text)

#Parse item prices
for price in soup.find_all('div', class_='price'):
	price_list.append(price.text)

for moq in soup.find_all('div', class_='min-order'):
	moq_list.append(moq.text)

#Join items and prices together
item_price_list = zip(item_list, price_list, moq_list[1:])

#Put list of tuples into a dataframe and export as csv
df = pd.DataFrame(item_price_list, columns=['item', 'price', 'moq'])
df.to_csv('alibaba_itemlist.csv', index=False)