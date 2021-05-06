# Project Description

The goal of this repository is to determine and add crime information to each parcel within the sales_analysis table. All the information regarding crime occurrences were collected directly from the Volusia County Sheriff's Office website, meaning that the data in reliable.

Learning the crime statistics of a specific region can be interesting for differentreasons. Perhaps you want to purchase a property but first you'd like to make sure the area is safe enough for your familiy, or maybe you simply want to study the demographics of a region and understand how that influences its safety.

The new features added to this project are show below:

nbr_crimes -----> 'Integer' that depicts the total number of crimes that happened within 1200ft of that specific parcel
crime_desc -----> Feature of type 'text' which containg the description of nearest crime (ex: assault)
crime_dist -----> 'Text' variable containing the distance (miles) to the nearest crime described in crime_desc
crime_date -----> 'Date' variable that show year-month-day of the nearest crime 

![image](https://user-images.githubusercontent.com/82676042/117323410-dba24080-ae5c-11eb-8690-cde6029e787b.png)





Add crime data from Volusia county (Florida) into a sales analysis table.

Zip file contains two folders:

1. add_new_sales_analysis:
  this will create a new crime_sales_analysis table in your pgAdmin which contains information about crimes around each parcel of the original sales_analysis table.
 
2. create_crime_table [optional]:
  create a new table that contains only information about crimes that happened within volusia county in the past 6 months. Concluding the steps in this folder is not
  required to complete part 1 (add_new_sales_analysis).
