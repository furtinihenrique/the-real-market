from fastapi import FastAPI
from fastapi import status
from enum import StrEnum
from pydantic import BaseModel, ConfigDict
from pathlib import Path
import get_brent_data



#Start the API
app = FastAPI()

#Classes for requests 
"""
class Commodity(StrEnum):
    BRENT = "BRE"

class RequestModel(BaseModel) :
    model_config = ConfigDict(extra='allow')

    commodity: Commodity
    start_date: datetime.date
    end_date: datetime.date
"""

#Default route for tests
@app.get("/health")
def health_test():
    data = {
        "status_code": status.HTTP_200_OK,
        "details": {
            "author": {
                "name": "Henrique Araujo Furtini",
                "email": "furtiniprofissional@gmail.com"
            }
        }
    }
    return data

@app.get("/brent")
def get_data():
    return get_brent_data.get_brent_data()
    
     
