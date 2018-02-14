#source : https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3
# https://stackoverflow.com/questions/22003302/beautiful-soup-just-get-the-value-inside-the-tag

import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

import sys # import module sys to get the type of exception

# *****  extract_SnP500_symbols() function *********
#
# **************************************************
def extract_SnP500_symbols():
    snp500_list = []
    try:  
        url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies' 
        page = requests.get(url)
        #print(page.status_code)
        soup = BeautifulSoup(page.text, 'html.parser')
    
        # extract first table which is symbol list
        table = soup.find('table', class_='wikitable')
        trs = table.find_all('tr')
        #print(len(trs))
        
        
        for tr in trs:
            try:  
                tds = tr.find_all('td')
                symbol = str(tds[0].get_text())
                name = str(tds[1].get_text())
                #print(symbol, name)
                snp500_list.append([symbol, name])
                
            except:
                # first <tr> is table header, it won't have <td> so handle exception here
                print('While extracting <tr> Eror Occured!',sys.exc_info()[0])   
    
    except:
        print('While extracting S&P500 Symols Eror Occured!',sys.exc_info()[0])
  
    return snp500_list


# *****  get_SnP500_symbols() function *********
#
# **********************************************
def get_SnP500_symbols():
    # check if pickel file exists, if so read pickel file and return symbols
    # else call extract() function , write pickel then return symbol list
    
    #df.to_pickle("sp500-zacksRanks")

    #you can load it back using:
    #df = pd.read_pickle(file_name)
    
    symbol_list = extract_SnP500_symbols()
    return symbol_list
    
# *****  extract_rank_info() function *********
#
# **********************************************
def extract_rank_info(symbol_):
    row_ = []
    try:  
        url = 'https://www.zacks.com/stock/quote/{}?q={}'.format(symbol_,symbol_) 
        page = requests.get(url)
       
        
        #print(page.status_code)
        soup = BeautifulSoup(page.text, 'html.parser')
    
        # extract Rank
        div = soup.find('div', class_='zr_rankbox')
        p = div.find('p', class_='rank_view').get_text().split()
        # print(p, div)
        rank = int(p[1])
        
        # extract VGM  Sytle Score 
        div = soup.find('div', class_='zr_rankbox composite_group')
        p = div.find('p', class_='rank_view')
        span = p.find_all('span', class_='composite_val')
        vgm = [x.get_text() for x in span]
       
        
        row_ = [ symbol_, rank, vgm[0], vgm[1], vgm[2], vgm[3] ]
        print(row_)
       
    
    except:
        print(symbol_," : For this symbol Eror Occured!",sys.exc_info()[0])
  
    return row_


# *****  main() program *********************
#
# *******************************************
def main():
    #stocks = get_symbols()
    symbol_list = get_SnP500_symbols()
    print(len(symbol_list))
    stock_ranks = []
    
    for symbol_name in symbol_list:  
        row = extract_rank_info(symbol_name[0])
        if len(row) > 0:
            stock_ranks.append(row)
        
    print ( stock_ranks)

    # create Dataframe from list and save dataframe as pickle file
    df = pd.DataFrame(stock_ranks,columns=['Symbol','Rank', 'Value', 'Growth', 'Momentum', 'VGM_composite'])
    df['Date'] = datetime.datetime.now().strftime("%Y-%m-%d")
    print (df)
        
    df.to_pickle("sp500-zacksRanks")

    #you can load it back using:
    #df = pd.read_pickle(file_name)


# *****  callcmain() program *********
#
main()
