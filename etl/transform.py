# etl/transform.py
import pandas as pd
import hashlib

def handle_missing_and_anonymize(df: pd.DataFrame) -> pd.DataFrame:
    df.fillna({
        "TotalCharges": 0.0,
        "TechSupport": "No"
    }, inplace=True)

    # Anonymize CustomerID using SHA256
    df["CustomerID"] = df["CustomerID"].apply(lambda x: hashlib.sha256(str(x).encode()).hexdigest())

    return df