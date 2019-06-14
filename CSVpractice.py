#https://www.youtube.com/watch?v=cXP_i5-nTXg&list=PL55RiY5tL51o5jBXR1h2JvFm0L-fbThG4
#On video 2 at 0 minutes
#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

content = pd.read_csv('revenue-profit.csv', sep = ";") #sep is what separates the columns
#print(content.head()) #head is only first 5 rows

content = content.rename(columns={'no_data':'Year'}) #Rename column name
#print(content.head())

singleYear = content[content.Year == 2012] #Only columns with the year == 2012
#print(singleYear)

singleColumn = content[['Revenue', 'Profit']] #Only columns
#print(singleColumn)

showLoc = content.loc[2:3,["Revenue","Profit"]] #show rows 2 through 3 and specific columns
#print(showLoc)

#print(content.describe()) #High level data about the data

plt.plot(content.Year, content.Revenue) #Use MatPlotLib to plot a chart. (matplotlib.org)
plt.xlabel('Year')
plt.ylabel('Revenue')
plt.show()