# Azure Modern Data Platform
![Alt text for the image](https://github.com/upandya999/azure-modern-data-platform/blob/main/project_images/azure_pipeline_official_logos.svg)

# Architecture Explanation
### Python
Python is used for ingestion scripts and data processing logic because it provides strong ecosystem support for APIs, data manipulation, and cloud integrations.

### Azure Data Lake
Azure Data Lake acts as the central storage layer for raw and processed data. It allows scalable storage for structured and semi-structured datasets while keeping the raw data preserved for future reprocessing.

### Airflow
Airflow orchestrates the entire pipeline using DAGs (Directed Acyclic Graphs). It manages task scheduling, dependencies, retries, and monitoring of pipeline execution.

### dbt
dbt is used for transformation and data modeling. It enables modular SQL transformations and supports testing, documentation, and version control of analytics models.

### Data Quality Checks
Data validation ensures that incorrect or incomplete records do not propagate into analytics systems.
This project builds an end-to-end modern data pipeline using Azure and Airflow.

Tech Stack
- Azure Data Lake
- Airflow
- Python
- dbt
- Great Expectations
- Synapse

Architecture

API → Airflow → ADLS → Transformations → dbt → Synapse → Power BI

# How to run it locally

# 1. Clone the repository
git clone https://github.com/your-username/azure-modern-data-platform.git
cd azure-modern-data-platform

# 2. Create a Python virtual environment
python -m venv venv

# 3. Activate the virtual environment
# Mac / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate

# 4. Install project dependencies
pip install -r requirements.txt

# 5. Run data ingestion scripts
python ingestion/ingest_products.py
python ingestion/ingest_orders.py

# 6. Run transformation step
python transformations/transform_orders.py

# 7. Run data quality checks
python data_quality/validate_orders.py

# 8. Initialize Airflow database
airflow db init

# 9. Create Airflow admin user
airflow users create \
  --username admin \
  --firstname admin \
  --lastname admin \
  --role Admin \
  --email admin@example.com \
  --password admin

# 10. Start Airflow scheduler
airflow scheduler

# 11. Start Airflow webserver
airflow webserver --port 8080

# 12. Open Airflow UI
# http://localhost:8080

# 13. Trigger the DAG
# ecommerce_pipeline