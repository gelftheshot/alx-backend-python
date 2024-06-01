#!/usr/bin/env python3
"""
    type anonated funtion to kv that take string and int
    and return the tuple of them
"""
from typing import Union
from typing import Tuple

def to_kv(k: str, v:Union[int, float]) -> Tuple:
    """
        return tuple of the k and v
    """
    return (k, v**2)