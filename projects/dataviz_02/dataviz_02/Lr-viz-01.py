import pandas as pd 
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt 
from matplotlib import style
style.use('ggplot')
start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2017, 12, 12)
df = web.DataReader("XOM", "yahoo", start, end)
#print(df.tail())
df['Adj Close'].plot()
plt.show()