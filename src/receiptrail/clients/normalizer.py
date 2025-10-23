from .base import BaseClient
from ..types.normalizer import (
    ProcessImageRequest,
    ProcessImageResponse,
    ProcessJsonRequest,
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
