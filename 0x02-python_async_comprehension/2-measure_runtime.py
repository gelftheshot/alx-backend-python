#!/usr/bin/env python3

""" measure the time for excution of the functions """
import time
import asyncio
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> int:
    """ measure the tim taken for comprtion"""
    time_0 = time.time()
    await asyncio.gather(
            async_comprehension(), async_comprehension(),
            async_comprehension(), async_comprehension()
            )
    time_1 = time.time()
    return(time_1 - time_0)
