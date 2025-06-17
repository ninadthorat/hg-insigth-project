FROM apache/airflow:2.9.1-python3.10

USER root

# Install OS packages needed for psycopg2 and pandas
RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    apt-get clean

USER airflow

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
