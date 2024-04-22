#!/usr/bin/env python3
'''
    running at the same time using a given function
'''

from typing import List
import asyncio
import random

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''Execute task_wait_random and returns sorted list of delay'''
    li_1 = []
    li_2 = []
    for i in range(n):
        dt = task_wait_random(max_delay)
        dt.add_done_callback(lambda x: li_2.append(x.result()))
        li_1.append(dt)

    for spawn in li_1:
        await spawn

    return li_2
