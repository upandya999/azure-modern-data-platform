import pandas as pd
import random
import datetime

def generate_orders():

    orders = []

    for i in range(1000):

        orders.append({
            "order_id": i,
            "customer_id": random.randint(1,100),
            "product_id": random.randint(1,20),
            "amount": random.randint(20,500),
            "order_date": datetime.date.today().isoformat()
        })

    df = pd.DataFrame(orders)

    df.to_parquet("orders.parquet")

    print("Orders generated")