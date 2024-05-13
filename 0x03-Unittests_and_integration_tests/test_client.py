#!/usr/bin/env python3
GithubOrgClient = __import__('client').GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock

class TestGithubOrgClient(unittest.TestCase):
    """ a class to test githuborg client"""


    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, get_patch):
        """ Test the org of the client """
        get_patch.return_value = expected
        x = GithubOrgClient(org)
        self.assertEqual(x.org, expected)
        get_patch.assert_called_once_with("https://api.github.com/orgs/"+org)

    def test_public_repos_url(self):
        """ test that _public_repos_url works """
        expected = "www.gelf.com"
        payload = {"repos_url": expected}
        to_mock = 'client.GithubOrgClient.org'
        with patch(to_mock, PropertyMock(return_value=payload)):
            cli = GithubOrgClient("x")
            self.assertEqual(cli._public_repos_url, expected)
        