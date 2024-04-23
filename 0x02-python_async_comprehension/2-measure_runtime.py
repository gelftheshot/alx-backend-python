#!/usr/bin/python

""" the comment seciton """
import time
import asyncio
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime():
    """ the comment section """
    time_0 = time.time()
    await asyncio.gather(
            async_comprehension(), async_comprehension(),
            async_comprehension(), async_comprehension()
            )
    time_1 = time.time()
    return(time_1 - time_0)
