# Built-in imports
import os
from datetime import datetime

# Third-party imports
import pandas as pd

# Project imports
from bin.gainers.base import GainerDownload, GainerProcess

"""
Yahoo specific downloader and processor classes.
"""

class GainerDownloadYahoo(GainerDownload):
    """
    Class to download Yahoo gainers page.
    """

    def __init__(self):
        self.url = "https://finance.yahoo.com/markets/stocks/gainers/"

    def download(self):
        print("Downloading Yahoo gainers...")
        os.system(
            f"sudo google-chrome-stable --headless --disable-gpu --dump-dom "
            f"--no-sandbox {self.url} > ygainers.html"
        )
        print("Yahoo gainers HTML downloaded.")


class GainerProcessYahoo(GainerProcess):
    """
    Class to normalize and save Yahoo gainers data.
    """

    def __init__(self):
        self.input_file = "ygainers.html"
        self.output_file = f"ygainers_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    def normalize(self):
        print("Normalizing Yahoo gainers...")
        tables = pd.read_html(self.input_file)
        df = tables[0][['Symbol', 'Price (Intraday)', 'Change', '% Change']]
        df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
        df['price_percent_change'] = df['price_percent_change'].str.replace('%', '')
        df.to_csv(self.output_file, index=False)
        self.df = df

    def save_with_timestamp(self):
        print(f"Saved Yahoo gainers to {self.output_file}.")
