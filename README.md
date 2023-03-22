## Project-4_World Refugee Migration Trends and Predictions

![image](https://user-images.githubusercontent.com/113714205/226762476-fc712adc-19bd-4047-bfc6-7fd9f07a6db2.png)

Project 4:

Team Members:   Rahma Ali, Nicholas Erdos-Thayer, Chris Schultz,  Art Rogers

# Project Background and Sources:

Our project aims to analyze data provided by the United Nations Refugee Agency (UNHCR) and other sources to gain insights into migration patterns and to develop a machine learning model to focus on refugee populations. The data includes information on refugee populations, demographic information (gender & age), asylum decisions, conflict and disasters impacting refugee populations around the world. We hope to gain a deeper understanding of the factors that influence migration flows and develop predictions of future migration patterns.

**Refugee Summary:**
In the past decade, the global refugee crisis has more than doubled in scope. In 2022, the UNHCR announced that we had surpassed the 100 million mark for total displaced persons, meaning that over 1.2% of the global population have been forced to leave their homes. Among these people are over 32.5 million refugees. 76% of those refugees come from just six countries. Before we look at the world’s largest refugee crises, a quick note that we’re focusing specifically on refugees and counting them by country of origin for this listing

# Technology Used
•	Flask
•	HTML
•	CSS
•	Java Script
•	Decision Tree Classifier
•	Random Forest Classifier
•	Pandas
•	SQLite
•	Tableau


# Data Sources:
Our data sources show conflict and disaster are the two major types of refugee populations.

•	**Refugee Demographic Data** - The United Nations Refugee Agency (UNHCR ) collects data on refugee’s around the world - https://www.unhcr.org/refugee-statistics/download/?url=Kg1Mg6

•	**Conflict Data** - Uppsala Conflict Data Program - Department of Peace and Conflict Research - https://ucdp.uu.se/

•	**Disaster Data** - Centre for Research on the Epidemiology of Disasters - https://www.emdat.be/

# Data Limitations:

•	**Data standardization:** The use of different methods for counting refugee populations, 
which can make it difficult to compare data across different sources. For example, 
some organizations may use different definitions of "refugee" or "asylum seeker," 
which can lead to confusion and inconsistencies in data analysis.

•	**Bias:** not all refugees live in informal settlements. Therefore, those who live outside 
of refugee’s camps might not be represented in the data collection.

•	**Limited access to data on conflict:** affected areas in eastern Ukraine due to security 
concerns and restrictions on movement.

•	**Time sensitivity:** Turkey Earthquake challenges in collecting accurate data on the 
number of casualties and damage to infrastructure in the immediate aftermath of the 
earthquake due to limited access and time sensitivity.

•	**Lack of historical data:** Limited access to data on conflict affected areas in Ukraine 
and challenges in collecting accurate data on the number of casualties and damage to 
infrastructure in Turkey Earthquake.


 # Data Cleaning
 The data cleaning process involved identifying missing data, correcting inconsistencies, removing duplicates, irrelevant data, standardizing and scaling the data. The resulting cleaned dataset was suitable for further analysis and can be used to gain insights into the patterns, trends and future prediction of refugee migration. 

**Example of uncleaned data**
 
![image](https://user-images.githubusercontent.com/113312408/226767144-787db2ec-2de2-4942-867d-132c8500d308.png)

**Example of cleaned data**

![image](https://user-images.githubusercontent.com/113312408/226766928-bdd77fd0-1682-471c-b526-56af3fe17590.png)

 #  Database
Created SQLite tables to store and retrieve the data. Created a database schema with primary and secondary keys and documented the schema in Quick Database Diagrams application.

**Tables:**
1.	Table 1 -Demographic_ml
2.	Table 2 – Event_ml
3.	Table 3- Cleaned_conflict
4.	Table 4 –Cleaned_disasters

![image](https://user-images.githubusercontent.com/113312408/226196244-7c66b085-c3f8-4512-bb7f-a54b80c58ddd.png)

# Tableau Metrics, Maps & Graphs:
Created 4 areas of focus to capture the refugee metrics and to show countries with the greatest impacts from conflicts or disasters.
 
 **Observation 1 Demographics:**
  •	The Demographic graphs demonstrates the ages, gender and overall volume of the refugee crisis
   ![image](https://user-images.githubusercontent.com/113714205/226493646-4230440a-3c06-4147-9621-569fef31820d.png)
  
  **Observation 2:**
  •	This map shows the countries with the greatest impacts from conflicts and disasters. 
  ![image](https://user-images.githubusercontent.com/113714205/226493951-f280cf5f-b3f1-48cf-aa1c-f5be076f494f.png)
  
  **Observation3:**
  This graphical shows Refugee Movement
  ![image](https://user-images.githubusercontent.com/113714205/226493823-a0cd46ee-71a1-476e-8632-0e8faf491cb9.png)


# Web Site:
We used HTML and CSS to design the site and a highlight able navigation bar to navigate to different pages of the website.  For the graphical representations we embedded Tableau slides to demonstrate our data.


![image](https://user-images.githubusercontent.com/113714205/226765350-b2810ebf-11cb-4566-911b-a215f0541a89.png)



# Machine Learning: 
    •	Out machine learning was in sections highlighted below.
    •	Loading the cleaned data
    •	Used OneHot Encoder to transform the data
    •	Trained and scaled the data
    •	Used Linear Regression for the first regression model
    •	Used Random Forest Regression for the second regression model
    •	Used “model.predict” to make our prediction






 

