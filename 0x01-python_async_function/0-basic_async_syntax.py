#!/usr/bin/env python3

""" a python asynchrous function that will wait for a random delay """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ return the random delay """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
