import requests
import pandas as pd

def fetch_products():

    url = "https://fakestoreapi.com/products"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data)

    df.to_parquet("products.parquet")

    print("Products data saved")