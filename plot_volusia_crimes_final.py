# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 11:46:27 2021

@author: dnaza
"""

from urllib.request import urlopen
import json
import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt



#Access file with information about US counties
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)


#============================================================================================
#Find index for Volusia County
for item in enumerate(counties['features']):
    if counties['features'][item[0]]['properties']['NAME'] == 'Volusia':
        print(item[0])
        
        df = counties['features'][776]['geometry']['coordinates']
  
lat = []
lon = []

#Create list for longitudes and latitudes
for coord in df[0]:
    lon.append(coord[0])
    lat.append(coord[1])





#==========================================================================================
#Create .shp file with polygons coordinates for Volusia county
lat_point_list = lat
lon_point_list = lon

polygon_geom = Polygon(zip(lon_point_list, lat_point_list))
crs = {'init': 'epsg:4326'}
polygon = gpd.GeoDataFrame(index=[0], crs=crs, geometry=[polygon_geom])       
print(polygon.geometry)

polygon.to_file(filename='polygon.geojson', driver='GeoJSON')
polygon.to_file(filename='polygon.shp', driver="ESRI Shapefile")

import folium
m = folium.Map([50.854457, 4.377184], zoom_start=5, tiles='cartodbpositron')
folium.GeoJson(polygon).add_to(m)
folium.LatLngPopup().add_to(m)
m





#==========================================================================================
#Run separate module to get coordinates of crimes (only one of the two lines below should be uncommented)
# exec(open('coordinates_from_address.py').read())
df = pd.read_csv('G:/MA 540 - Data Mining/PROJECT/crime_coord.csv')



#Create shape file with polygons coordinates for Volusia county
volusia = gpd.read_file('G:/MA 540 - Data Mining/PROJECT/polygon.shp')

#Define axis: In this case, Florida
gax = volusia.boundary.plot(color='black',edgecolor='red', alpha=1,linewidth=0.5,  figsize=(10,10))    

#Set higher definition/resolution for the image
plt.rcParams["figure.dpi"] = 700  


#define GeoPandas dataframe and plot GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df['LON'], df['LAT']))
gdf.plot(ax=gax, color='red', marker = 'o', markersize = 5, alpha = 0.1)
