#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
from utils import access_nested_map
import unittest
from parameterized import parameterized
from typing import (
    Union,
    Dict,
    Tuple
)


class TestAccessNestedMap(unittest.TestCase):
    """ this is a test for access_nested_map """

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(
        self, nested_map: Dict, path: Tuple,
            expected: Union[int, Dict]) -> None:
        """ test for the access_nested_map function """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
