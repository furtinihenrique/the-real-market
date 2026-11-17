import brent_data as bd
from decimal import *
import pandas as pd

def calculate_total_return(prices_list):
    actual_price = prices_list[len(prices_list)-1]
    first_price = prices_list[0]
    total_return = ((actual_price - first_price)/first_price) * 100
    return (round(total_return, 3))

def average_price(prices_list):
    lenght = len(prices_list)
    total_sum = 0
    for price in prices_list:
        total_sum += price
    return round(Decimal(1/lenght) * total_sum, 3)

def cumulative_return(prices_list):
    lenght = len(prices_list)
    return (prices_list[lenght]/prices_list[0]) - 1 * 100

def dialy_return(prices_list):
    return pd.Series.pct_change(prices_list)

def volatility(prices_list):
    return pd.Series.std(prices_list, ddof=1)