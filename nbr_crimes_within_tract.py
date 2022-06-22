# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 17:52:13 2021

@author: dnaza
"""


import psycopg2
import re
import matplotlib.pyplot as plt
import os
import pandas as pd

# connection to database:
try:
    conn = psycopg2.connect("dbname='spatial' user='postgres' host='localhost' password='vhq_5101'")
except:
    print("cant connect to the database")

cur = conn.cursor()
cur2 = conn.cursor()
cur3 = conn.cursor()



sql = "select name10 from volusia.dataframe" # limit 10"

print('SQL: ', sql)
cur.execute(sql)

# one way grab all the data into a multi-dimensional array
#data = cur.fetchall()
#actual_data = data[0][0]

# I like to fetch one row at a time like reading data from a file
i=0
row = cur.fetchone()
while row is not None:
    i = i + 1
    
    name10 = str(row[0])
    
    sql2 = "select count(*) from volusia.partial_crime c, volusia.dataframe p where p.name10 = '" + name10 + "' and ST_Within(c.geom, p.geom);"
    print(sql2)
    
    cur2.execute(sql2)
    row2 = cur2.fetchone()
    
    crimes = row2[0]
    
    sql3 = "update volusia.dataframe d set nbr_crimes = " + str(crimes) + " where d.name10='" + str(name10) + "';"
    print(sql3)
    cur3.execute(sql3)
    
 
    if i%10000 == 0:
        print(i)
        conn.commit()
    row = cur.fetchone()

#df = pd.
conn.commit()
conn.close()

