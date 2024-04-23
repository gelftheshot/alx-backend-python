#!/usr/bin/env python3

"""comment section"""

import random
import asyncio
import time


async def async_generator():
    """ the comment section """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
