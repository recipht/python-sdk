"""Receiptrail SDK for Python"""

from .client import ReceiptrailClient
from .types import ReceiptrailConfig
from .types.ingestor import (
    IngestReceiptRequest,
    IngestReceiptResponse,
    ReceiptValueResponse,
    ReceiptCountResponse,
    ReceiptChartResponse,
    SuccessRateResponse,
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
    "ReceiptValueResponse",
    "ReceiptCountResponse",
    "ReceiptChartResponse",
    "SuccessRateResponse",
    "ProcessImageRequest",
    "ProcessImageResponse",
    "ProcessJsonRequest",
    "NormalizedReceipt",
    "LineItem",
]
