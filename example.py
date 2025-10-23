"""Example usage of Receiptrail SDK"""

import os
import time
from receiptrail import ReceiptrailClient


def main():
    # Initialize the SDK with your personal access token from Logto
    client = ReceiptrailClient(
        access_token=os.environ.get("RECEIPTRAIL_ACCESS_TOKEN", "your-token-here")
    )

    try:
        # Example 1: Ingest receipts
        print("Ingesting receipts...")
        ingest_response = client.ingest_receipt(
            {
                "merchant_code": "SQUARE_US",
                "location_id": "LOC_123",
                "source_type": "api",
                "format_type": "json",
                "receipts": [
                    {
                        "transaction_id": "fea72209-00d8-4b67-8591-d809ca054a73",
                        "payload": {
                            "merchant_name": "SMOKEY FLAVOR BBQ & BURGER",
                            "total_amount": 31.00,
                            "currency": "USD",
                            "transaction_date": "2024-12-01T14:03:00Z",
                            "payment_method": {
                                "type": "AMEX",
                                "bin": "374245",
                                "last_four": "1002",
                                "account_number_masked": "**** **** **** 1002",
                                "approval_code": "802797",
                                "reference_number": "PRJwvm82mVynITIsIPhe5FBDuaB",
                                "transaction_id": "fea72209-00d8-4b67-8591-d809ca054a73",
                                "validation_code": "1002",
                                "terminal_id": "SQ_TERMINAL_001"
                            },
                            "auth_code": "802797",
                            "aid": "A000000025010901",
                            "store_info": {
                                "store_number": "SQ_001",
                                "operator_number": "OP_12345",
                                "terminal_number": "17",
                                "transaction_number": "14322",
                                "manager": "Mgr JOHN SMITH",
                                "phone": "(214) 434-0204",
                                "address": {
                                    "street": "123 Main Street",
                                    "city": "Dallas",
                                    "state": "TX",
                                    "zip": "75201"
                                },
                                "coordinates": {
                                    "lat": 32.84380194,
                                    "lng": -97.01091694
                                }
                            },
                            "receipt_url": "https://squareup.com/receipt/american-express-only/PRJwvm82mVynITIsIPhe5FBDuaB",
                            "line_items": [
                                {
                                    "product_code": "BBQ001",
                                    "name": "BBQ Brisket Sandwich",
                                    "quantity": 1,
                                    "unit_price": 12.99,
                                    "total_price": 12.99,
                                    "category": "Main Course",
                                    "tax_category": "TF",
                                    "regular_price": 12.99,
                                    "discount_applied": 0.00
                                }
                            ],
                            "taxes": [
                                {
                                    "type": "Sales Tax",
                                    "rate": 0.0825,
                                    "amount": 2.56
                                }
                            ]
                        },
                        "metadata": {
                            "source_system": "Square",
                            "version": "1.0",
                            "timestamp": "2024-12-01T14:03:00Z",
                            "location": "LOC_123",
                            "cashier": "CASH_001",
                            "register": "REG_001"
                        }
                    }
                ]
            },
            f"idempotency-{int(time.time() * 1000)}"  # Required idempotency key
        )
        print(f"Ingest response: {ingest_response}")

        # Example 2: Process receipt image
        print("\nProcessing receipt image...")
        normalized_receipt = client.process_image({
            "image_url": "https://example.com/receipt.jpg",
            "merchant_code": "MERCHANT_123",
        })
        print(f"Normalized receipt: {normalized_receipt}")

        # Example 3: Process JSON receipt
        print("\nProcessing JSON receipt...")
        json_receipt = client.process_json({
            "receipt_data": {
                "merchant_name": "Coffee Shop",
                "total_amount": 15.99,
                "currency": "USD",
                "transaction_date": "2025-01-15T10:30:00Z",
            },
            "merchant_code": "MERCHANT_123",
        })
        print(f"JSON receipt: {json_receipt}")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
