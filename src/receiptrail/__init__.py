"""Receiptrail SDK for Python"""

from .client import ReceiptrailClient
from .types import ReceiptrailConfig
from .types.ingestor import (
    IngestReceiptRequest,
    IngestReceiptResponse,
)
from .types.normalizer import (
    ProcessImageRequest,
    ProcessImageResponse,
    ProcessJsonRequest,
    NormalizedReceipt,
    LineItem,
)

__version__ = "0.1.0"
__all__ = [
    "ReceiptrailClient",
    "ReceiptrailConfig",
    "IngestReceiptRequest",
    "IngestReceiptResponse",
    "ProcessImageRequest",
    "ProcessImageResponse",
    "ProcessJsonRequest",
    "NormalizedReceipt",
    "LineItem",
]
