import pandas as pd

def transform_orders():

    df = pd.read_parquet("orders.parquet")

    df["order_date"] = pd.to_datetime(df["order_date"])

    df["year"] = df["order_date"].dt.year

    df["month"] = df["order_date"].dt.month

    df.to_parquet("orders_transformed.parquet")

    print("Orders transformed")
    