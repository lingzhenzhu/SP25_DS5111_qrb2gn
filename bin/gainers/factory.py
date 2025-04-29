# Project imports
from bin.gainers.yahoo import GainerDownloadYahoo, GainerProcessYahoo
from bin.gainers.wsj import GainerDownloadWSJ, GainerProcessWSJ

"""
Factory class to create downloader and processor instances.
"""

class GainerFactory:
    """
    Factory class to create Gainer downloader and processor.
    """

    def __init__(self, choice):
        assert choice in ['yahoo', 'wsj'], f"Unsupported gainer type: {choice}"
        self.choice = choice

    def get_downloader(self):
        if self.choice == 'yahoo':
            return GainerDownloadYahoo()
        return GainerDownloadWSJ()

    def get_processor(self):
        if self.choice == 'yahoo':
            return GainerProcessYahoo()
        return GainerProcessWSJ()
