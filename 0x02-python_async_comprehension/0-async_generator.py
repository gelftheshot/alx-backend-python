#!/usr/bin/env python3

"""a python script to genrate random numbers from 0-10"""

import random
import asyncio
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """ Generate random nubers from 0 up to 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
