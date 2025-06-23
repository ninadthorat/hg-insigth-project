#!/bin/bash

# Wait for DB to be ready
sleep 10

# Initialize Airflow DB (only if not already initialized)
airflow db init

# Create user if not exists
airflow users create \
    --username airflow \
    --firstname Ninad \
    --lastname Thorat \
    --role Admin \
    --email airflow@example.com \
    --password hginsigth123

# Start Airflow in standalone mode
exec airflow standalone
