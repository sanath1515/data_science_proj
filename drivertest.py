# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 19:59:11 2023

@author: HP
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By



path = "C:/Users/HP/OneDrive/Desktop/Data Science/ds_proj/chromedriver-win64/chromedriver.exe"

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/');

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element(By.NAME,'q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()