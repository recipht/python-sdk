import time
from typing import Optional
import requests
from ..types import LogtoTokenResponse


class LogtoAuthClient:
    """Client for Logto authentication using personal access tokens"""

    def __init__(
        self,
        personal_access_token: str,
        logto_endpoint: str = "https://dtoqr1.logto.app"
    ):
        self.personal_access_token = personal_access_token
        self.logto_endpoint = logto_endpoint
        self._cached_token: Optional[str] = None
        self._token_expiry: float = 0

    def get_access_token(self) -> str:
        """Get access token, using cache if available"""
        if self._cached_token and time.time() < self._token_expiry:
            return self._cached_token

        # Exchange personal access token for API access token
        response = requests.post(
            f"{self.logto_endpoint}/oidc/token",
            data={
                "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
                "subject_token": self.personal_access_token,
                "subject_token_type": "urn:ietf:params:oauth:token-type:access_token",
                "resource": "https://api.receiptrail.ai",
            },
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
            },
        )
        response.raise_for_status()

        token_data: LogtoTokenResponse = response.json()
        self._cached_token = token_data["access_token"]
        self._token_expiry = time.time() + token_data["expires_in"] - 60

        return self._cached_token
