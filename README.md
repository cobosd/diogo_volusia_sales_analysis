# Project Description

The goal of this repository is to determine and add crime information to each parcel within the sales_analysis table. All the information regarding crime occurrences were collected directly from the Volusia County Sheriff's Office website, meaning that the data in reliable.

Learning the crime statistics of a specific region can be interesting for differentreasons. Perhaps you want to purchase a property but first you'd like to make sure the area is safe enough for your familiy, or maybe you simply want to study the demographics of a region and understand how that influences its safety.

New features added to this project are show below:

nbr_crimes -----> 'Integer' that depicts the total number of crimes that happened within 1200ft of that specific parcel

crime_desc -----> Feature of type 'text' which containg the description of nearest crime (ex: assault)

crime_dist -----> 'Text' variable containing the distance (miles) to the nearest crime described in crime_desc

crime_date -----> 'Date' variable that show year-month-day of the nearest crime 

The crimes occurrences utilized to determine the features just decribed can be seen in the following image where they are plotted on the Volusia County make after having their address converted into geographical coordinates (longitude, latitude). 

![image](https://user-images.githubusercontent.com/82676042/117323410-dba24080-ae5c-11eb-8690-cde6029e787b.png)


The methodology used to collect and determine the new attributes were based on python, postgres, and QGIS. The number of crimes within 1200ft of a parcel was determined with a python script that looped through each parcel and executed a combination of "ST_Buffer" and "ST_Within" queries, counting the exact number of crimes "within" a "1200 ft Buffer" of that parcel. For the remaining features, the python scrip was also needed, however, only only KNN query was required to find the nearest crime and pull up its information. From there, the distance could be converted to miles and the attributes where simply added to the new dataframe wherever the parcel id (parid) matched the one in the python loop.

It is important to note, however, that regions seen in the map containing _zero_ crimes might have that statistic due to software limitations, not because they are 100% safe. The software can only translate a full address (street, city) or (street, zip code) into coordinates, but many of the crime instances occurred in the Volusia County Sherrif's land and therefore did not have a specific city disclosed as information.


*------------------------------------------------------------ABOUT THE FILES------------------------------------------------------------------*

How to add crime data from Volusia county (Florida) into a sales analysis table to create a crime_sales_analysis table:

"Volusia SA - Crime Table.pdf" is a short presentation taking you step by step on how to add crime_sales_analysis to your pgAdmin. It basically asks to download zip file in this repository and run a command on command prompt.



Zip file contains two folders:

1. add_new_sales_analysis:
  this will create a new crime_sales_analysis table in your pgAdmin which contains information about crimes around each parcel of the original sales_analysis table.
 
2. create_crime_table [optional]:
  create a new table that contains only information about crimes that happened within volusia county in the past 6 months. Concluding the steps in this folder is not
  required to complete part 1 (add_new_sales_analysis).
