from fastapi import FastAPI
from fastapi import status
import requests
import pytest

app = FastAPI()

class TestClass:
    def test_api_health(self):
        data = {
            "status_code": status.HTTP_200_OK,
            "details": {
                "author": {
                    "name": "Henrique Araujo Furtini",
                    "email": "furtiniprofissional@gmail.com"
                }
            }
        }
        api_url = "http://127.0.0.1:8000/health"
        api_request = requests.get(api_url).json()
        assert data == api_request
            
