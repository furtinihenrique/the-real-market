from pydantic import BaseModel, ConfigDict
from pathlib import Path
from dotenv import  load_dotenv
from enum import StrEnum
from decimal import *
import os
import csv
import datetime
import httpx

load_dotenv()

#Classes for requests 
class Commodity(StrEnum):
    BRENT = "BRE"


class RequestModel(BaseModel) :
    model_config = ConfigDict(extra='allow')

    commodity: Commodity
    start_date: datetime.date
    end_date: datetime.date

class ResponseModel(BaseModel):
    commodity: Commodity
    date: datetime.date
    price: Decimal

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

    i = 0
    start_date_index = 0
    end_date_index = 0
    for day in dates:
        i += 1
        if day["Date"] == start_date:
            start_date_index = i
        elif day["Date"] == end_date:
            end_date_index = i

    required_dates_data = []
    sentinel = True
    while(sentinel):
        required_dates_data.append(dates[start_date_index])
        if(start_date_index == end_date_index): sentinel = False
        start_date_index += 1

    print(required_dates_data)


