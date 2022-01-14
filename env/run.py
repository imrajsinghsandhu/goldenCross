import os, sys, argparse #cli libraries 
import pandas as pd
import backtrader as bt
from strategies import goldencross

# you will basically throw strategy classes in this script for backtrader to run 

cerebro = bt.Cerebro()
cerebro.broker.setcash(100000)

spy_prices = pd.read_csv('c:/Users/Imraj/Desktop/goldencross/env/data/spy_goldencross.csv', index_col='Date', parse_dates=True)

# creating a feed to be used by backtrader 
feed = bt.feeds.PandasData(dataname=spy_prices)
cerebro.adddata(feed)
cerebro.addstrategy(goldencross.GoldenCross)
cerebro.run()
cerebro.plot(volume=False)