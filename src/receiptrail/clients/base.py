from typing import Any, Dict, Optional
import requests
from ..auth import LogtoAuthClient


class BaseClient:
    """Base HTTP client with authentication"""

    def __init__(
        self,
        auth_client: LogtoAuthClient,
        base_url: str,
        timeout: int = 30
    ):
        self.auth_client = auth_client
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()

    def _get_headers(self, additional_headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        """Get request headers with authentication"""
        token = self.auth_client.get_access_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        if additional_headers:
            headers.update(additional_headers)
        return headers

    def request(
        self,
        method: str,
        url: str,
        data: Optional[Any] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """Make HTTP request with authentication"""
        full_url = f"{self.base_url}{url}"
        request_headers = self._get_headers(headers)

        response = self.session.request(
            method=method,
            url=full_url,
            json=data,
            params=params,
            headers=request_headers,
            timeout=self.timeout,
        )
        response.raise_for_status()
        return response.json()
