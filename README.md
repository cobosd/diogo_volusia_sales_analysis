# Project Description

The goal of this repository is to determine and add crime information to each parcel within the sales_analysis table. All the information regarding crime occurrences were collected directly from the Volusia County Sheriff's Office website, meaning that the data in reliable.

Learning the crime statistics of a specific region can be interesting for different reasons.

New features added to this project are show below:

nbr_crimes -----> 'Integer' that depicts the total number of crimes that happened within 1200ft of that specific parcel

crime_desc -----> Feature of type 'text' which containg the description of nearest crime (ex: assault)

crime_dist -----> 'Text' variable containing the distance (miles) to the nearest crime described in crime_desc

crime_date -----> 'Date' variable that show year-month-day of the nearest crime 

The crimes occurrences utilized to determine the features just decribed can be seen in the following image where they are plotted on the Volusia County map after having their address converted into geographical coordinates (longitude, latitude). 

![image](https://user-images.githubusercontent.com/82676042/117323410-dba24080-ae5c-11eb-8690-cde6029e787b.png)


The methodology used to collect and determine the new attributes were based on python, postgres, and QGIS. The number of crimes within 1200ft of a parcel was determined with a python script that looped through each parcel and executed a combination of "ST_Buffer" and "ST_Within" queries, counting the exact number of crimes "within" a "1200 ft Buffer" of that parcel. For the remaining features, the python scrip was also needed, however, only only KNN query was required to find the nearest crime and pull up its information. From there, the distance could be converted to miles and the attributes where simply added to the new dataframe wherever the parcel id (parid) matched the one in the python loop.

It is important to note, however, that regions seen in the map containing _zero_ crimes might have that statistic due to software limitations, not because they are 100% safe. The software can only translate a full address (street, city) or (street, zip code) into coordinates, but many of the crime instances occurred in the Volusia County Sherrif's land and therefore did not have a specific city disclosed as information.

