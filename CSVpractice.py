#https://youtu.be/cXP_i5-nTXg?t=1214
#import numpy as np
import pandas as pd

content = pd.read_csv('revenue-profit.csv', sep = ";") #sep is what separates the columns
print(content.head()) #head is only first 5 rows

content = content.rename(columns={'no_data':'Year'}) #Rename column name
print(content.head())

singleYear = content[content.Year == 2012] #Only columns with the year == 2012
print(singleYear)