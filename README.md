# Satori Public API Connector Python

[![PyPI version](https://img.shields.io/pypi/v/binance-connector)](https://pypi.python.org/pypi/binance-connector)
[![Python version](https://img.shields.io/pypi/pyversions/binance-connector)](https://www.python.org/downloads/)
[![Documentation](https://img.shields.io/badge/docs-latest-blue)](https://binance-connector.readthedocs.io/en/stable/)
[![Code Style](https://img.shields.io/badge/code_style-black-black)](https://black.readthedocs.io/en/stable/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a lightweight library that works as a connector to satori api.

- Supported APIs:
  - `/api/*`
- Customizable base URL, request timeout and HTTP proxy
- Response metadata can be displayed

## RESTful APIs

Usage examples:

```python
from satori.client import Client, Order, OrderList


client = Client()

# Get server timestamp
print(client.time())
# Get kline of ETH-USD at 1MIN interval
print(client.kline("ETH-USD", "1MIN"))
# Get last 10 klines of ETH-USD at 1MIN interval
print(client.klines("ETH-USD", "1MIN", limit=10))

# API key/secret are required for user data endpoints
client = Client(api_key='<api_key>', api_secret='<api_secret>')

# Get account and balance information
print(client.balance())

# Post a new order
order1 = Order(str(client.time()), True, True, 20, 2, "ETH-USD", 3, "0.02", "3100")
response =client.create_order(order1,client.time())
print(response)
```

- In order to set your API and Secret Key for use of the examples, create a file `examples/config.ini` with your keys.

- Eg:

  ```ini
  # config.ini
  [keys]
  base_url=
  ws_url=
  api_key=
  api_secret=
  ```

### Authentication

Satori supports HMAC authentication.

```python
# HMAC: pass API key and secret
client = Client(api_key, api_secret)
print(client.account())
```

### Base URL

If `base_url` is not provided, it defaults to `zk-test.satori.finance`.<br/>

### Optional parameters

PEP8 suggests _lowercase with words separated by underscores_, but for this connector,
the methods' optional parameters should follow their exact naming as in the API documentation.

```python
# Recognised parameter name
response = client.cancel_order(entrustId='ETH-USD', timestamp=client.time())

# Unrecognised parameter name
response = client.cancel_order(entrust_id='ETH-USD', timestamp=client.time())
```

### Timeout 

`timeout` is available to be assigned with the number of seconds you find most appropriate to wait for a server response.<br/>
Please remember the value as it won't be shown in error message _no bytes have been received on the underlying socket for timeout seconds_.<br/>
By default, `timeout` is None. Hence, requests do not time out.

```python
from satori.client import Client
client= Client(timeout=1)
```

### Proxy

Proxy is supported.

```python
from satori.client import Client
proxies = { 'https': 'http://1.2.3.4:8080' }

client= Client(proxies=proxies)
```

## Websocket

​	Usage examples:

```python
# WebSocket API Client
from binance.websocket.spot.websocket_api import SpotWebsocketAPIClient

def message_handler(_, message):
    logging.info(message)

my_client = SpotWebsocketAPIClient(on_message=message_handler)

my_client.ticker(symbol="BNBBUSD", type="FULL")

time.sleep(5)
logging.info("closing ws connection")
my_client.stop()
```

```python
# WebSocket Stream Client
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient

def message_handler(_, message):
    logging.info(message)

my_client = SpotWebsocketStreamClient(on_message=message_handler)

# Subscribe to a single symbol stream
my_client.agg_trade(symbol="bnbusdt")
time.sleep(5)
logging.info("closing ws connection")
my_client.stop()
```
