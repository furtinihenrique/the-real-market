from pathlib import Path
from dotenv import  load_dotenv
from decimal import *
import datetime
import os
import csv
import httpx
import sys

load_dotenv()

#Data retrieval
def get_brent_data():
    brent_api_url = os.getenv("BRENT_CSV_URL")
    response = httpx.get(brent_api_url, follow_redirects=True)
    Path("brent-daily.csv").write_bytes(response.content)
    return "Brent data loaded!"


def read_csv(start_date, end_date):
    start_date_index = 0
    end_date_index = 0
    found_start_date = False
    found_end_date = False
    dates = []
    required_filtered_dates_data = []
    i = -1
    try:
        with open("brent-daily.csv", "r") as file:
            data = csv.DictReader(file)
            for row in data: 
                i+=1
                dates.append(row)

                if dates[i]["Date"] == str(end_date):
                    found_end_date = True
                    required_filtered_dates_data.append(dates[i])
                    break
                
                if dates[i]["Date"] == str(start_date):
                    start_date_index = i
                    required_filtered_dates_data.append(dates[i])

                if start_date_index != 0 and i > start_date_index:
                    required_filtered_dates_data.append(dates[i])
    except IOError:
        print("Error while opening the file.")
        sys.exit()

    if start_date_index == 0 or found_end_date == False: return "Invalid date"
    return required_filtered_dates_data

def normalize_brent_data(list):
    normalized_data = []
    format = '%Y-%m-%d'

    for item in list:
        normalized_data.append({'Date': datetime.datetime.strptime(item['Date'], format).date(), 'Price': Decimal(item["Price"])})
    return normalized_data

def get_only_prices(list):
    prices = []
    for item in list:
        prices.append(item["Price"])
    return prices