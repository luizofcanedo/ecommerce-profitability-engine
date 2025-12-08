import pandas as pd
import numpy as np
from datetime import datetime

# ==========================================
# CONFIGURATION
# ==========================================
INPUT_FILE = 'Ecommerce_Sales_Data_2024_2025.csv'
OUTPUT_FILE = 'Processed_Profitability_Audit.csv'  # NEUTRAL NAME

# ==========================================
# PHASE 1: INGESTION
# ==========================================
def ingest_data(filepath: str) -> pd.DataFrame:
    """
    Reads the raw sales data from CSV.
    Simulates fetching data from a Data Lake or SQL Dump.
    """
    try:
        print(f"[INFO] Ingesting data from {filepath}...")
        df = pd.read_csv(filepath)
        print(f"[SUCCESS] Ingested {len(df)} rows.")
        return df
    except FileNotFoundError:
        print(f"[ERROR] File {filepath} not found.")
        return pd.DataFrame()

# ==========================================
# PHASE 2: TRANSFORMATION (THE MAGIC)
# ==========================================
def process_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans raw sales data and applies 'Enterprise-Grade' business logic.
    
    Args:
        df (pd.DataFrame): The raw dataframe.
        
    Returns:
        pd.DataFrame: Enriched dataframe with Audit recommendations.
    """
    print("[INFO] Starting Data Transformation...")
    
    # 1. CLEANING: Strict Type Conversion
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    
    # 2. FEATURE ENGINEERING: Profit Margin
    # Calculate the actual margin percentage: (Profit / Sales) * 100
    df['Margin_Percent'] = np.where(
        df['Sales'] > 0, 
        (df['Profit'] / df['Sales']) * 100, 
        0.0
    )
    
    # 3. BUSINESS LOGIC (The "Analyst Bot")
    # Matches the logic described in your README
    
    conditions = [
        (df['Profit'] < 0),                                           # 1. Bleeding Money
        (df['Margin_Percent'] < 10) & (df['Profit'] > 0),             # 2. Low Margin (Risk)
        (df['Margin_Percent'] >= 10) & (df['Margin_Percent'] < 25),   # 3. Healthy
        (df['Margin_Percent'] >= 25)                                  # 4. Star Performer
    ]
    
    choices = [
        'CRITICAL: NEGATIVE MARGIN',
        'WARNING: LOW MARGIN',
        'HEALTHY: STANDARD',
        'PERFORMER: HIGH MARGIN'
    ]
    
    # Column name matches your Dashboard Guide
    df['Performance_Tag'] = np.select(conditions, choices, default='HEALTHY: STANDARD')
    
    # 4. ANOMALY DETECTION (The "Audit" Layer)
    # Flags "Bad Discount Strategies" (High Discount + Negative Profit)
    # Threshold matched to README (Discount > 30)
    df['Audit_Alert'] = np.where(
        (df['Discount'] > 30) & (df['Profit'] < 0), 
        'FLAG: BAD DISCOUNT STRATEGY', 
        'PASSED'
    )

    print(f"[SUCCESS] Transformation Complete. Enriched with Performance Tags.")
    return df

# ==========================================
# PHASE 3: LOADING (THE OUTPUT)
# ==========================================
def load_data(df: pd.DataFrame, output_path: str):
    """
    Saves the enriched data for the Dashboard.
    """
    try:
        df.to_csv(output_path, index=False)
        print(f"[SUCCESS] Data saved to {output_path}")
        print("-" * 30)
        print("PREVIEW OF PROCESSED DATA:")
        print(df[['Category', 'Sales', 'Profit', 'Margin_Percent', 'Performance_Tag']].head())
    except Exception as e:
        print(f"[ERROR] Failed to save data: {e}")

# ==========================================
# EXECUTION PIPELINE
# ==========================================
if __name__ == "__main__":
    # 1. Ingest
    raw_df = ingest_data(INPUT_FILE)
    
    if not raw_df.empty:
        # 2. Transform
        clean_df = process_sales_data(raw_df)
        
        # 3. Load
        load_data(clean_df, OUTPUT_FILE)