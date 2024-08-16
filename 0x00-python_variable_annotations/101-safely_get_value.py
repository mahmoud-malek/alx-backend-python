#!/usr/bin/env python3
"""Type-annotated function safely_get_value"""

from typing import Union, Mapping, Any, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Type-annotated function safely_get_value
    that takes a dictionary input and returns its value"""
    if key in dct:
        return dct[key]
    else:
        return default
