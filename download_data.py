from pandas.io.data import DataReader as DR
from datetime import datetime as dt
import pylab as p
import numpy as np

start = dt(2010, 1, 1)
end = dt(2013, 12, 31)
data = DR("1295.KL", 'yahoo', start, end)
    #public bank data from 2010 to 2013 is downloaded

data = p.array(data)
closing = data[:,3]
sum = closing.cumsum()

avg_days = 5

matrix = np.zeros((2,(len(sum)-avg_days+1)))
matrix[0,:] = sum[(avg_days-1):]
matrix[1,1:] = sum[:-(avg_days)]

moving_avg = (matrix[0] - matrix[1])/avg_days

days = len(closing)



p.plot(moving_avg)
p.plot(closing)
label = 'Days' ; p.xlabel(label)
label = 'Stock price' ; p.ylabel(label)
p.title('%d-days moving average of Public Bank Berhad from Jan 1,2010 to Dec 31,2013'%avg_days)
p.show()

