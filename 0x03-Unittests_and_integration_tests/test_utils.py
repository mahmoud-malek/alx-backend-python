#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
from utils import access_nested_map
from utils import get_json
from utils import memoize
import unittest
from unittest import mock
from parameterized import parameterized
from typing import (
    Union,
    Dict,
    Tuple
)


class TestAccessNestedMap(unittest.TestCase):
    """ this is a test for access_nested_map """

    @parameterized.expand([
        ({
            "a": 1
        }, ["a"], 1),
        ({
            "a": {
                "b": 2
            }
        }, ["a"], {
            "b": 2
        }),
        ({
            "a": {
                "b": 2
            }
        }, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple,
                               expected: Union[int, Dict]) -> None:
        """ test for the access_nested_map function """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ["a"], KeyError),
        ({"a": 1}, ["a", "b"], KeyError),]
    )
    def test_access_nested_map_exception(self, nested_map: Dict, path: Tuple,
                                         expected: KeyError) -> None:
        """ test for key error exception """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ a suit of testing for GetJson method """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url: str, payload: Dict) -> None:
        """ a method to test the getjson """
        with mock.patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = payload
            self.assertEqual(get_json(url), payload)


class TestMemoize(unittest.TestCase):
    """ a suit of testing for memoize method """

    def test_memoize(self) -> None:
        """ a method to test the memoize """

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method') as mock_a_method:
            mycls = TestClass()
            mycls.a_property
            mycls.a_property
            mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
