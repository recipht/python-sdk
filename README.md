# Receiptrail Python SDK

Official Python SDK for the Receiptrail API - a digital receipt aggregation, normalization, and delivery platform.

## Features

- 🔐 **Authentication** - Secure authentication using Logto Personal Access Tokens (PAT)
- 📥 **Receipt Ingestion** - Ingest receipts from various sources with idempotency support
- 🔄 **Receipt Normalization** - Process and normalize receipt data from images or JSON
- 📦 **Type-Safe** - Full type hint support with detailed type definitions
- ⚡ **Token Caching** - Automatic access token caching and refresh

## Installation

```bash
pip install receiptrail
```

## Quick Start

### 1. Get Your Personal Access Token

Create a Personal Access Token (PAT) from your [Logto Console](https://docs.logto.io/user-management/personal-access-token).

### 2. Initialize the Client

```python
from receiptrail import ReceiptrailClient

client = ReceiptrailClient(
    access_token='your-logto-personal-access-token'
)
```

### 3. Ingest Receipts

```python
response = client.ingestor.ingest_receipt(
    {
        "merchant_code": "SQUARE_US",
        "location_id": "LOC_123",
        "source_type": "api",
        "format_type": "json",
        "receipts": [
            {
                "transaction_id": "txn_001",
                "payload": {
                    "merchant_name": "Coffee Shop",
                    "total_amount": 15.99,
                    "currency": "USD",
                    "transaction_date": "2025-01-15T10:30:00Z",
                    "line_items": [
                        {
                            "name": "Latte",
                            "quantity": 1,
                            "unit_price": 5.99,
                            "total_price": 5.99,
                        }
                    ],
                },
            }
        ],
    },
    "unique-idempotency-key-123"  # Required for duplicate prevention
)
```

### 4. Process and Normalize Receipts

```python
# Process receipt image
normalized = client.normalizer.process_image({
    "image_url": "https://example.com/receipt.jpg",
    "merchant_code": "MERCHANT_123",
})

# Process JSON receipt
json_receipt = client.normalizer.process_json({
    "receipt_data": {
        "merchant_name": "Coffee Shop",
        "total_amount": 15.99,
        "currency": "USD",
    },
    "merchant_code": "MERCHANT_123",
})
```

## API Reference

### Ingestor Client (`client.ingestor`)

Manage receipt ingestion.

#### Methods

- **`ingest_receipt(request, idempotency_key)`** - Ingest receipts with duplicate prevention
  - `request`: Receipt data including merchant_code, location_id, and receipts array
  - `idempotency_key` (required): Unique key to prevent duplicate ingestion

### Normalizer Client (`client.normalizer`)

Process and normalize receipt data from various formats.

#### Methods

- **`process_image(request)`** - Extract and normalize data from receipt images
  - `request`: { "image_url": str, "merchant_code": str }

- **`process_json(request)`** - Normalize structured JSON receipt data
  - `request`: { "receipt_data": dict, "merchant_code": str }

## Configuration Options

```python
from receiptrail import ReceiptrailClient

client = ReceiptrailClient(
    # Required: Your Logto Personal Access Token
    access_token='your-pat-token',

    # Optional: Custom Logto endpoint
    # Default: 'https://dtoqr1.logto.app'
    logto_endpoint='https://your-logto-instance.app',

    # Optional: Custom API base URL
    # Default: 'https://api.receiptrail.ai'
    base_url='https://api.receiptrail.ai',

    # Optional: Request timeout in seconds
    # Default: 30
    timeout=60,
)
```

## Best Practices

### Idempotency Keys

Always use unique idempotency keys for receipt ingestion to prevent duplicate processing:

```python
import time
import uuid

# Use transaction ID + timestamp
idempotency_key = f"{transaction_id}-{int(time.time() * 1000)}"

# Or use UUID
idempotency_key = str(uuid.uuid4())

client.ingestor.ingest_receipt(receipt_data, idempotency_key)
```

### Error Handling

```python
from requests.exceptions import HTTPError, RequestException

try:
    response = client.ingestor.ingest_receipt(data, idempotency_key)
    print('Success:', response)
except HTTPError as error:
    # API error response
    print('API Error:', error.response.status_code, error.response.json())
except RequestException as error:
    # Network error
    print('Network Error:', str(error))
except Exception as error:
    # Other errors
    print('Error:', str(error))
```

### Token Caching

The SDK automatically caches access tokens and refreshes them before expiry. You don't need to manage token refresh manually.

## Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run example
python example.py

# Run tests
pytest
```

## Support

- **Documentation**: [Receiptrail API Docs](https://api.receiptrail.ai)
- **Issues**: [GitHub Issues](https://github.com/receiptrail/python-sdk/issues)
- **Email**: support@receiptrail.ai

## License

MIT
