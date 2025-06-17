# etl/load.py
import pandas as pd
from sqlalchemy import create_engine

def load_to_postgres(df: pd.DataFrame, table_name: str, if_exists: str = "replace"):
    engine = create_engine("postgresql+psycopg2://user:password@postgres:5432/staging_db")
    df.to_sql(table_name, engine, if_exists=if_exists, index=False)
