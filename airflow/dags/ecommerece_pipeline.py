from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from ingestion.ingest_products import fetch_products
from ingestion.ingest_orders import generate_orders
from transformations.transform_orders import transform_orders
from data_quality.validate_orders import validate_orders
# this is to add a line
with DAG(
    dag_id="ecommerce_pipeline",
    start_date=datetime(2024,1,1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    ingest_products = PythonOperator(
        task_id="fetch_products",
        python_callable=fetch_products
    )

    ingest_orders = PythonOperator(
        task_id="generate_orders",
        python_callable=generate_orders
    )

    transform = PythonOperator(
        task_id="transform_orders",
        python_callable=transform_orders
    )

    validate = PythonOperator(
        task_id="validate_orders",
        python_callable=validate_orders
    )

    ingest_products >> ingest_orders >> transform >> validate