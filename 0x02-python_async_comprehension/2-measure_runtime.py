#!/usr/bin/env python3

""" measure the time for excution of the functions """
from time import time
from asyncio import gather
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """ measure the tim taken for comprtion"""
    time_0 = time()
    await gather(
            async_comprehension(), async_comprehension(),
            async_comprehension(), async_comprehension())
    time_1 = time()
    return time_1 - time_0
