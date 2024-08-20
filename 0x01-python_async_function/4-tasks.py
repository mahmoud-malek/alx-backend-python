#!/usr/bin/env python3

""" an asynchronous coroutine that takes in an integer """

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ an asynchronous coroutine that takes in an integer """
    delays = [task_wait_random(max_delay) for i in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
