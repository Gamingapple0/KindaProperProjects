from pandas_datareader import data as web
import datetime as dt
from pandas import Timestamp
from sklearn.preprocessing import scale
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from matplotlib.dates import date2num
from matplotlib import style
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# style.use('ggplot')
# ls = []
# for i in range(1,4):
#     tm = [dt.datetime(2020,1,i)]
#     ls.append(tm)
# ls = list(map(date2num,ls))
# # b = np.array([[1,2,3],[4,5,6],[7,8,9]])
# b = np.array([1,2,3])
# fig,ax = plt.subplots()
# fig.autofmt_xdate()
# ax.plot(ls,b,'o')
# ax.grid(True)
# ax.xaxis_date()
#
# plt.show()
#
# start1 = dt.datetime(2021, 9, 20)
# end1 = dt.datetime(2021, 9, 24)
# actual = web.DataReader('AAPL', 'yahoo', start1, end1)
# actual = np.array(actual['Adj Close'])
# print(actual)
start = dt.datetime(2020,1,1)
end = dt.datetime(2020,4,1)
# apple = web.DataReader('AAPL','yahoo',start,end)['Adj Close']
pred = [[139.20947886],[139.75774595],[141.52081573]]
# dates = []
# for i in range(1,2):
#     year = 2020
#     ts = Timestamp(2019, i, 1)
#     days = ts.days_in_month
#     for j in range(1,days):
#         dates.append([Timestamp(year,i,j)])
    # dates = [[Timestamp(2019,1,1)],[Timestamp(2019,1,2)],[Timestamp(2019,1,3)]]
# print(dates)
# fig,ax = plt.subplots()
# fig.autofmt_xdate()
# plt.plot(dates,pred)
# plt.show()
data = web.DataReader('AAPL','yahoo',start,end)
data['Shifted'] = data['Adj Close'].shift(-4)
dates = pd.date_range(start,end)
data[['Adj Close','Shifted']].to_csv('bleh.csv',sep=' ')
# fig, ax = plt.subplots()
# fig.autofmt_xdate()
# plt.plot(dates,pred)
# plt.show()
a = 1
