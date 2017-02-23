import requests, pprint
import pandas as pd
from bs4 import BeautifulSoup

def scrape_products(url):
	'''Takes in url of products page from alibaba.com and scrapes the product name,
	price, min order quantity, and seller name and exports the data as a csv
	'''

	res = requests.get(url)

	#List of items
	item_list = []
	price_list = []
	moq_list = []
	seller_list = []

	#create html document
	soup = BeautifulSoup(res.text, 'html.parser')

	#retrieve list of items being sold
	for itemclass in soup.find_all('h2', class_='title'):
		item_list.append(itemclass.text)

	#retrieve prives of items
	for price in soup.find_all('div', class_='price'):
		price_list.append(price.text)

	#retrieve the minimun order quantity
	for moq in soup.find_all('div', class_='min-order'):
		moq_list.append(moq.text)

	#retrieve the list of sellers
	for seller in soup.find_all('div', class_='stitle'):
		seller_list.append(seller.text)

	#Join all qualities together
	#moq_list[1:] because the first element is actually from the search bar and not an item
	item_price_list = zip(item_list, price_list, moq_list[1:], seller_list)

	#Put list of tuples into a dataframe and export as csv
	df = pd.DataFrame(item_price_list, columns=['ITEM', 'PRICE', 'MOQ', 'SELLER'])
	df.to_csv('alibaba_itemlist.csv', index=False)

