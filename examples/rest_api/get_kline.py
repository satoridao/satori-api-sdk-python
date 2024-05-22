#!/usr/bin/env python

from satori.client import Client


client = Client()

if __name__ == '__main__':
    client = Client()
    print(client.kline("ETH-USD",period="1MIN"))
