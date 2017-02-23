# Sample Test passing with nose and pytest
import fairtrade as ft

sample_url = r'https://www.alibaba.com//Gym-Equipment_pid100006579?spm=a2700.8270666-18.201612262000.107.Ub4iIB'

try:
	ft.scrape_products(sample_url)
	print 'Function executed, check csv file'
except:
	print 'Test failed'




