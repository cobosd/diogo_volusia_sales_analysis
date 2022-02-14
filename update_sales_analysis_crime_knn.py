# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 20:37:04 2021

@author: dnaza
"""

import psycopg2
import re
import matplotlib.pyplot as plt
import os
import pandas as pd

# connection to database:
try:
    conn = psycopg2.connect("dbname='spatial' user='postgres' host='localhost' password='' ")
except:
    print("cant connect to the database")

cur = conn.cursor()
cur2 = conn.cursor()
cur3 = conn.cursor()



sql = "select parid from volusia.sales_analysis" # limit 10"

print('SQL: ', sql)
cur.execute(sql)
# row = cur.fetchone()

# one way grab all the data into a multi-dimensional array
data = cur.fetchall()
#actual_data = data[0][0]

# I like to fetch one row at a time like reading data from a file
i=0

for row in range(0, len(data)): # is not None:
    i = i + 1
    
    parcel = int(data[row][0])
    
    print('\n',i)
    print(parcel)
    
    sql2 = "SELECT c.crime_desc, c.address, c.crime_date, ST_Distance(s.geom, c.geom)/5280 as d_miles FROM volusia.crime_info c, volusia.sales_analysis s where s.parid=" + str(parcel) +"  order by s.geom <-> (select c.geom) limit 1;"
    cur2.execute(sql2)
    row2 = cur2.fetchone()
    
    desc = row2[0]
    add = row2[1]
    date = row2[2]
    dist = row2[3]
    
    #Whenever KNN returns 0
    if dist == None:
        dist = 0
        
    sql3 = "update volusia.sales_analysis s set crime_date = '" + str(date) + "', crime_desc = '" + str(desc) + "', crime_add = '" + str(add) + "', crime_dist = " + str(dist) + " where s.parid=" + str(parcel) + ";"
    cur3.execute(sql3)

    
    if i%10000 == 0:
        print(i)
        conn.commit()
    row = cur.fetchone()

#df = pd.
conn.commit()
conn.close()