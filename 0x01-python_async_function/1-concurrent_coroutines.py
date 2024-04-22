#!/usr/bin/env python3
"""
    do multiple delay at the same time
"""

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Performing multiple waits and return a sorted list of delays"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delay_ls = await asyncio.gather(*tasks)
    return sorted(delay_ls)
