import pandas as pd
from sqlalchemy import create_engine
from hashlib import sha256

# Read CSV
df = pd.read_csv("/opt/airflow/data/customer_churn_data.csv")

# Fill missing values
df.fillna({
    "TotalCharges": 0,
    "TechSupport": "Unknown"
}, inplace=True)

# Anonymize PII
df['CustomerID'] = df['CustomerID'].astype(str).apply(lambda x: sha256(x.encode()).hexdigest())

# Load into PostgreSQL
engine = create_engine("postgresql+psycopg2://user:password@postgres:5432/staging_db")

df.to_sql("customers", engine, if_exists="replace", index=False)