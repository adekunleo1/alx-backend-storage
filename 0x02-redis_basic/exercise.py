#!/usr/bin/env python3
"""class module for Redis server exercises interaction"""
import redis
import uuid
import sys
from typing import Union, Callable, List, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """counts the amount of calls a method make"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """function method wrapper"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """history of inputs and outputs parameter"""
    input_list_key = method.__qualname__ + ":inputs"
    output_list_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def set_history(self, *args, **kwargs):
        """key list for wrapped function"""
        self._redis.rpush(input_list_key, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(output_list_key, str(data))
        return data

    return set_history


def replay(method: Callable) -> None:
    """ouput history of calls for a function"""
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"
    redis = method.__self__._redis
    count = redis.get(key).decode("utf-8")
    print(f"{key} was called {count} times:")
    inputList = redis.lrange(inputs, 0, -1)
    outputList = redis.lrange(outputs, 0, -1)
    redis_zipped = list(zip(inputList, outputList))
    for a, b in redis_zipped:
        attr, result = a.decode("utf-8"), b.decode("utf-8")
        print(f"{key}(*{attr}) -> {result}")


class Cache:
    """redis storage cache class"""

    def __init__(self):
        """Instantiate Redis DB """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """create and store any type of data in Redis DB"""
        key = str(uuid.uuid1())
        self._redis[key] = data
        return key

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[str, bytes, int, float]:
        """convert the data back to desired format"""
        return fn(self._redis.get(key)) if fn else self._redis.get(key)

    def get_str(self, b: bytes) -> str:
        """convert bytes to str"""
        return b.decode('utf-8')

    def get_int(self, b: bytes) -> int:
        """convert bytes to int"""
        return int.from_bytes(b, sys.byteorder)

    def get_list(self, k: str) -> List:
        """convert bytes from store to list"""
        return self._redis.lrange(k, 0, -1)
