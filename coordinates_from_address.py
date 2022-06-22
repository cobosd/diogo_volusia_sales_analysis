# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 21:00:18 2021

@author: dnaza
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

df = pd.read_excel('G:/MA 540 - Data Mining/PROJECT/Last6MonthsVolusiaCrime.xlsx')
                 
url = 'https://www.mapdevelopers.com/geocode_tool.php'
driver = webdriver.Chrome()
driver.get(url)

location = []

for add in df['ADDRESS']:
    
    lat = None
    lon = None
    
    add = add.replace('BLK ', '') #Remove BLK to prevent errors 
    mngmntIP = driver.find_element_by_xpath('//*[@id="address"]')
    # content = driver.find_element_by_class_name('width70')
    mngmntIP.clear()
    key = add + ', volusia'
    mngmntIP .send_keys(key)
    
    wait = WebDriverWait(driver, 10)
    launchButton = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="search-form"]/div[1]/span[2]/button')))
    launchButton.click()
    
    lon = driver.find_element_by_xpath('//*[@id="display_lng"]').text
    lat = driver.find_element_by_xpath('//*[@id="display_lat"]').text
    
    if lon != '' and lat != '' and float(lat) < 34 and float(lon) < -80.5:
        location.append([add, float(lat), float(lon)])
    
    
crime_df = pd.DataFrame(location,  columns =['ADDRESS', 'LAT', 'LON'])
crime_df.to_csv(r'G:/MA 540 - Data Mining/PROJECT/crime_coord.csv')