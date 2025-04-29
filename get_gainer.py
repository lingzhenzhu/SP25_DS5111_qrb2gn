# Built-in imports
import sys

# Project imports
from bin.gainers.factory import GainerFactory

"""
Main script to download, normalize, and save gainer data.
"""

class ProcessGainer:
    """
    Template class for running the gainer download and processing workflow.
    """

    def __init__(self, downloader, processor):
        self.downloader = downloader
        self.processor = processor

    def _download(self):
        self.downloader.download()

    def _normalize(self):
        self.processor.normalize()

    def _save(self):
        self.processor.save_with_timestamp()

    def process(self):
        """
        Execute the full workflow.
        """
        self._download()
        self._normalize()
        self._save()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Missing required argument 'choice'.")
        print("Usage: python get_gainer.py <choice>")
        sys.exit(1)
    choice = sys.argv[1]
    factory = GainerFactory(choice)
    downloader = factory.get_downloader()
    processor = factory.get_processor()

    runner = ProcessGainer(downloader, processor)
    runner.process()
