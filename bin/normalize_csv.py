"""
Normalize Gainers CSV files from Yahoo Finance or WSJ Market Data
into a unified format: symbol, price, price_change, price_percent_change.
"""

import os
import argparse
import pandas as pd

def normalize_csv(input_file):
    """
    Normalize gainers csv from different sources (Yahoo, WSJ)
    into a standard format: symbol, price, price_change, price_percent_change.
    """
    assert os.path.exists(input_file), f"❌ File {input_file} does not exist."

    # Read the input csv
    df = pd.read_csv(input_file)
    print(f"✅ Loaded {input_file} with shape {df.shape}")

    # Try to detect source based on columns
    if {'Symbol', 'Price', 'Change', 'Change %'}.issubset(df.columns):
        # Yahoo format
        print("Detected source: Yahoo Finance")
        df = df[['Symbol', 'Price', 'Change', 'Change %']].copy()
        df.rename(columns={
            'Symbol': 'symbol',
            'Price': 'price',
            'Change': 'price_change',
            'Change %': 'price_percent_change'
        }, inplace=True)
        df['symbol'] = df['symbol'].astype(str).str.upper()
        df['price'] = df['price'].astype(str).str.replace(',', '').astype(float)
        df['price_change'] = df['price_change'].astype(str).str.replace(',', '').astype(float)
        df['price_percent_change'] = df['price_percent_change'].astype(str).str.strip('%').astype(float)

    elif {'Unnamed: 0', 'Last', 'Chg', '% Chg'}.issubset(df.columns):
        # WSJ format
        print("Detected source: WSJ Market Data")
        df = df[['Unnamed: 0', 'Last', 'Chg', '% Chg']].copy()
        df.rename(columns={
            'Unnamed: 0': 'symbol',
            'Last': 'price',
            'Chg': 'price_change',
            '% Chg': 'price_percent_change'
        }, inplace=True)
        # Extract code inside parentheses and uppercase
        df['symbol'] = df['symbol'].astype(str).str.extract(r'\((\w+)\)', expand=False).str.upper()
        df['price'] = df['price'].astype(str).str.replace(',', '').astype(float)
        df['price_change'] = df['price_change'].astype(str).str.replace(',', '').astype(float)
        df['price_percent_change'] = df['price_percent_change'].astype(str).str.strip('%').astype(float)

    else:
        raise ValueError(f"❌ Unsupported CSV format: columns found {list(df.columns)}")

    # Final sanity check
    expected_columns = ['symbol', 'price', 'price_change', 'price_percent_change']
    assert list(df.columns) == expected_columns, f"❌ Columns mismatch after normalization: {list(df.columns)}"

    # Save normalized file
    output_file = input_file.replace('.csv', '_norm.csv')
    df.to_csv(output_file, index=False)
    print(f"✅ Normalized CSV saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Normalize Gainers CSV files.")
    parser.add_argument("input_file", type=str, help="Path to raw gainers CSV file")
    args = parser.parse_args()

    normalize_csv(args.input_file)
