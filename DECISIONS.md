# Architectural Decisions

This document explains the key design decisions behind the architecture of this data pipeline. The goal is to demonstrate the reasoning behind tool selection and architectural trade-offs.

---

## 1. Why Airflow for Orchestration

Apache Airflow was chosen because it provides a flexible workflow orchestration framework that supports task dependencies, retries, scheduling, and monitoring through DAGs. It is widely used in production data platforms and allows pipelines to be managed as code.

Alternative considered:
- Cron jobs
- Prefect
- Azure Data Factory

Reason for rejection:
Cron lacks observability and dependency management, while Airflow provides mature scheduling and monitoring capabilities suitable for complex pipelines.

---

## 2. Why Python for Data Ingestion

Python was selected for ingestion scripts due to its strong ecosystem for API integrations, data manipulation, and cloud SDKs.

Advantages:
- Simple API integrations
- Rich libraries such as pandas and requests
- Native support for cloud SDKs

Python also allows ingestion logic to remain flexible when integrating multiple external systems.

---

## 3. Why Azure Data Lake as Storage

Azure Data Lake was selected as the central storage layer because it supports scalable and cost-efficient storage for structured and semi-structured data.

Benefits:
- Highly scalable storage
- Supports raw, processed, and curated zones
- Integrates well with analytics and processing engines

The storage structure follows a Medallion Architecture pattern.

---

## 4. Why Parquet Format

Parquet was chosen for storing datasets due to its columnar storage format optimized for analytics workloads.

Advantages:
- Efficient compression
- Faster analytical queries
- Reduced storage costs

Parquet is widely adopted in modern data lake architectures.

---

## 5. Why dbt for Transformations

dbt was selected for the transformation layer because it enables modular SQL transformations with version control.

Key benefits:
- SQL-based modeling
- Built-in testing
- Documentation generation
- Dependency management between models

This allows transformation logic to be managed in a scalable and maintainable way.

---

## 6. Why Great Expectations for Data Quality

Great Expectations was chosen for data validation because it provides declarative data quality checks and easy integration with data pipelines.

Capabilities:
- Schema validation
- Column-level checks
- Automated data quality reports

Data quality checks prevent corrupted or invalid records from propagating to analytics systems.

---

## 7. Why Separate Ingestion and Transformation Layers

The pipeline separates ingestion and transformation logic to improve maintainability and scalability.

Benefits:
- Raw data remains unchanged
- Transformations can evolve independently
- Data lineage becomes easier to track

This design follows common modern data platform practices.

---

## 8. Why Orchestrate Everything Through Airflow

Instead of manually running scripts, all tasks are executed through Airflow DAGs.

Advantages:
- Task dependency management
- Automated scheduling
- Monitoring and logging
- Retry mechanisms

This ensures the pipeline behaves like a production system.

---

## 9. Why Containerization with Docker

Docker was used to standardize the runtime environment for the pipeline.

Benefits:
- Consistent environments across machines
- Simplified dependency management
- Easier deployment

Containerization also enables easier migration to cloud environments.

---

## 10. Why a Star Schema for Analytics

The final analytics layer follows a star schema design.

Benefits:
- Optimized for BI queries
- Simplifies joins for analysts
- Improves dashboard performance

Fact tables store measurable metrics while dimension tables provide descriptive attributes.

---

## Future Improvements

Potential architectural improvements include:

- Implementing incremental transformations
- Adding CI/CD pipelines for automated
