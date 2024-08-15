#!/usr/bin/env python3

""" This module contains a function that takes a list of
 floats and returns their sum """

from typing import List, Tuple, Sequence


def element_length(lst: Sequence) -> List[Tuple[Sequence, int]]:
    """ This function takes a list of strings and returns
         a list of tuples """
    return [(i, len(i)) for i in lst]
