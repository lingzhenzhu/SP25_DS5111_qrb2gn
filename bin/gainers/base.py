# Built-in imports
from abc import ABC, abstractmethod

# No third-party imports
# No project imports

"""
Base classes for Gainer downloading and processing.
"""

class GainerDownload(ABC):
    """
    Abstract base class for downloading gainer data.
    """

    @abstractmethod
    def download(self):
        """
        Method to download raw data.
        """
        pass


class GainerProcess(ABC):
    """
    Abstract base class for processing gainer data.
    """

    @abstractmethod
    def normalize(self):
        """
        Method to normalize raw data into standardized format.
        """
        pass

    @abstractmethod
    def save_with_timestamp(self):
        """
        Method to save the processed data with a timestamped filename.
        """
        pass
# Built-in imports
from abc import ABC, abstractmethod

# No third-party imports
# No project imports

"""
Base classes for Gainer downloading and processing.
"""

class GainerDownload(ABC):
    """
    Abstract base class for downloading gainer data.
    """

    @abstractmethod
    def download(self):
        """
        Method to download raw data.
        """
        pass


class GainerProcess(ABC):
    """
    Abstract base class for processing gainer data.
    """

    @abstractmethod
    def normalize(self):
        """
        Method to normalize raw data into standardized format.
        """
        pass

    @abstractmethod
    def save_with_timestamp(self):
        """
        Method to save the processed data with a timestamped filename.
        """
        pass
