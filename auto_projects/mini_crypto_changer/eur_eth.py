#!/usr/bin/python3

import requests


def eur_eth(eur_amount: float) -> float:
    """Convert a EUR amount to ETH using the CoinGecko simple price API."""
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "ethereum",
        "vs_currencies": "eur",
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    eth_price = response.json()["ethereum"]["eur"]
    return eur_amount / eth_price