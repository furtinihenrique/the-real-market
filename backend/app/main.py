from fastapi import FastAPI
from fastapi import status
import brent_data

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

@app.get("/brent")
def get_data():
    brent_data.get_brent_data()
    brent_data.read_csv("2026-10-22", "2026-10-26")
    
     
