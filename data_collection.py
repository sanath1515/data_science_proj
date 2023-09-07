# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 19:26:54 2023

@author: HP
"""

import glassdor_scraper as gs
# import pandas as pd

path = "C:/Users/HP/OneDrive/Desktop/Data Science/ds_proj/chromedriver-win64/chromedriver"
df = gs.get_jobs('data scientist', 15, False, path, 5)
print(df)
# //*[@id="LoginModal"]/div/div/div/div[2]/button

# /html/body/div[14]/div/div/div/div[2]/button