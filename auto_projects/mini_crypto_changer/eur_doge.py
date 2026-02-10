#!/usr/bin/python3

import requests


def eur_doge(eur_amount: float) -> float:
    """Convert a EUR amount to DOGE using the CoinGecko simple price API."""
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "dogecoin",
        "vs_currencies": "eur",
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    doge_price = response.json()["dogecoin"]["eur"]
    return eur_amount / doge_price