#!/usr/bin/env python3

"""Measure runtime"""

import asyncio
import random
import time
from typing import List

async_generator = __import__('0-async_generator').async_generator
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure runtime"""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start


if __name__ == '__main__':
    print(asyncio.run(measure_runtime()))
