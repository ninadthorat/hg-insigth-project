from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from sqlalchemy import create_engine
import pandas as pd
import os
import sys
# Make sure /opt/airflow is in the Python path so we can import etl/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from etl.extract import read_csv
from etl.transform import handle_missing_and_anonymize
from etl.load import load_to_postgres

default_args = {
    'start_date': datetime(2023, 1, 1),
}

with DAG('modular_elt_pipeline',
         schedule_interval="@hourly",
         catchup=False,
         default_args=default_args) as dag:

    def load_raw():
        df = read_csv('/opt/airflow/data/customer_churn_data.csv')
        load_to_postgres(df, 'raw_customer_data')


    def process_data():
        engine = create_engine("postgresql+psycopg2://user:password@postgres:5432/staging_db")
        df = pd.read_sql_table("raw_customer_data", con=engine)
        transformed_df = handle_missing_and_anonymize(df)
        load_to_postgres(transformed_df, 'processed_customer_data')


    t1 = PythonOperator(
        task_id='load_raw_data',
        python_callable=load_raw
    )

    t2 = PythonOperator(
        task_id='transform_and_load_processed_data',
        python_callable=process_data
    )

    t1 >> t2
