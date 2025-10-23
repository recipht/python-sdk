from typing import TypedDict, Optional, List, Dict, Any
from . import SourceType, FormatType


class IngestReceiptRequest(TypedDict, total=False):
    """Request for ingesting receipts"""
    merchant_code: str
    location_id: Optional[str]
    source_type: Optional[SourceType]
    format_type: Optional[FormatType]
    receipts: List[Dict[str, Any]]


class IngestReceiptResponse(TypedDict):
    """Response from receipt ingestion"""
    ingestion_id: str
    status: str
    message: str
    receipts_count: int


class ReceiptValueResponse(TypedDict):
    """Receipt value analytics response"""
    total_value: float
    currency: str
    period: str


class ReceiptCountResponse(TypedDict):
    """Receipt count analytics response"""
    total_count: int
    period: str


class ChartDataPoint(TypedDict):
    """Chart data point"""
    date: str
    value: float


class ReceiptChartResponse(TypedDict):
    """Receipt chart data response"""
    data: List[ChartDataPoint]
    period: str


class SuccessRateResponse(TypedDict):
    """Success rate analytics response"""
    success_rate: float
    total_attempts: int
    successful: int
    failed: int
    period: str
