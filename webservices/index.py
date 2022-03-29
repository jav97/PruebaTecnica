import pandas as pd
import requests 

BASE_URL = 'https://fakestoreapi.com'

query_params = {
    "limit": 1
}

response = requests.get(f"{BASE_URL}/products", params = query_params)
print(response.json())
print(response.status_code)