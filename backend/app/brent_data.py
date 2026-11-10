from pathlib import Path
from dotenv import  load_dotenv
from decimal import *
import os
import csv

import httpx

load_dotenv()

#Data retrieval
def get_brent_data():
    brent_api_url = os.getenv("BRENT_CSV_URL")
    response = httpx.get(brent_api_url, follow_redirects=True)
    Path("brent-daily.csv").write_bytes(response.content)
    return "Brent data loaded!"


def read_csv(start_date, end_date):
    dates = []
    with open("brent-daily.csv", "r") as file:
        data = csv.DictReader(file)
        for row in data:
            dates.append(row)

    found_start_date = False
    found_end_date = False
    i = -1
    start_date_index = 0
    end_date_index = 0
    for day in dates:
        i += 1
        if day["Date"] == str(start_date):
            start_date_index = i
            found_start_date = True
        
        if day["Date"] == str(end_date):
            end_date_index = i
            found_end_date = True
            break

    if found_start_date == False or found_end_date == False: return "Invalid date"
        

    required_dates_data = []
    sentinel = True
    while(sentinel):
        required_dates_data.append(dates[start_date_index])
        if(start_date_index == end_date_index): sentinel = False
        start_date_index += 1

    return required_dates_data
