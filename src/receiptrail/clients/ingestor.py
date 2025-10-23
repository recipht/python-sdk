from .base import BaseClient
from ..types.ingestor import (
    IngestReceiptRequest,
    IngestReceiptResponse,
)


class IngestorClient(BaseClient):
    """Client for Receiptrail Ingestor API"""

    def ingest_receipt(
        self,
        request: IngestReceiptRequest,
        idempotency_key: str
    ) -> IngestReceiptResponse:
        """Ingest receipts"""
        return self.request(
            "POST",
            "/v1/ingestor/receipts/ingest",
            data=request,
            headers={"Idempotency-Key": idempotency_key},
        )
