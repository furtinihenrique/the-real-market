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

"""
    for day in dates:
        if day["Date"] == start_date:
            i = dates[day]
            print(i)
"""      


