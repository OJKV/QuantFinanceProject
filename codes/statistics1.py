import numpy as np
import pandas as pd
import scipy.stats as scs
import pandas_datareader.data as web  
import datetime
import matplotlib.pyplot as plt
import math
 

class statistics(object):

 def __init__(self, ticker, y1, m1, d1, y2, m2, d2):
    self.ticker=ticker
    self.y1=y1
    self.m1=m1
    self.d1=d1
    self.y2=y2
    self.m2=m2
    self.d2=d2

  


 def stat(self):

  start = datetime.datetime(self.y1,self.m1,self.d1)
 
  end = datetime.datetime(self.y2,self.m2,self.d2)

  dates=pd.date_range(start,end)
  df1=pd.DataFrame(index=dates)
 
 

  stock = web.DataReader(self.ticker, "yahoo", start, end)
  stock['returns'] = np.log(stock['Adj Close'] / stock['Adj Close'].shift(1))

  df=pd.DataFrame({'Statistics':[np.mean(stock['returns']), np.std(stock['returns']), np.mean(stock['returns']) * 252,
                 np.std(stock['returns']) * math.sqrt(252),scs.skew(stock['returns'], nan_policy='omit'), scs.kurtosis(stock['returns'], nan_policy='omit')]},
                index=['Mean of Daily Log Returns','Std of Daily Log Returns', 'Mean of Annual. Log Returns',
                       'Std of Annual. Log Returns','Skewness', 'Kurtosis'])#table of final results
  writer=pd.ExcelWriter('output2.xlsx')
  df.to_excel(writer,'Sheet1')
  writer.save()#Saving in Excel file
  
  plt.figure(figsize=(11, 8))
  plt.subplot(3,1,1)

  m=stock['returns'].rolling(center=False,window=252).mean()
  m.plot()
  plt.grid(True)
  plt.ylabel('mean (252d)')

  plt.subplot(3,1,2)# nrows, ncols, plot_number
 
  vo= stock['returns'].rolling(center=False,window=252).std()
  vo.plot()

  plt.grid(True)
  plt.ylabel('volatility (252d)')
 

  plt.subplot(3,1,3)
 
  cor=m.rolling(window=252).corr(vo)
  cor.plot()
  plt.grid(True)
  plt.ylabel('correlation (252d)')

  return plt.show() 

    
       

 
 

