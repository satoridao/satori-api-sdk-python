from satori.lib.utils import hmac_hashing


def order(self, pairName: str):
    time = self.get_time()
    payload = {
        "pair": pairName,
        "method": self.ACTION_SUBSCRIBE,
        "event": "api_entrust",
        "apiKey": self.api_key,
        "signature": hmac_hashing(self.api_secret, str(time)),
        "timestamp": time
    }
    self.send(payload)


def position(self, pairName: str):
    time = self.get_time()
    payload = {
        "pair": pairName,
        "method": self.ACTION_SUBSCRIBE,
        "event": "api_position",
        "apiKey": self.api_key,
        "signature": hmac_hashing(self.api_secret, str(time)),
        "timestamp": time
    }
    self.send(payload)


def kline(self, pairName: str, period: str):
    time = self.get_time()
    payload = {
        "pair": pairName,
        "period": period,
        "method": self.ACTION_SUBSCRIBE,
        "event": "api_kline",
        "apiKey": self.api_key,
        "signature": hmac_hashing(self.api_secret, str(time)),
        "timestamp": time
    }
    self.send(payload)


def order_book(self, pairName: str):
    time = self.get_time()
    payload = {
        "pair": pairName,
        "method": self.ACTION_SUBSCRIBE,
        "event": "api_depth",
        "apiKey": self.api_key,
        "signature": hmac_hashing(self.api_secret, str(time)),
        "timestamp": time
    }
    self.send(payload)
