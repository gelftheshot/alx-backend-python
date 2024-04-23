#!/usr/bin/env python3

""" the comment section """

import asyncio
import time
import random
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension():
    """ the comment section """
    return [i async for i in async_generator()]
