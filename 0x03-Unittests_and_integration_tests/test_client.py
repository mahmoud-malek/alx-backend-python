#!/usr/bin/env python3

""" Test client module """

import unittest
from unittest import mock
from parameterized import parameterized
from client import GithubOrgClient
import client
from unittest.mock import MagicMock


class TestGithubOrgClient(unittest.TestCase):
    """ Test GithubOrgClient """

    @parameterized.expand([('google', ), ('abc', )])
    @mock.patch('client.get_json')
    def test_org(self, org: str, getJson: MagicMock) -> None:
        """ test org method """
        client = GithubOrgClient(org)
        self.assertEqual(client.org, getJson.return_value)
        getJson.assert_called_once_with(client.ORG_URL.format(org=org))

    def test_public_repos_url(self) -> None:
        """ tes tpublic repos url """
        with mock.patch('client.GithubOrgClient.org',
                        new_callable=mock.PropertyMock) as org:
            org.return_value = {'repos_url': 'http://google.com'}
            client = GithubOrgClient('google')
            self.assertEqual(client._public_repos_url, 'http://google.com')


if __name__ == '__main__':
    unittest.main()
