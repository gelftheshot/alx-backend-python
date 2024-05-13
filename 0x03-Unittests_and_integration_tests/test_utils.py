#!/usr/bin/env python3
""" a test class for utils in test_utils file """
access_nested_map = __import__('utils').access_nested_map
import unittest
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    """ a test class for ascessnestmap fucnon """

    @parameterized.expand([({"a": 1}, ("a",),1),
                        ({"a": {"b": 2}}, ("a",), {"b": 2}),
                        ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map, path, e_result):
        """ the main method to test """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, e_result)