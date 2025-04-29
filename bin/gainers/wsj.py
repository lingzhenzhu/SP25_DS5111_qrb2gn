# Built-in imports
import os
import re
from datetime import datetime

# Third-party imports
import pandas as pd

# Project imports
from bin.gainers.base import GainerDownload, GainerProcess

"""
WSJ specific downloader and processor classes.
"""

class GainerDownloadWSJ(GainerDownload):
    """
    Class to download WSJ gainers page.
    """

    def __init__(self):
        self.url = "https://www.wsj.com/market-data/stocks/us/movers"

    def download(self):
        print("Downloading WSJ gainers...")
        os.system(
            f"sudo google-chrome-stable --headless --disable-gpu --dump-dom "
            f"--no-sandbox {self.url} > wsjgainers.html"
        )
        print("WSJ gainers HTML downloaded.")


class GainerProcessWSJ(GainerProcess):
    """
    Class to normalize and save WSJ gainers data.
    """

    def __init__(self):
        self.input_file = "wsjgainers.html"
        self.output_file = f"wsjgainers_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    def normalize(self):
        print("Normalizing WSJ gainers...")
        tables = pd.read_html(self.input_file)
        df = tables[0][['Name', 'Last', 'Chg', '% Chg']]
        df.columns = ['name', 'price', 'price_change', 'price_percent_change']
        df['symbol'] = df['name'].apply(lambda x: re.findall(r'\((.*?)\)', x)[-1] if '(' in x else x).str.upper()
        df = df[['symbol', 'price', 'price_change', 'price_percent_change']]
        df.to_csv(self.output_file, index=False)
        self.df = df

    def save_with_timestamp(self):
        print(f"Saved WSJ gainers to {self.output_file}.")
