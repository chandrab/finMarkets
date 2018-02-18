#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 19:27:59 2018

@author: padma
"""

import requests
from bs4 import BeautifulSoup


import sys # import module sys to get the type of exception

# *****  extract_rank_info() function *********
#
# **********************************************
def analyst_target_price(symbol_):
    row_ = []
    try:  
        url = 'https://finance.yahoo.com/quote/{}?p={}'.format(symbol_,symbol_) 
        page = requests.get(url)
          
        #print(page.status_code)
        soup = BeautifulSoup(page.text, 'html.parser')
    
    
        app = soup.find('div', attrs={'id':'app'})
        print(app)
        
        str = app.find(string="Analyst Price Targets")
        

        print(str)
        
        """
        id = app.find('div',attrs={'data-reactid':'1'})
        id = id.find('div', attrs={'data-reactid':'2'})
        id = id.find('div', attrs={'data-reactid':'3'})
        id = id.find('div', attrs={'data-reactid':'4'})
        print(len(id))
        #print(id)
        id = id.find('div', attrs={'id':'YDC_Col2'})
        #id = id[1]
        #id = id.find('div', attrs={'data-reactid':'35'})
        #id = id.find('div', attrs={'data-reactid':'36'})
        
        id = soup.find_all("div")
       
        print(id)
        
        //*[@id="Col2-7-QuoteModule-Proxy"]/div/section/a/h2
        #Col2-7-QuoteModule-Proxy > div > section > a > h2
        <h2 class="Fz(m) D(ib) Td(inh)">Analyst Price Targets (33)</h2>
        """
       
    except:
        print(symbol_," : For this symbol Eror Occured!",sys.exc_info()[0])
  
    return row_

# main
analyst_target_price('EBAY')


