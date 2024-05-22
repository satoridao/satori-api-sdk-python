from satori.lib.utils import hmac_hashing


def account(self, symbol: str):
    time = self.get_time()
    payload = {
        "symbol": symbol,
        "method": self.ACTION_SUBSCRIBE,
        "event": "api_account",
        "apiKey": self.api_key,
        "signature": hmac_hashing(self.api_secret, str(time)),
        "timestamp": time
    }
    self.send(payload)


