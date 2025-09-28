# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch, Mock
import requests
from scraper.fetcher import fetch_page

class TestFetcher(unittest.TestCase):

    @patch('scraper.fetcher.requests.get')
    def test_fetch_page_success(self, mock_get):
        """
        Test that fetch_page returns content on a successful request.
        """
        # Configure the mock to simulate a successful response
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.content = b"<html>Success</html>"
        mock_get.return_value = mock_response

        # Call the function
        content = fetch_page("http://example.com")

        # Assertions
        self.assertEqual(content, b"<html>Success</html>")
        mock_get.assert_called_once_with("http://example.com", headers=unittest.mock.ANY)

    @patch('scraper.fetcher.requests.get')
    def test_fetch_page_failure(self, mock_get):
        """
        Test that fetch_page returns None and logs an error on a failed request.
        """
        # Configure the mock to simulate a request exception
        mock_get.side_effect = requests.exceptions.RequestException("Test error")

        # Call the function and capture log output
        with self.assertLogs('scraper.fetcher', level='ERROR') as cm:
            content = fetch_page("http://example.com")

            # Assertions
            self.assertIsNone(content)
            self.assertIn("Error fetching page http://example.com: Test error", cm.output[0])

        mock_get.assert_called_once_with("http://example.com", headers=unittest.mock.ANY)

if __name__ == '__main__':
    unittest.main()