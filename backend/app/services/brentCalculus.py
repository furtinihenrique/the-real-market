import brent_data as bd

def calculate_total_return(prices_list):
    actual_price = prices_list[len(prices_list)-1]
    first_price = prices_list[0]
    total_return = ((actual_price - first_price)/first_price) * 100
    return (round(total_return, 3))
    