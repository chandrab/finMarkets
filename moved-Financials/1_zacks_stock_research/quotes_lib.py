#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 08:24:45 2017

@author: Reddy
"""

from pandas_datareader import data
import pandas as pd

def get_stock_quotes(symbol, dt_start, dt_end):

    tickers = [ symbol ]
    
    # Define which online source one should use
    data_source = 'google'
    
    
    # User pandas_reader.data.DataReader to load the desired data. As simple as that.
    panel_data = data.DataReader(tickers, data_source, dt_start, dt_end)
    
    # Getting just the adjusted closing prices. This will return a Pandas DataFrame
    # The index in this DataFrame is the major index of the panel_data.
    close = panel_data.ix['Close']
    
    # Getting all weekdays between 
    all_weekdays = pd.date_range(start=dt_start, end=dt_end, freq='B')
    
    # How do we align the existing prices in adj_close with our new set of dates?
    # All we need to do is reindex close using all_weekdays as the new index
    close = close.reindex(all_weekdays)
    
    return close

# main program call
if __name__ == '__main__':
    c = get_stock_quotes('IBM', '2017-01-01', '2017-01-10')
    c.head(3)
    
""" 
To Run from Console

from quotes_lib import *
c = get_stock_quotes('IBM', '2017-01-01', '2017-01-10')
""" 
