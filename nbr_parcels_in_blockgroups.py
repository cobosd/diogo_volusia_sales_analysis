# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 19:01:45 2021

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
cur4 = conn.cursor()



sql = "select objectid from volusia.bg_census" # limit 10"

print('SQL: ', sql)
cur.execute(sql)

# one way grab all the data into a multi-dimensional array
data = cur.fetchall()
#actual_data = data[0][0]

# I like to fetch one row at a time like reading data from a file
i=0
# row = cur.fetchone()

for row in data:
    i = i + 1
    print(i)
    
    objid = str(row[0])
    
    
    
    #----------get number of parcels
    sql2 = "select count(*) from volusia.myparcels c, volusia.bg_census p where p.objectid = '" + str(objid) + "' and ST_Within(c.geom, p.geom);"
    cur2.execute(sql2)
    row2 = cur2.fetchone()
    
    #---------get info on parcels
    # sql2 = "select c.* from volusia.myparcels c, volusia.bg_census p where p.objectid = '" + str(objid) + "' and ST_Within(c.geom, p.geom);"
    # cur2.execute(sql2)
    # row2 = cur2.fetchone()

    if row2 != None:
        nbr_parcels = row2[0]
    else:
        nbr_parcels = 0
    
    
    
    
    sql3 = "update volusia.bg_census d set nbr_parcels = " + str(nbr_parcels) + " where d.objectid='" + str(objid) + "';"
    # print(sql3)
    cur3.execute(sql3)
    
 
    if i%10000 == 0:
        print(i)
        conn.commit()
    row = cur.fetchone()

#df = pd.
conn.commit()
conn.close()
