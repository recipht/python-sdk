from typing import TypedDict, List


class DeliveryChartDataPoint(TypedDict):
    """Delivery chart data point"""
    date: str
    successful: int
    failed: int
    total: int


class DeliveriesSummaryResponse(TypedDict):
    """Deliveries summary response"""
    total_deliveries: int
    successful_deliveries: int
    failed_deliveries: int
    pending_deliveries: int
    period: str


class DeliverySuccessRateResponse(TypedDict):
    """Delivery success rate response"""
    success_rate: float
    total_attempts: int
    successful: int
    failed: int
    period: str


class DeliveryChartResponse(TypedDict):
    """Delivery chart data response"""
    data: List[DeliveryChartDataPoint]
    period: str
