## Stock and option data analytics
#### In current project, I built a program which could be employed by quants in analysing the stocks and options.  

#### For Stock data analysis, program performs following tasks:
*	Retrieving data of chosen stock through pandas DataReader, and plotting it
*	Gives a  table with statistical analysis and tests of the stock(mean, st.dev, skewness, kurtosis) and plot mean return, volatility and correlation graphs
*	Plotting Moving Average crossover and Stochastic Oscillator to identify closest trading signal. For a short MA we use n=20, for a long n=50.
*	Check profitability of MA crossover and Stochastic oscillator strategies for a current stock. For this reason P&L and Sharpe Ratio will be used as measures of profitability.

#### Along with Stock analysis, our program  also conducts analysis of Option on the same stock. We employ assumptions of constant *risk free rate (r)* =0.05, *maturity (T)*, 1 year and *Strike price (K)* 100.  Following tasks are performed:
*	Computation of option price with Black-Scholes model and plot graphs with respect to parameters
*	Calculation and plotting of Greeks(sensitivities) of the option
* Valuation of option using Monte Carlo Simulation

#### Input parameters include:
For Stock data analysis: 
1.	Name of the ticker(e.g. ‘AAPL’) , 
2.	Starting date of historical data = ‘01/03/2013’ and Ending date= ‘16/03/2017’ 
3.	length of short MA = 20, length of long MA=50. 

For Option Analysis:
1.	Stock’s current price from Yahoo Finance
2.	Volatility =0.1
3.	r=0.05, 
4.	T =1  
5.	K=100

#### Ouput  parameters include:
- Plots of stock’s mean return, volatility and correlation, Moving Average crossover and Stochastic Oscillator
- Table with stock’s  mean, standard deviation, skewness and kurtosis
- Table with P&L and Sharpe Ratio for Stochastic Oscillator and Moving Average strategies
- Table with option prices computed by Monte Carlo and Black Sholes 
- Table with Delta, Gamma, Theta, Vega of the option 
- Plots of  Delta, Gamma, Theta, Vega  

#### All table data are exported in Excel file using Pandas’ ExcelWriter feature.


#### Here are the output plots
![1](https://user-images.githubusercontent.com/59889139/132145503-2f79d2c6-3713-4127-a39c-b9ccf14c7eb3.png)
![2](https://user-images.githubusercontent.com/59889139/132145504-3cfc6038-f1f9-46b0-aede-63b49b9620c2.png)
![3](https://user-images.githubusercontent.com/59889139/132145505-ce77475c-91dc-4351-9b1e-baa75b9697e9.png)
![4](https://user-images.githubusercontent.com/59889139/132145507-d2fd3d52-54e4-442e-baa4-8e6e716e12a0.png)
