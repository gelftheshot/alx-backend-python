#!/usr/bin/env python3

""" a python script to return list of generated objects"""

import asyncio
from typing import List
import random
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """ return list of generated objects"""
    return [i async for i in async_generator()]
