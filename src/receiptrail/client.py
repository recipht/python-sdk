from typing import Any, Dict, Optional
import requests
from .auth import LogtoAuthClient
from .types.ingestor import IngestReceiptRequest, IngestReceiptResponse
from .types.normalizer import (
    ProcessImageRequest,
    ProcessImageResponse,
    ProcessJsonRequest,
    NormalizedReceipt,
)


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
        self._base_url = base_url
        self._timeout = timeout
        self._session = requests.Session()

    def _get_headers(self, additional_headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        """Get request headers with authentication"""
        token = self._auth_client.get_access_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        if additional_headers:
            headers.update(additional_headers)
        return headers

    def _request(
        self,
        method: str,
        url: str,
        data: Optional[Any] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """Make HTTP request with authentication"""
        full_url = f"{self._base_url}{url}"
        request_headers = self._get_headers(headers)

        response = self._session.request(
            method=method,
            url=full_url,
            json=data,
            params=params,
            headers=request_headers,
            timeout=self._timeout,
        )
        response.raise_for_status()
        return response.json()

    def ingest_receipt(
        self,
        request: IngestReceiptRequest,
        idempotency_key: str
    ) -> IngestReceiptResponse:
        """Ingest receipts"""
        return self._request(
            "POST",
            "/v1/ingestor/receipts/ingest",
            data=request,
            headers={"Idempotency-Key": idempotency_key},
        )

    def process_image(self, request: ProcessImageRequest) -> ProcessImageResponse:
        """Process receipt image"""
        return self._request("POST", "/v1/normalizer/process/image", data=request)

    def process_json(self, request: ProcessJsonRequest) -> NormalizedReceipt:
        """Process JSON receipt"""
        return self._request("POST", "/v1/normalizer/process/json", data=request)
