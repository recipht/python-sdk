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
    ProcessBulkJsonRequest,
    NormalizedReceipt,
    LineItem,
)
from .types.delivery import (
    DeliveriesSummaryResponse,
    DeliverySuccessRateResponse,
    DeliveryChartResponse,
    DeliveryChartDataPoint,
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
    "ProcessBulkJsonRequest",
    "NormalizedReceipt",
    "LineItem",
    "DeliveriesSummaryResponse",
    "DeliverySuccessRateResponse",
    "DeliveryChartResponse",
    "DeliveryChartDataPoint",
]
