#!/usr/bin/env python

from satori.client import Client


client = Client()

if __name__ == '__main__':
    client = Client()
    print(client.depth("ETH-USD",page_size= 2))
    print(client.depth("ETH-USD"))



