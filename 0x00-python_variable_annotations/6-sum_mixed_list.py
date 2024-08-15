#!/usr/bin/env python3

""" a module contain sum_mixed function that takes a list
and return their sum """

from typing import List, Union


def sum_mixed(mxd_lst: List[Union[int, float]]) -> float:
    """ This function takes a list of floats and returns their sum """
    return sum(mxd_lst)
