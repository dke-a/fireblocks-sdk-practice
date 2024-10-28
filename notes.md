# API - SDK Study Nodes

## About API Exceptions

Found that `.venv/lib/python3.11/site-packages/fireblocks/exceptions.py` contain information on how to access attributes of exception `e`:

```python
    def __init__(
        self,
        status=None,
        reason=None,
        http_resp=None,
        *,
        body: Optional[str] = None,
        data: Optional[Any] = None,
    ) -> None:
        self.status = status
        self.reason = reason
        self.body = body
        self.data = data
        self.headers = None
```


## Get Vault Accounts

Exception when calling TransactionsApi->create_transaction: **(400)
Reason: Bad Request**
HTTP response headers: 
```json
Status Code: 200

Headers:
{
    'Date': 'Mon, 28 Oct 2024 17:00:14 GMT',
    'Content-Type': 'application/json; charset=utf-8',
    'Content-Length': '730',
    'Connection': 'keep-alive',
    'X-Powered-By': 'Express',
    'X-Request-ID': 'ec78326c4fb64805f2aacd1b8b703d25',
    'ETag': 'W/"2da-BHnMoTS7QREi48Ud3/3JS6c4Lvw"',
    'Strict-Transport-Security': 'max-age=15724800; includeSubDomains',
    'CF-Cache-Status': 'DYNAMIC',
    'Server': 'cloudflare',
    'CF-RAY': '8d9c7b1e19ca42ec-EWR'
}

Data:
{
  "accounts": [
    {
      "id": "3",
      "name": "First SDK Vault",
      "assets": [],
      "hiddenOnUI": false,
      "autoFuel": false
    },
    {
      "id": "2",
      "name": "First SDK Vault",
      "assets": [],
      "hiddenOnUI": false,
      "autoFuel": false
    },
    {
      "id": "1",
      "name": "test-vault",
      "assets": [
        {
          "id": "ETH_TEST5",
          "total": "0",
          "balance": "0",
          "available": "0",
          "pending": "0",
          "frozen": "0",
          "lockedAmount": "0",
          "staked": "0"
        }
      ],
      "hiddenOnUI": false,
      "autoFuel": false
    },
    {
      "id": "0",
      "name": "Default",
      "assets": [
        {
          "id": "BTC_TEST",
          "total": "0",
          "balance": "0",
          "available": "0",
          "pending": "0",
          "frozen": "0",
          "lockedAmount": "0",
          "staked": "0",
          "blockHeight": "3191575"
        },
        {
          "id": "ETH_TEST5",
          "total": "0",
          "balance": "0",
          "available": "0",
          "pending": "0",
          "frozen": "0",
          "lockedAmount": "0",
          "staked": "0"
        }
      ],
      "hiddenOnUI": false,
      "autoFuel": false
    }
  ],
  "paging": {}
}

Raw Data (if JSON):
{
  "accounts": [
    {
      "id": "3",
      "name": "First SDK Vault",
      "hiddenOnUI": false,
      "autoFuel": false,
      "assets": []
    },
    {
      "id": "2",
      "name": "First SDK Vault",
      "hiddenOnUI": false,
      "autoFuel": false,
      "assets": []
    },
    {
      "id": "1",
      "name": "test-vault",
      "hiddenOnUI": false,
      "autoFuel": false,
      "assets": [
        {
          "id": "ETH_TEST5",
          "total": "0",
          "balance": "0",
          "lockedAmount": "0",
          "available": "0",
          "pending": "0",
          "frozen": "0",
          "staked": "0"
        }
      ]
    },
    {
      "id": "0",
      "name": "Default",
      "hiddenOnUI": false,
      "autoFuel": false,
      "assets": [
        {
          "id": "BTC_TEST",
          "total": "0",
          "balance": "0",
          "lockedAmount": "0",
          "available": "0",
          "pending": "0",
          "frozen": "0",
          "staked": "0",
          "blockHeight": "3191575"
        },
        {
          "id": "ETH_TEST5",
          "total": "0",
          "balance": "0",
          "lockedAmount": "0",
          "available": "0",
          "pending": "0",
          "frozen": "0",
          "staked": "0"
        }
      ]
    }
  ],
  "paging": {}
}
```

## Create Transaction

## Get API Users

api_client.py:325: UserWarning: Failed to deserialize response of type ErrorResponse: 1 validation error for ErrorResponse
error
  Input should be a valid dictionary or instance of ErrorResponseError [type=model_type, input_value=None, input_type=NoneType]
    For further information visit https://errors.pydantic.dev/2.9/v/model_type
  warnings.warn(
**Exception when calling ApiUserApi->get_api_users: (403)
Reason: Forbidden**

```json
HTTP response headers: HTTPHeaderDict({'Date': 'Mon, 28 Oct 2024 16:07:26 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '43', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'X-Request-ID': '4b6be234654dfc0bba4a451540640b49', 'ETag': 'W/"2b-1qlRPxyZHAbCKTkurgtuyEuBMLk"', 'Strict-Transport-Security': 'max-age=15724800; includeSubDomains', 'CF-Cache-Status': 'DYNAMIC', 'Server': 'cloudflare', 'CF-RAY': '8d9c2dc25f6e7d0c-EWR'})
HTTP response body: message='Lacking permissions' code=-1
```