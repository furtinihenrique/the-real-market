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
    normalized_data = brent_data.normalize_brent_data(brent_data.read_csv(requestModel.start_date, requestModel.end_date))
    prices = brent_data.get_only_prices(normalized_data)
    total_variation = brentCalculus.calculate_total_return(prices)
    average_price = brentCalculus.average_price(prices)
    return (f"Total variation in the period: {total_variation}% and average price ${average_price}")

     
