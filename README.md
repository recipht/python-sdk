# Receiptrail SDK for Python

Official Python SDK for the Receiptrail API.

## Installation

```bash
pip install receiptrail-sdk
```

## Usage

```python
from receiptrail import ReceiptrailClient

# Initialize the client with your personal access token
client = ReceiptrailClient(access_token="your-logto-personal-access-token")

# Ingest receipts
response = client.ingestor.ingest_receipt({
    "merchant_code": "MERCHANT_123",
    "location_id": "LOCATION_456",
    "receipts": [
        {
            "transaction_id": "TXN_001",
            "amount": 100.50,
            "currency": "USD",
        }
    ],
})

# Get receipt analytics
receipt_value = client.ingestor.get_receipt_value(
    start_date="2025-01-01",
    end_date="2025-01-31"
)

# Process receipt image
normalized = client.normalizer.process_image({
    "image_url": "https://example.com/receipt.jpg",
    "merchant_code": "MERCHANT_123",
})

# Get delivery analytics
delivery_summary = client.delivery.get_deliveries_summary(
    start_date="2025-01-01",
    end_date="2025-01-31"
)
```

## API Clients

### Ingestor Client

- `ingest_receipt(request, idempotency_key=None)` - Ingest receipts
- `get_receipt_value(start_date=None, end_date=None)` - Get receipt value analytics
- `get_receipt_count(start_date=None, end_date=None)` - Get receipt count
- `get_receipt_chart(start_date=None, end_date=None)` - Get receipt chart data
- `get_ingestion_success_rate(start_date=None, end_date=None)` - Get ingestion success rate

### Normalizer Client

- `process_image(request)` - Process receipt image
- `process_json(request)` - Process JSON receipt
- `process_bulk_json(request)` - Process multiple JSON receipts
- `list_receipts(skip=None, limit=None)` - List receipts
- `get_receipt(receipt_id)` - Get receipt by ID

### Delivery Client

- `get_deliveries_summary(start_date=None, end_date=None)` - Get deliveries summary
- `get_delivery_success_rate(start_date=None, end_date=None)` - Get delivery success rate
- `get_deliveries_chart(start_date=None, end_date=None)` - Get delivery chart data

## Configuration

```python
client = ReceiptrailClient(
    access_token="your-token",        # Required
    logto_endpoint="https://...",      # Optional, defaults to production
    base_url="https://...",            # Optional, defaults to production API
    timeout=30,                        # Optional, defaults to 30 seconds
)
```

## Requirements

- Python >= 3.8
- requests >= 2.31.0

## License

MIT
