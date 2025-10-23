from typing import TypedDict, Optional, List, Any, Literal

SourceType = Literal["api", "sftp"]
FormatType = Literal["json", "xml", "csv", "html", "base64", "raw"]


class ReceiptrailConfig(TypedDict):
    """Configuration for Receiptrail SDK"""
    access_token: str
    logto_endpoint: Optional[str]
    base_url: Optional[str]
    timeout: Optional[int]


class LogtoTokenResponse(TypedDict):
    """Response from Logto token exchange"""
    access_token: str
    token_type: str
    expires_in: int
    scope: str
