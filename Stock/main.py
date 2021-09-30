# import pandas as pd
# from pandas_datareader import data as web
# import datetime as dt
# from sklearn.preprocessing import scale
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# import numpy as np
# import matplotlib.pyplot as plt
# from mplfinance import plot as pltcandle
# import pickle


# Import These ^^^


class Stock:
    def __init__(self, ticker, start, end, loc='upper left'):
        self.ticker = ticker
        self.start = start
        self.end = end
        self.loc = loc
        # Used in predict to get data from a certain number of days
        self.X = None
        # Used to pass fdays from predict to show_pred
        self.pred_days = None
        self.data = web.DataReader(self.ticker, 'yahoo', self.start, self.end)

    # It's used often so made a method for it
    def graph_settings(self, title):
        fig, ax = plt.subplots()
        fig.autofmt_xdate()
        plt.xlabel('Dates')
        plt.ylabel('Price')
        plt.title(title)

    def view(self, candle):
        if candle:
            pltcandle(self.data, type='candle', style='yahoo', warn_too_much_data=100000000000000000000000000)
            return
        data = self.data['Adj Close']
        fig, ax = plt.subplots()
        fig.autofmt_xdate()
        plt.plot(data)

    def cmp(self, tickers):
        self.graph_settings(f'Comparison between {self.ticker} and others')
        plt.plot(web.DataReader(self.ticker, 'yahoo', self.start, self.end)['Adj Close'], label=self.ticker)
        for ticker in tickers:
            tk = web.DataReader(ticker, 'yahoo', self.start, self.end)['Adj Close']
            plt.plot(tk, label=ticker)
        plt.legend(loc=self.loc)

    def show(self):
        plt.show()

    def mk_model(self, days, rd_state=None):
        # Shifts the data by the number of days to be used as Y
        self.data['Shifted'] = self.data['Adj Close'].shift(-days)
        self.data.dropna(inplace=True)
        # Turns Adj Close and converts it to an array and scales it down
        X = scale(np.array(self.data['Adj Close']))
        self.X = X
        Y = np.array(self.data['Shifted'])
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=rd_state)
        lr = LinearRegression()
        lr.fit(X_train.reshape(-1, 1), Y_train.reshape(-1, 1))
        acc = lr.score(X_test.reshape(-1, 1), Y_test.reshape(-1, 1))
        return lr, acc

    def sv_model(self, svname, model):
        with open(svname, 'wb') as file:
            pickle.dump(model, file)

    def load_model(self, svname):
        with open(svname, 'rb') as file:
            model = pickle.load(file)
            return model

    def predict(self, model, fdays):
        self.pred_days = fdays
        new = self.X[-fdays:].reshape(-1, 1)
        res = model.predict(new)
        return res

    def show_pred(self, predictions, plot=True):
        prd = self.end + dt.timedelta(days=self.pred_days - 1)
        dates = pd.date_range(self.end, prd)
        if not plot:
            return dates
        self.graph_settings(f'Prediction for {self.ticker} from {str(self.end)[:10]} to {str(prd)[:10]}')
        plt.plot(dates, predictions, color='orange')

    # Only to be used when you're using older dates
    # To check the models relative accuracy
    def cmp_pred(self, predictions, prin=False):
        dates = self.show_pred(predictions, plot=False)
        actual = web.DataReader(self.ticker, 'yahoo', start=dates[0], end=dates[-1])['Adj Close']
        if prin:
            print(actual)
        self.graph_settings(f'Comparison between the actual {self.ticker} price and the predicted')
        plt.plot(actual, label='actual')
        plt.plot(dates, predictions, label='predictions')
        plt.legend(loc=self.loc)


# Simple examples of how this should be used

if __name__ == '__main__':
    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2021, 6, 26)
    apple = Stock('AAPL', start, end)
    lr, acc = apple.mk_model(50)
    preds = apple.predict(lr, 50)
    tickers = ['FB', 'MSFT']
    apple.cmp(tickers)
    apple.cmp_pred(preds)
    # apple.load_model('model.pickle',lr)
    apple.show()
