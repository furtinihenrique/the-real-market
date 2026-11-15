from fastapi import FastAPI
from fastapi import status
import api.schemas.brent.brentRequest as brentRequest
import brent_data
import services.brentCalculus as brentCalculus

#Start the API
app = FastAPI()

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

#/brent route
@app.post("/brent")
async def get_data_filtered(requestModel: brentRequest.RequestModel):
    brent_data.get_brent_data()
    filtered_dates, last_requested_price = brent_data.read_csv(requestModel.start_date, requestModel.end_date)
    normalized_data = brent_data.normalize_brent_data(filtered_dates)
    prices = brent_data.get_only_prices(normalized_data)
    total_variation = brentCalculus.calculate_total_return(prices)
    average_price = brentCalculus.average_price(prices)
    
    return {
        "total_variation" : total_variation,
        "average_price" : average_price,
        "last_date_requested_price" : last_requested_price
    }

@app.get("/brent/lastest")
def get_last_infos():
    last_price, last_date = brent_data.get_last_price()
    return {
        "last_price": last_price,
        "last_date": last_date
    }

     
