import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import style


style.use('ggplot')

web_stat = {'Day':[1,2,3,4,5,6],
            'Visitors': [50, 42, 56, 67, 78, 80],
            'Bounce Rate':[65, 75, 56, 67, 89, 34]}

df = pd.DataFrame(web_stat)
print(df)

df.set_index('Day', inplace=True) ##Sets Day column of the dataframe as index and assign to df
print(df.head(2))
print(df['Bounce Rate'])
#print(df.Bounce Rate) #Not possible but the other cols without a white spcae can be called the same way.
print(df.Visitors) #value can be reterived using . operator as well if col name has not white space.

print(df[['Visitors','Bounce Rate']]) # multiple cols can be reterived from Dataframe using double square.

# Convert a col from Dataframe to list
print(df.Visitors.tolist())
print(df['Visitors'].tolist()) #both performs the same operation
print(np.array(df[['Visitors','Bounce Rate']])) #this is how we can convert multiple cols into array

df2 = pd.DataFrame(np.array(df[['Visitors','Bounce Rate']])) #converting an array into a dataframe
print(df2)
print(df.info())