# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 10:25:42 2021

@author: dnaza
"""

import censusgeocode as cg
import pandas as pd
import geopandas as gpd


df_main = pd.read_excel('G:/MA 540 - Data Mining/PROJECT/Last6MonthsVolusiaCrime.xlsx')

coord = []

for row in range(5251, len(df_main)):    #Change range as needed
    
    print(row)
    
    
    #reset iteration values to avoid mistakes
    df = [] 
    x = None
    y = None
    
    df = df_main.iloc[row]
    tp = df['TYPE']
    add = df['ADDRESS']
    dpt = df['DEPARTMENT']
    
    if (tp == 'DRUNK DRIVER' or tp == 'DRUNK PERSON') and (dpt == 'Volusia County Sheriff' or dpt == 'Volusia County Beach Patrol'):
        continue #do nothi for these cases
        
    else:
        city = dpt.replace(' Police','')
        full_add = add.replace(' BLK', '') + ', ' + city + ', FL'
        
        try:
            x, y = cg.onelineaddress(full_add)[0]['coordinates'].values()
            
            # x , y = dic[0]['coordinates'].values()
            
            # x = longitude, y = latitude
            if y != '' and x != '' and float(y) > 27.5 and float(y) < 34 and float(x) < -80.5 and float(x) > -82:
                coord.append([full_add, float(x), float(y)])
           
        
        except Exception:
            next
            

crime_df = pd.DataFrame(coord,  columns =['ADDRESS', 'LON', 'LAT'])
crime_df.to_csv(r'G:/MA 540 - Data Mining/PROJECT/crime_coord_3.csv')