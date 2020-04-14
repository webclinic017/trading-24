import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import urllib3
import bs4 as bs
import pickle
import requests
import webbrowser
import datetime as dt
import scipy.optimize as spo
from statsmodels import regression
import statsmodels.api as sm

from pandas_datareader import data as pdr
from numpy import asarray
from numpy import savetxt

import yfinance as yf
if __name__ == "__main__":
    start = '2017-11-01'
    end = '2019-11-01'
    ticker = 'AAPL'
    # df = pdr.get_data_yahoo(ticker, start=start, end=end)
    
    # define data
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # save to csv file
    savetxt('data.csv', data, delimiter=',')