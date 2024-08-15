#!/usr/bin/env python3

""" This module contains a function that takes a list of
 floats and returns their sum """

from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[int, float]:
    """ This function takes a float and returns a tuple """
    return (k, v ** 2)
