from typing import Optional
from .auth import LogtoAuthClient
from .clients.ingestor import IngestorClient
from .clients.normalizer import NormalizerClient


class ReceiptrailClient:
    """Main Receiptrail SDK client"""

    def __init__(
        self,
        access_token: str,
        logto_endpoint: str = "https://dtoqr1.logto.app",
        base_url: str = "https://api.receiptrail.ai",
        timeout: int = 30
    ):
        """
        Initialize Receiptrail SDK client

        Args:
            access_token: Personal access token from Logto
            logto_endpoint: Logto endpoint URL
            base_url: API base URL
            timeout: Request timeout in seconds
        """
        self._auth_client = LogtoAuthClient(access_token, logto_endpoint)

        self.ingestor = IngestorClient(self._auth_client, base_url, timeout)
        self.normalizer = NormalizerClient(self._auth_client, base_url, timeout)
