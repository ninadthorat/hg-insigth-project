
import pandas as pd
import hashlib

def handle_missing_and_anonymize(df: pd.DataFrame) -> pd.DataFrame:
    df["TotalCharges"].fillna(0.0, inplace=True)
    df["TechSupport"].fillna("No", inplace=True)

    # Fill InternetService with the most common value
    most_common_internet_service = df["InternetService"].mode()[0]
    df["InternetService"].fillna(most_common_internet_service, inplace=True)

    # Anonymize CustomerID
    df["CustomerID"] = df["CustomerID"].apply(lambda x: hashlib.sha256(str(x).encode()).hexdigest())

    return df