import json, hmac, hashlib, time, requests, base64
from requests.auth import AuthBase

class CoinbaseAuth(AuthBase):
    SIGNATURE_HTTP_HEADER = 'CB-ACCESS-SIGN'
    TIMESTAMP_HTTP_HEADER = 'CB-ACCESS-TIMESTAMP'
    KEY_HTTP_HEADER = 'CB-ACCESS-KEY'
    PASSPHRASE_HTTP_HEADER = 'CB-ACCESS-PASSPHRASE'

    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase

    def __call__(self, request):
        #Add headers        
        request.headers[CoinbaseAuth.KEY_HTTP_HEADER] = self.api_key
        request.headers[CoinbaseAuth.PASSPHRASE_HTTP_HEADER] = self.passphrase
        timestamp = str(time.time())        
        request.headers[CoinbaseAuth.TIMESTAMP_HTTP_HEADER] = timestamp
        
        #add signature
        method = request.method
        path = request.path_url
        content = request.body
        message = timestamp + method + path        
        if content:
            message += content 
        print message
        hmac_key = base64.b64decode(self.secret_key)
        sig = hmac.new(hmac_key, message, hashlib.sha256)
        sig_b64 = sig.digest().encode("base64").rstrip("\n")
        
        #Add signature header
        request.headers[CoinbaseAuth.SIGNATURE_HTTP_HEADER] = sig_b64
        return request
