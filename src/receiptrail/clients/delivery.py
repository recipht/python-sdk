from typing import Optional
from .base import BaseClient
from ..types.delivery import (
    DeliveriesSummaryResponse,
    DeliverySuccessRateResponse,
    DeliveryChartResponse,
)


class DeliveryClient(BaseClient):
    """Client for Receiptrail Delivery API"""

    def get_deliveries_summary(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> DeliveriesSummaryResponse:
        """Get deliveries summary"""
        params = {}
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        return self.request("GET", "/delivery/analytics/deliveries/summary", params=params)

    def get_delivery_success_rate(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> DeliverySuccessRateResponse:
        """Get delivery success rate"""
        params = {}
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        return self.request("GET", "/delivery/analytics/deliveries/success-rate", params=params)

    def get_deliveries_chart(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> DeliveryChartResponse:
        """Get deliveries chart data"""
        params = {}
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        return self.request("GET", "/delivery/analytics/deliveries/chart", params=params)
