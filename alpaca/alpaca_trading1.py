import alpaca_trade_api as tradeapi
import logging
from pathlib import Path
import sys, os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ALPACA_API_KEY")
api_secret = os.getenv("ALPACA_API_SECRET")
base_url = "https://paper-api.alpaca.markets"


def get_account():
    api = tradeapi.REST(api_key, api_secret, base_url, api_version="v2")

    try:
        account = api.get_account()
        print(account)
        logging.getLogger().setLevel(logging.DEBUG)
        logging.getLogger().debug(" ".join(["Get Account", str(account)]))
        logging.getLogger().setLevel(logging.ERROR)

    except (KeyboardInterrupt, SystemExit) as e:
        logging.exception("Exception occurred")
        raise e


def get_all_open_position():
    api = tradeapi.REST(api_key, api_secret, base_url, api_version="v2")
    try:
        positions = api.list_positions()
        logging.getLogger().setLevel(logging.DEBUG)
        logging.getLogger().debug("List all position")
        for position in positions:
            print(position)
            logging.getLogger().debug(" ".join(["Position", str(position)]))
        logging.getLogger().setLevel(logging.ERROR)

    except (KeyboardInterrupt, SystemExit) as e:
        logging.exception("Exception occurred")
        raise e


def place_buy_order():
    api = tradeapi.REST(api_key, api_secret, base_url, api_version="v2")
    try:
        symbol = "BTC/USD"
        qty = 1
        order = api.submit_order(symbol, qty=qty, time_in_force="gtc")
        print(order)
        logging.getLogger().setLevel(logging.DEBUG)
        logging.getLogger().debug(" ".join(["Place a buy order", symbol, str(qty)]))
        logging.getLogger().debug(order)
        logging.getLogger().setLevel(logging.ERROR)

    except (KeyboardInterrupt, SystemExit) as e:
        logging.exception("Exception occurred")
        raise e


def main():
    log_file = Path(__file__).stem + ".log"
    logging.basicConfig(
        filename=log_file,
        format="%(asctime)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
        level=logging.ERROR,
    )
    get_account()
    get_all_open_position()
    # place_buy_order()
    # get_all_open_position()


if __name__ == "__main__":
    main()
