#!/usr/bin/env python

from satori.client import Client


client = Client()

if __name__ == '__main__':
    client = Client()
    print(client.index_price("ETH-USD"))
    print(client.index_price("BTC-USD"))
