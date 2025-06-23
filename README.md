# 📊 Customer Churn ETL Pipeline (Dockerized)

This project demonstrates a modular ELT pipeline using **Apache Airflow**, **PostgreSQL**, **Pandas**, and **Metabase**, containerized using **Docker Compose**. It performs hourly ingestion of customer churn data, processes it for missing values and PII, and exposes it for reporting.

---

## 📁 Project Structure

```
├── airflow/
│   ├── dags/                  # Airflow DAG definition
│   │   └── churn_etl_dag.py
│   ├── jars/                  # PostgreSQL JDBC JARs
│   ├── Dockerfile             # Custom Airflow image with Python packages
│   └── requirements.txt       # Python dependencies
├── data/                      # Raw data files
│   └── customer_churn_data.csv
├── etl/                       # Python ETL layer (modular)
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── __init__.py
├── Dashboard/                # Metabase screenshots (for demo)
│   └── img.png
├── docker-compose.yml        # All service definitions
└── README.md                 # This file
```

---

## 💠 Tech Stack

- **Airflow** (2.9.1, Python 3.10)
- **PostgreSQL** (15)
- **Pandas** for data transformation
- **Metabase** (reporting)
- **Docker Compose**

---

## 🚀 Setup Instructions

### ✅ Prerequisites

- Docker Desktop installed
- Internet connection to pull images

---

### 🧱 Build & Start the Containers

```bash
git clone <your-repo-url>
cd hg-insigth-project

# Start everything
docker-compose up --build -d
```

### 🐘 PostgreSQL

- Host: `localhost`
- Port: `5433`
- User: `user`
- Password: `password`
- DB: `staging_db`

### 🌐 Airflow

- Open: [http://localhost:8080](http://localhost:8080)

  ```
- Username: `airflow`
- Password: `hginsigth123`
- Trigger DAG: `churn_etl_dag`

### 📊 Metabase

- Open: [http://localhost:3000](http://localhost:3000)
- Connect to DB:
  - Host: `pg-staging`
  - Port: `5432`
  - User: `user`, Password: `password`
  - DB name: `staging_db`
- Explore the processed data: `processed_customer_data` table

---

## 🔄 DAG Flow Overview

1. **Extract**: Load CSV from `/data/customer_churn_data.csv`
2. **Load raw**: Store into `raw_customer_data` table
3. **Transform**:
   - Fill missing `TotalCharges`, `TechSupport`
   - Fill missing `InternetService` with most common value
   - Anonymize `CustomerID` with SHA-256
4. **Load processed**: Save cleaned data to `processed_customer_data`

Runs **hourly** via Airflow's `@hourly` schedule.

---

## 📸 Dashboard



- Go to `Out analytics' from collections
- Selct `Customer Churn` dashboard
The Metabase dashboard shows:

- Churn rate
- Breakdown by contract type and internet service



---

## 🩱 Cleanup

```bash
docker-compose down -v
```

---

## 📌 Notes

- All data and processing runs inside Docker containers.
- Metabase dashboards are **not persisted** — use screenshots or rebuild manually.
- Airflow password is regenerated every container restart. Fetch from logs as shown above.

---

## ✅ Author

Built by Ninad Thorat as part of HG Insight assessment.

