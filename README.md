# requests-CoinbaseExchangeAuth
An authentication handler for using Coinbase Exchange API with Python Requests.

Requests is an HTTP library, written in Python, for human beings. This library
adds optional Coinbase Exchange API authentication support. Basic usage:


```python
    >>> import requests
    >>> from CoinbaseExchangeAuth import CoinbaseAuth
    >>> api_url = 'https://api.exchange.coinbase.com:443/'
    >>> auth = CoinbaseAuth(API_KEY, API_SECRET, API_PASS)
    >>> #GETs work, shows account balances
    >>> r = requests.get(api_url + 'accounts', auth=auth)
    >>> print r.json()
    {accounts: ...}
    >>> order = {}        
    >>> order['size'] = 0.01
    >>> order['price'] = 100
    >>> order['side'] = 'buy'
    >>> order['product_id'] = 'BTC-USD'
    >>> data = "{product_id:'BTC-USD'}"
    >>> r = requests.post(api_url + 'orders', json=order, auth=auth)
    >>> print r.json()
    {u'id': u'37cf0a2e-7ea9-4b90-...'}
```
