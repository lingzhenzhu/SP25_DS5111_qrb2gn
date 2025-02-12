import pandas as pd
import argparse
import os

def normalize_csv(input_file):
    """
    Normalize csv to be：
    symbol, price, price_change, price_percent_change
    """
    assert os.path.exists(input_file), f"No {input_file}"

    # Read CSV
    df = pd.read_csv(input_file)

    # make sure file are correct
    required_columns = {'symbol', 'price', 'price_change', 'price_percent_change'}
    assert required_columns.issubset(set(df.columns)), f"Missing column: {df.columns}"

    # New file
    output_file = input_file.replace('.csv', '_norm.csv')

    # keep things needed
    df = df[['symbol', 'price', 'price_change', 'price_percent_change']]

    # make sure file are correct
    assert df['price'].dtype in [float, int], "price format wrong"
    assert df['price_change'].dtype in [float, int], "price change format wrong"

    # save new CSV
    df.to_csv(output_file, index=False)
    print(f"Completed: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CSV norm")
    parser.add_argument("input_file", type=str, help="input csv file")
    args = parser.parse_args()

    normalize_csv(args.input_file)
