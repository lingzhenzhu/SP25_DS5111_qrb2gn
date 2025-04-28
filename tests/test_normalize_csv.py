import sys
sys.path.append('.')

import os
import pandas as pd
import pytest
from bin.normalize_csv import normalize_csv

@pytest.fixture
def sample_csv_file():
    """Fixture to create a temporary sample csv file for testing."""
    input_file = "test_sample.csv"
    output_file = "test_sample_norm.csv"

    df = pd.DataFrame({
        "Symbol": ["AAPL", "TSLA"],
        "Price": ["175.25", "230.10"],
        "Change": ["2.30", "-3.25"],
        "Change %": ["1.33%", "-1.39%"]
    })
    df.to_csv(input_file, index=False)

    yield input_file, output_file

    # Clean up after test
    if os.path.exists(input_file):
        os.remove(input_file)
    if os.path.exists(output_file):
        os.remove(output_file)

def test_normalize_csv(sample_csv_file):
    """Test that normalize_csv correctly transforms a raw csv into a standardized format."""
    input_file, output_file = sample_csv_file

    # Run the normalize function
    normalize_csv(input_file)

    # Check output file is created
    assert os.path.exists(output_file), "Normalized csv file was not created."

    # Load output file and verify structure
    df_norm = pd.read_csv(output_file)

    expected_columns = ["symbol", "price", "price_change", "price_percent_change"]

    # Check if the normalized csv has the expected columns
    assert list(df_norm.columns) == expected_columns, f"Expected columns {expected_columns} but got {list(df_norm.columns)}."

    # Check if data types are correct
    assert df_norm["symbol"].dtype == object, "Symbol column should be of type object (string)."
    assert pd.api.types.is_float_dtype(df_norm["price"]), "Price column should be of type float."
    assert pd.api.types.is_float_dtype(df_norm["price_change"]), "Price change column should be of type float."
    assert pd.api.types.is_float_dtype(df_norm["price_percent_change"]), "Price percent change column should be of type float."

    # Check row count matches
    assert df_norm.shape[0] == 2, f"Expected 2 rows but got {df_norm.shape[0]}."

