#!/usr/bin/env python3
"""
    a functon that take argument and reuthr mutiplier
"""
from typing import Callable
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_func(n: float) -> float:
        return n * multiplier
    return multiplier_func

