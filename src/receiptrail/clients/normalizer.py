from typing import Optional, List
from .base import BaseClient
from ..types.normalizer import (
    ProcessImageRequest,
    ProcessImageResponse,
    ProcessJsonRequest,
    ProcessBulkJsonRequest,
    NormalizedReceipt,
)


class NormalizerClient(BaseClient):
    """Client for Receiptrail Normalizer API"""

    def process_image(self, request: ProcessImageRequest) -> ProcessImageResponse:
        """Process receipt image"""
        return self.request("POST", "/v1/normalizer/process/image", data=request)

    def process_json(self, request: ProcessJsonRequest) -> NormalizedReceipt:
        """Process JSON receipt"""
        return self.request("POST", "/v1/normalizer/process/json", data=request)

    def process_bulk_json(self, request: ProcessBulkJsonRequest) -> List[NormalizedReceipt]:
        """Process multiple JSON receipts"""
        return self.request("POST", "/v1/normalizer/process/bulk-json", data=request)

    def list_receipts(
        self,
        skip: Optional[int] = None,
        limit: Optional[int] = None
    ) -> List[NormalizedReceipt]:
        """List receipts"""
        params = {}
        if skip is not None:
            params["skip"] = skip
        if limit is not None:
            params["limit"] = limit
        return self.request("GET", "/v1/normalizer/receipts", params=params)

    def get_receipt(self, receipt_id: str) -> NormalizedReceipt:
        """Get receipt by ID"""
        return self.request("GET", f"/v1/normalizer/receipts/{receipt_id}")
