#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 19:31:14 2018

@author:  
"""

# *****  Dev Notes ******************************************************
#
#  RUNNING SELENIUM WITH Full CHROME browser and scraping web page
# see post below for details  
#
#  0. $conda install --name <myenv> selenium   # install 'selenium'  

#  1. download and unzip chrome dirver from  https://sites.google.com/a/chromium.org/chromedriver/
#  2. copy chromedriver exectable file to current directory where you are executing this python program 
#  
#  3. $python by_full_browser.py   # run this python file, it will get result by opening Browser 
#
#   https://stackoverflow.com/questions/39197977/python-beautifulsoup-scrape-yahoo-finance-value
#   https://stackoverflow.com/questions/38173541/how-to-resolve-chromedriver-executable-needs-to-be-in-path-error-when-running
#   https://stackoverflow.com/questions/29858752/error-message-chromedriver-executable-needs-to-be-available-in-the-path
#
# **********************************************************************

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def full_browser():
    # this is executable file by  unzip of downloaded chrome driver from https://sites.google.com/a/chromium.org/chromedriver/
    chromedriver_loc = './chromedriver2'  
    driver = webdriver.Chrome(executable_path=chromedriver_loc)
    
    #driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://finance.yahoo.com/quote/AAPL/profile?p=AAPL")
    
    # wait for the Full Time Employees to be visible
    wait = WebDriverWait(driver, 10)
    employees = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[. = 'Full Time Employees']/following-sibling::strong")))
    print(employees.text)
    
    driver.close()
 

 
# *****  main call ****************************
#
# **********************************************
full_browser()