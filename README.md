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

