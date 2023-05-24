# Examples
Here are some examples which help you to get started with the library.

## Async Client:
```python title="async_client.py" linenums="1"
import asyncio
from plisio import AsyncClient

client = AsyncClient("<API_KEY>")
print(str(client))
```
```bash title="output" linenums="1"
<AsyncClient: https://plisio.net/api/v1>
```

```python title="get_transactions.py" linenums="1"
async def main():
    txs = await client.transactions()
    print(txs)


asyncio.run(main())
```
```json title="output" linenums="1"
{
  "status": "success",
  "data": {
    "operations": [
      {
        "user_id": 1,
        "shop_id": "607sdw35f4ee4a2b7t",
        "type": "invoice",
        "status": "completed",
        "tx_url": [
          "https://etherscan.io/tx/0x0000000000",
          "https://etherscan.io/tx/0x0000000000"
        ],
        "id": "1000000"
      },
      {
        "user_id": 1,
        "shop_id": null,
        "type": "cash_in",
        "status": "completed",
        "pending_sum": "0.00000000",
        "psys_cid": "BTC",
        "currency": "BTC",
        "source_currency": "USD",
        "source_rate": "0.00010216",
        "fee": null,
        "wallet_hash": "0x0000000000",
        "sendmany": null,
        "params": {
          "value": "0.00225754",
          "currency": "BTC"
        },
        "expire_at_utc": null,
        "created_at_utc": 1563529570,
        "amount": "0.00014243",
        "sum": 0.00014243,
        "commission": null,
        "tx_url": null,
        "tx_id": null,
        "id": "1000001",
        "actual_sum": 0.00014243,
        "actual_commission": null,
        "actual_fee": null,
        "actual_invoice_sum": null,
        "status_code": 3
      },
      {
        "user_id": 1,
        "shop_id": null,
        "type": "cash_out",
        "status": "completed",
        "pending_sum": "0.00000000",
        "psys_cid": "ETH-TESTNET",
        "currency": "TETH",
        "source_currency": "USD",
        "source_rate": "0.000216542551694120",
        "fee": "0.00952",
        "wallet_hash": "0x00000000001",
        "sendmany": null,
        "params": {
          "fee": {
            "gasLimit": "80000",
            "gasPrice": "119",
            "nonce": "",
            "dynamicField": "gasPrice",
            "plan": "normal",
            "unit": "Gwai",
            "value": "0.00952"
          },
          "source_currency": "USD",
          "source_rate": "0.000216542551694120"
        },
        "expire_at_utc": null,
        "created_at_utc": 1639734963,
        "amount": "0.017948510338824132",
        "sum": "0.027468510338824132",
        "commission": "0.000000000000000000",
        "tx_url": "https://ropsten.etherscan.io/tx/0x00000000001",
        "tx_id": [
          "0x00000000001"
        ],
        "id": "100000000000000000000002",
        "actual_sum": "0.017948510338824132",
        "actual_commission": null,
        "actual_fee": 0,
        "actual_invoice_sum": null,
        "status_code": 3,
        "tx": [
          {
            "url": "https://ropsten.etherscan.io/tx/0x00000000001",
            "wallet_hash": [
              "0x00000000001"
            ]
          }
        ]
      },
      .....
    ],
    "_links": {
      "self": {
        "href": "https://devdevda.com/api/v1/operations?api_key=...&page=1&per-page=10"
      },
      "first": {
        "href": "https://devdevda.com/api/v1/operations?api_key=...&page=1&per-page=10"
      },
      "last": {
        "href": "https://devdevda.com/api/v1/operations?api_key=...&page=157&per-page=10"
      },
      "next": {
        "href": "https://devdevda.com/api/v1/operations?api_key=...&page=2&per-page=10"
      }
    },
    "_meta": {
      "totalCount": 156,
      "pageCount": 15,
      "currentPage": 1,
      "perPage": 10
    }
  }
}
```
