import time
from satori.websocket.client.websocket_api import WebsocketAPIClient
from examples.utils.prepare_env import get_env


def message_handler(_, message):
    print(message)


if __name__ == '__main__':
    config = get_env()
    my_client = WebsocketAPIClient(api_key=config["api_key"], on_message=message_handler,
                                   api_secret=config["api_secret"], stream_url=config["ws_url"],
                                   proxies={'https': 'http://127.0.0.1:7890'})
    my_client.trade_data("ETH-USD","1MIN")
    time.sleep(50)
    my_client.stop()
