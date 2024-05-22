#!/usr/bin/env python
from satori.client import Client
from examples.utils.prepare_env import get_env

if __name__ == '__main__':
    config = get_env()
    cs = Client(api_key=config["api_key"], api_secret=config["api_secret"], base_url=config["base_url"])
    time = cs.time()["data"]
    # print(cs.order_list("ETH-USD",time))
    print(cs.cancel_order(entrustId=74078841,timestamp=str(time)))