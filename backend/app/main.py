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

@app.post("/brent")
async def get_data_filtered(requestModel: brentRequest.RequestModel):
    start_date = requestModel.start_date
    end_date = requestModel.end_date
    brent_data.get_brent_data()
    data = brent_data.get_only_prices(brent_data.normalize_brent_data(brent_data.read_csv(start_date, end_date)))
    total_variation = brentCalculus.calculate_total_return(data)
    return (f"Total variation in the period: {total_variation}%")
    
     
