from typing import TypedDict, Optional, List, Dict, Any


class LineItem(TypedDict, total=False):
    """Receipt line item"""
    name: str
    quantity: Optional[float]
    unit_price: Optional[float]
    total_price: Optional[float]
    category: Optional[str]


class NormalizedReceipt(TypedDict, total=False):
    """Normalized receipt data"""
    receipt_id: str
    merchant_name: Optional[str]
    merchant_address: Optional[str]
    transaction_date: Optional[str]
    total_amount: Optional[float]
    currency: Optional[str]
    tax_amount: Optional[float]
    items: Optional[List[LineItem]]
    payment_method: Optional[str]
    metadata: Optional[Dict[str, Any]]


class ProcessImageRequest(TypedDict, total=False):
    """Request for processing receipt image"""
    image_url: Optional[str]
    image_base64: Optional[str]
    merchant_code: Optional[str]


class ProcessImageResponse(TypedDict):
    """Response from image processing"""
    receipt_id: str
    status: str
    normalized_data: NormalizedReceipt


class ProcessJsonRequest(TypedDict, total=False):
    """Request for processing JSON receipt"""
    receipt_data: Dict[str, Any]
    merchant_code: Optional[str]


class ProcessBulkJsonRequest(TypedDict, total=False):
    """Request for processing multiple JSON receipts"""
    receipts: List[Dict[str, Any]]
    merchant_code: Optional[str]
