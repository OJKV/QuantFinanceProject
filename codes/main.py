import numpy as np
import pandas as pd
import pandas_datareader.data as web  
import datetime
import matplotlib.pyplot as plt
import strategy3  
import plot  
from statistics1 import statistics
from Option_pricing import *
from Option_greeks import *

s=strategy3.strategy("^GSPC",2013,3,1,2017,3,16)
k=plot.plot("AAPL",2013,3,1,2017,3,16)
s1=statistics("^GSPC",2013,3,1,2017,3,16)
 
k.ma(20,50)#plot Moving Average Crossoer

s1.stat() # compute statisitcs and plot mean, std, correlation 

Sharpe_pnl=s.ma(20,50).append(s.stochastic())#Table with P&L and Sharpe Ratio

writer=pd.ExcelWriter('output1.xlsx')
Sharpe_pnl.to_excel(writer,'Sheet1')
writer.save()

St = 140.460007 # current stock price 
K = 100.0 # option strike
T = 1.0 # maturity date
r = 0.05 # risk-less short rate
sigma = 0.2 # volatility
I = 100000 #number of simulations

Monte=mc(St, K, T, r, sigma,I)
BS=BSM_call_value(St, K, T, r, sigma)

df=pd.DataFrame({'Option prices':[Monte, BS]},
                index=['Monte Carlo','Black Scholes'])#Table with option prices
 
writer=pd.ExcelWriter('output3.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()

plot_option(St,K,T,r,sigma)# plot sensitivity graphs

Delta=BSM_delta(St, K, T, r, sigma)
Gamma=BSM_gamma(St, K, T, r, sigma)
Theta=BSM_theta(St, K, T, r, sigma)
Vega=BSM_vega(St, K, T, r, sigma)

df2=pd.DataFrame({'Greeks':[Delta, Gamma,Theta,Vega]},
                index=['Delta','Gamma','Theta','Vega'])#Table with option prices

writer=pd.ExcelWriter('output4.xlsx')
df2.to_excel(writer,'Sheet1')
writer.save()

plot_greeks(St, K, T, r, sigma)


 


