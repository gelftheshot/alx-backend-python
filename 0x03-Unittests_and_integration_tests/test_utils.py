#!/usr/bin/env python3
""" a test class for utils in test_utils file """
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock

class TestAccessNestedMap(unittest.TestCase):
    """ a test class for ascessnestmap fucnon """

    @parameterized.expand([({"a": 1}, ("a",),1),
                        ({"a": {"b": 2}}, ("a",), {"b": 2}),
                        ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map, path, e_result):
        """ the main method to test """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, e_result)
    
    @parameterized.expand([({}, ("a",), KeyError),
                        ({"a", 1}, ("a", "b"), KeyError),])
    def test_access_nested_map_exception(self, nested_map, path, e_error):
        """ the excepting checker """
        with self.assertRaises(e_error):
            access_nested_map(nested_map, path)
    
class TestGetJson(unittest.TestCase):
    """ testing get json from url """

    @parameterized.expand([
       ("http://example.com", {"payload": True}),
       ("http://holberton.io", {"payload": False})])
    @patch('requests.get')
    def test_get_json(self, test_url,test_payload, mock_get):
        """ mocking get function from utils """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        self.assertEqual(result, test_payload)