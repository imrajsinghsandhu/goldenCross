import math
import backtrader as bt 
import datetime

class GoldenCross(bt.Strategy):
    params = (('fast', 50 ), ('slow', 200), ('order_percentage', 0.95), ('ticker', 'SPY'))

    # initialising the strategy with indicators 
    def __init__(self):
        self.fast_moving_average = bt.indicators.EMA(
            self.data.close, period=self.params.fast, plotname='50 day moving average'
        )

        self.slow_moving_average = bt.indicators.SMA(
            self.data.close, period=self.params.slow, plotname='200 day moving average'
        ) 

        self.crossover = bt.indicators.CrossOver(self.fast_moving_average, self.slow_moving_average)

    def next(self):
        if self.position.size == 0:
            if self.crossover > 0:
                # you are going to now invest 95% of your wealth 
                amount_to_invest = (self.params.order_percentage * self.broker.cash)
                self.size = math.floor(amount_to_invest/self.data.close) 
                dt = self.datas[0].datetime.date(0)

                print("{}: Buy {} shares of {} at {}".format(dt ,self.size, self.params.ticker, self.data.close[0]))

                self.buy(size=self.size)

        if self.position.size > 0:
            if self.crossover < 0:
                dt = self.datas[0].datetime.date(0)

                print("{}: Sell {} shares of {} at {}".format(dt, self.size, self.params.ticker, self.data.close[0]))
                self.close()

# 2016-01-11: Sell 1089 shares of SPY at 192.110001
# 2016-04-25: Buy 1025 shares of SPY at 208.610001
# 2018-12-07: Sell 1025 shares of SPY at 263.570007
# 2019-04-01: Buy 933 shares of SPY at 285.829987
# 2020-03-30: Sell 933 shares of SPY at 261.649994
# 2020-07-09: Buy 776 shares of SPY at 314.380005
