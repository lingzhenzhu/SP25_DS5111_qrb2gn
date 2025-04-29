# Built-in imports
import sys
sys.path.append(".")

# Built-in imports
import os
import pandas as pd

# Project imports
from bin.gainers.base import GainerDownload
from bin.gainers.factory import GainerFactory
from bin.gainers.yahoo import GainerProcessYahoo
from bin.gainers.wsj import GainerProcessWSJ

"""
Tests for Gainer downloaders and processors.
"""

class MockDownloader(GainerDownload):
    """
    A mock downloader that simulates downloading without network activity.
    """

    def download(self):
        # Just create a dummy HTML file if needed
        print("Mock download completed.")


def test_factory_returns_correct_classes():
    factory = GainerFactory('yahoo')
    assert isinstance(factory.get_downloader(), GainerDownload)
    assert isinstance(factory.get_processor(), GainerProcessYahoo)

    factory = GainerFactory('wsj')
    assert isinstance(factory.get_downloader(), GainerDownload)
    assert isinstance(factory.get_processor(), GainerProcessWSJ)


def test_yahoo_normalization(tmp_path):
    """
    Test Yahoo normalization logic.
    """

    # Prepare fake HTML source
    sample_csv_path = tmp_path / "fake_yahoo.html"
    df = pd.DataFrame({
        'Symbol': ['AAPL', 'TSLA'],
        'Price (Intraday)': [150.0, 700.0],
        'Change': [1.5, -2.0],
        '% Change': ['+1%', '-0.28%']
    })
    df.to_html(sample_csv_path, index=False)

    # Run processing
    processor = GainerProcessYahoo()
    processor.input_file = str(sample_csv_path)
    processor.output_file = str(tmp_path / "output.csv")
    processor.normalize()

    result = pd.read_csv(processor.output_file)

    # Check the normalized structure
    assert list(result.columns) == ['symbol', 'price', 'price_change', 'price_percent_change']
    assert result.shape == (2, 4)


def test_wsj_normalization(tmp_path):
    """
    Test WSJ normalization logic.
    """

    # Prepare fake HTML source
    sample_csv_path = tmp_path / "fake_wsj.html"
    df = pd.DataFrame({
        'Name': ['Apple Inc (AAPL)', 'Tesla Inc (TSLA)'],
        'Last': [150.0, 700.0],
        'Chg': [1.5, -2.0],
        '% Chg': [1.0, -0.28]
    })
    df.to_html(sample_csv_path, index=False)

    # Run processing
    processor = GainerProcessWSJ()
    processor.input_file = str(sample_csv_path)
    processor.output_file = str(tmp_path / "output.csv")
    processor.normalize()

    result = pd.read_csv(processor.output_file)

    # Check the normalized structure
    assert list(result.columns) == ['symbol', 'price', 'price_change', 'price_percent_change']
    assert result.shape == (2, 4)
    assert result['symbol'].iloc[0] == 'AAPL'
    assert result['symbol'].iloc[1] == 'TSLA'

