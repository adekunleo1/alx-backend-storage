#!/usr/bin/env python3
"""Implement an expiring web cache and tracker
"""


import redis
import requests
rd = redis.Redis()
count = 0


def get_page(url: str) -> str:
    """track URL request and cache the result"""


    rd.set(f"cached:{url}", count)
    resp = requests.get(url)
    rd.incr(f"count:{url}")
    rd.setex(f"cached:{url}", 10, rd.get(f"cached:{url}"))
    return resp.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
