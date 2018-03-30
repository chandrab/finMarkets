#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 19:31:14 2018

@author: 
"""

# *****  Dev Notes ******************************************************
#
# RUNNING SELENIUM WITH HEADLESS CHROME and scraping web page
#   follow steps from this blog post
#   https://intoli.com/blog/running-selenium-with-headless-chrome/

#  0. $conda install --name <myenv> selenium   # install 'selenium'   
#  1. $brew install chromedriver
#  2. $chromedriver   # start, it listens on a port
#  3. $python by_headless_browser.py   # run this python file, it will get result without opening Browser 
#
# **********************************************************************

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from bs4 import BeautifulSoup
 
# *****  extract_rank_info() function *********
#
# ********************************************** 
def headless_browser():
    
    options = webdriver.ChromeOptions()
    
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    # set the window size
    #options.add_argument('window-size=1200x600')

    # initialize the driver
    driver = webdriver.Chrome(chrome_options=options)

    #driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.get("http://finance.yahoo.com/quote/AAPL/profile?p=AAPL")
    
    # wait for the Full Time Employees to be visible
    wait = WebDriverWait(driver, 90)
    employees = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[. = 'Full Time Employees']/following-sibling::strong")))
    print(employees.text)
    
    # driver.close()
    
    # get help from this url
    # https://coderwall.com/p/vivfza/fetch-dynamic-web-pages-with-selenium
    # https://www.linkedin.com/pulse/scraping-therapists-python-selenium-beautifulsoup-scott-edenbaum
    
    # And grab the page HTML source
    html_page = driver.page_source
    driver.quit()
    
    # Now you can use html_page as you like
   
    soup = BeautifulSoup(html_page, "html.parser")

    str_node = soup.find(string="100,000")
    print(soup)
# *****  main call ****************************
#
# **********************************************
headless_browser()