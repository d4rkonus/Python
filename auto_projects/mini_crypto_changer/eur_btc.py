#!/usr/bin/python3

import requests


def eur_btc(eur_amount: float) -> float:
    """Convert a EUR amount to BTC using the CoinGecko simple price API."""
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "eur",
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    btc_price = response.json()["bitcoin"]["eur"]
    return eur_amount / btc_price