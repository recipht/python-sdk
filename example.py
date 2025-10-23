"""Example usage of Receiptrail SDK"""

import os
from receiptrail import ReceiptrailClient


def main():
    # Initialize the SDK with your personal access token from Logto
    client = ReceiptrailClient(
        access_token=os.environ.get("RECEIPTRAIL_ACCESS_TOKEN", "your-token-here")
    )

    try:
        # Example 1: Ingest receipts
        print("Ingesting receipts...")
        ingest_response = client.ingestor.ingest_receipt({
            "merchant_code": "MERCHANT_123",
            "location_id": "LOC_456",
            "receipts": [
                {
                    "transaction_id": "TXN_001",
                    "amount": 100.50,
                    "currency": "USD",
                    "items": [
                        {"name": "Item 1", "quantity": 2, "price": 50.25}
                    ],
                }
            ],
        })
        print(f"Ingest response: {ingest_response}")

        # Example 2: Get receipt analytics
        print("\nGetting receipt value...")
        receipt_value = client.ingestor.get_receipt_value(
            start_date="2025-01-01",
            end_date="2025-01-31"
        )
        print(f"Receipt value: {receipt_value}")

        # Example 3: Process receipt image
        print("\nProcessing receipt image...")
        normalized_receipt = client.normalizer.process_image({
            "image_url": "https://example.com/receipt.jpg",
            "merchant_code": "MERCHANT_123",
        })
        print(f"Normalized receipt: {normalized_receipt}")

        # Example 4: Get delivery summary
        print("\nGetting delivery summary...")
        delivery_summary = client.delivery.get_deliveries_summary(
            start_date="2025-01-01",
            end_date="2025-01-31"
        )
        print(f"Delivery summary: {delivery_summary}")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
