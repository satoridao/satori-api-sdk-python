from satori.lib.utils import hmac_hashing


def trade_data(self, pairName: str, period: str):
    time = self.get_time()
    payload = {
        "pair": pairName,
        "period": period,
        "method": self.ACTION_SUBSCRIBE,
        "event": "api_trade",
        "apiKey": self.api_key,
        "signature": hmac_hashing(self.api_secret, str(time)),
        "timestamp": time
    }
    self.send(payload)


def trade_current(self, pairName: str):
    time = self.get_time()
    payload = {
        "pair": pairName,
        "method": self.ACTION_SUBSCRIBE,
        "event": "api_spot_deals",
        "apiKey": self.api_key,
        "signature": hmac_hashing(self.api_secret, str(time)),
        "timestamp": time
    }
    self.send(payload)


def trade_immediately(self, pairName: str):
    time = self.get_time()
    payload = {
        "pair": pairName,
        "method": self.ACTION_SUBSCRIBE,
        "event": "api_deal_user",
        "apiKey": self.api_key,
        "signature": hmac_hashing(self.api_secret, str(time)),
        "timestamp": time
    }
    self.send(payload)
