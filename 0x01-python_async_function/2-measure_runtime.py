#!/usr/bin/env python3

""" an asynchronous coroutine that takes in an integer """

import asyncio
import random
from time import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ an asynchronous coroutine that takes in an integer """
    start = time()
    asyncio.run(wait_n(n, max_delay))
    end = time()
    return (end - start) / n
