#source : https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3

import requests
import csv
from bs4 import BeautifulSoup

f = csv.writer(open('zackrank.csv', 'w'))
f.writerow(['Name', 'Link'])

stocks = [ 'ebay' ]
stock_ranks = []

for symbol in stocks:
    url = 'https://www.zacks.com/stock/quote/{}?q={}'.format(symbol,symbol) 
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    div = soup.find('div', class_='zr_rankbox')
    p = div.find('p', class_='rank_view').get_text().split()
    print(p, div)
    stock_ranks.append( (symbol, int(p[1])) )
  
#Todo : add pandas frame with date , extract VGM