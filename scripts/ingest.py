"""
Phase 2 — Data Ingestion

Downloads source datasets from live sources and stores them in data/raw/.
The pull date and time are displayed in the execution log.
Raw source files are not modified during ingestion.
"""

import os
import requests
import pandas as pd
from io import StringIO
from datetime import datetime

RAW_DIR = "data/raw"
os.makedirs(RAW_DIR, exist_ok=True)

pull_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"\n========== DATA INGESTION ==========")
print(f"Pull date and time: {pull_datetime}")

def ingest_psa_dataset(url, output_filename):

    # Get metadata
    metadata_response = requests.get(url)
    metadata_response.raise_for_status()

    metadata = metadata_response.json()

    # Build query using all available values
    query = []

    for variable in metadata["variables"]:
        query.append({
            "code": variable["code"],
            "selection": {
                "filter": "item",
                "values": variable["values"]
            }
        })

    payload = {
        "query": query,
        "response": {
            "format": "csv"
        }
    }

    # Get data
    response = requests.post(url, json=payload)
    response.raise_for_status()

    # Convert to DataFrame
    df = pd.read_csv(StringIO(response.text))

    # Save raw data
    output_path = os.path.join(RAW_DIR, output_filename)

    df.to_csv(output_path, index=False)

    # Display information
    print(f"\n========== {metadata['title']} ==========")
    print(df)
    print(f"\nSaved as: {output_path}")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    return df


# INCOME DATASET

income_url = (
    "https://openstat.psa.gov.ph/"
    "PXWeb/api/v1/en/DB/1E/IE/0011E3ANIE0.px"
)

income_df = ingest_psa_dataset(
    income_url,
    "fies_income_raw.csv"
)



# ICT PERFORMANCE DATASET

ict_url = (
    "https://openstat.psa.gov.ph/"
    "PXWeb/api/v1/en/DB/2D/2022/0042D4BAJ00.px"
)

ict_df = ingest_psa_dataset(
    ict_url,
    "aspbi_ict_raw.csv"
)

# INTERNET USAGE DATASET

google_sheet_id = (
    "1_QViSG-HgK4pgXFBMmEG-gWokCkurjmfSaX_yt0jFv4"
)

excel_url = (
    f"https://docs.google.com/spreadsheets/d/"
    f"{google_sheet_id}/export?format=xlsx"
)

# Download Excel file
excel_response = requests.get(excel_url)
excel_response.raise_for_status()

# Save raw Excel file directly
excel_path = os.path.join(
    RAW_DIR,
    "internet_usage_raw.xlsx"
)

with open(excel_path, "wb") as file:
    file.write(excel_response.content)

print("\n========== INTERNET USAGE DATA ==========")
print(f"Saved as: {excel_path}")

# Read Excel into DataFrame
internet_usage_df = pd.read_excel(excel_path)

print(internet_usage_df)
print(f"\nRows: {len(internet_usage_df)}")
print(f"Columns: {len(internet_usage_df.columns)}")