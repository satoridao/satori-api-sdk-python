#!/usr/bin/env python
from satori.client import Client
from examples.utils.prepare_env import get_env

if __name__ == '__main__':
    config = get_env()
    cs = Client(api_key=config["api_key"], api_secret=config["api_secret"], base_url=config["base_url"])
    time = cs.time()["data"]
    print(cs.position_list(pairName="ETH-USD", timestamp=time))
    print(cs.close_position(contractPositionId=1293630, price='3030', isMarket=True, quantity="0.01", timestamp=str(time)))
