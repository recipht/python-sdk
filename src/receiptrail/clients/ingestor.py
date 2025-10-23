from typing import Optional
from .base import BaseClient
from ..types.ingestor import (
    IngestReceiptRequest,
    IngestReceiptResponse,
    ReceiptValueResponse,
    ReceiptCountResponse,
    ReceiptChartResponse,
    SuccessRateResponse,
)


class IngestorClient(BaseClient):
    """Client for Receiptrail Ingestor API"""

    def ingest_receipt(
        self,
        request: IngestReceiptRequest,
        idempotency_key: Optional[str] = None
    ) -> IngestReceiptResponse:
        """Ingest receipts"""
        headers = {"Idempotency-Key": idempotency_key} if idempotency_key else None
        return self.request(
            "POST",
            "/ingestor/receipts/ingest",
            data=request,
            headers=headers,
        )

    def get_receipt_value(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> ReceiptValueResponse:
        """Get receipt value analytics"""
        params = {}
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        return self.request("GET", "/ingestor/analytics/receipts/value", params=params)

    def get_receipt_count(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> ReceiptCountResponse:
        """Get receipt count analytics"""
        params = {}
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        return self.request("GET", "/ingestor/analytics/receipts/count", params=params)

    def get_receipt_chart(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> ReceiptChartResponse:
        """Get receipt chart data"""
        params = {}
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        return self.request("GET", "/ingestor/analytics/receipts/chart", params=params)

    def get_ingestion_success_rate(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> SuccessRateResponse:
        """Get ingestion success rate"""
        params = {}
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        return self.request("GET", "/ingestor/analytics/ingestion/success-rate", params=params)
