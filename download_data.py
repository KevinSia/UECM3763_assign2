from pandas.io.data import DataReader as DR
import pandas as pd
from datetime import datetime as dt
import pylab as p

#obtaining data

start = dt(2012, 1, 1)
end = dt(2015, 7, 20)
closing_data = DR("1295.KL", 'yahoo', start, end)['Close']
    #Public Bank's closing stock prices from 2012 to 2015 is extracted

#calculating moving average

avg_days = 5
moving_avg = pd.rolling_mean(closing_data,avg_days)

#plotting moving average and stock price
joined_data = pd.concat([moving_avg,closing_data], axis = 1)
    # to merge moving average and closing price into one DataFrame
joined_data[['Moving average','Stock price']] = joined_data[[0,1]]
joined_data[['Moving average','Stock price']].plot(title = '%d-days moving average of stock 1295.KL'%avg_days)
    

#Correlation between prices of 1295.KL and KLCI index

combine=['1295.KL','^KLSE']
closing = DR(combine, 'yahoo', start, end)['Close']
    # a combined dataframe of closing prices is extracted

correlation = p.array(closing.corr())[0,1]
print('\nThe correlation between 1295.KL and KLCI is %f' %correlation)
