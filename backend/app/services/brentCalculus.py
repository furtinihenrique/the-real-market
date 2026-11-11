import brent_data as bd
from decimal import *

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
    