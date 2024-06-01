#!/usr/bin/env python3
"""
    type anonated funtion to kv that take string and int
    and return the tuple of them
"""
from typing import Union


def to_kv(k: int, v:Union[int, float]) -> tuple:
    """
        return tuple of the k and v
    """
    return (k, v**2)