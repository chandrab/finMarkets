#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 18:02:43 2018

@author: padma

Run as command line then working as
    $python3 supres.py
"""

#from numpy import array 
import numpy as np
from scipy.signal import savgol_filter as smooth


def supres(ltp, n):
    """
    This function takes a numpy array of last traded price
    and returns a list of support and resistance levels 
    respectively. n is the number of entries to be scanned.
    """

    #converting n to a nearest even number
    if n%2 != 0:
        n += 1
    
    n_ltp = ltp.shape[0]

    # smoothening the curve
    ltp_s = smooth(ltp, (n+1), 3) 

    #taking a simple derivative
    ltp_d = np.zeros(n_ltp)
    ltp_d[1:] = np.subtract(ltp_s[1:], ltp_s[:-1])
 
    resistance = []
    support = []
    
    for i in range(n_ltp - n):
        arr_sl = ltp_d[i:(i+n)]
        
        half = int(n/2) # asr chagned n/2 to half all below to getrid of error
        
        first = arr_sl[:half] #first half
        last = arr_sl[half:] #second half
        
        r_1 = np.sum(first > 0)
        r_2 = np.sum(last < 0)

        s_1 = np.sum(first < 0)
        s_2 = np.sum(last > 0)

        #local maxima detection
        if (r_1 == (n/2)) and (r_2 == half): 
            resistance.append(ltp[i+(half -1)])

        #local minima detection
        if (s_1 == (n/2)) and (s_2 == (n/2)): 
            support.append(ltp[i+((n/2)-1)])

    print( support, resistance)
    return support, resistance

# ***** -------- main
#
with open('prices.txt') as f:
    content = f.readlines()
    
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
prices = np.array( content )  # convert list to numpy array

print(prices[1])
sup, res = supres(prices, 60)
print( sup, res)
