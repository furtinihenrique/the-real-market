import api.schemas.brent.brentRequest as brentRequest
import pytest
import requests
from fastapi import status

class TestForBackend:
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

    def test_valid_date_false(self):
        data = {
            "commodity": "BRE",
            "start_date": "2025-02-01",
            "end_date": "2025-01-01"
        }
        api_url = "http://127.0.0.1:8000/brent"
        api_request = requests.post(api_url,json=data)
        assert api_request.status_code == 422

    def test_valid_date_correct(self):
        data = {
            "commodity": "BRE",
            "start_date": "2025-02-01",
            "end_date": "2026-01-01"
        }
        api_url = "http://127.0.0.1:8000/brent"
        api_request = requests.post(api_url,json=data)
        assert api_request.status_code == 200

