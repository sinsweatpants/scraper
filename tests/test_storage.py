# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch, mock_open, MagicMock
from scraper.storage import save_to_csv

class TestStorage(unittest.TestCase):

    def test_save_to_csv_with_valid_data(self):
        """
        Test that save_to_csv writes the correct data to a file.
        """
        sample_data = [
            {'Title': 'Book 1', 'Price': '£10.00', 'Availability': 'In stock'}
        ]
        headers = ['Title', 'Price', 'Availability']

        # Mock the open function
        m = mock_open()
        with patch('builtins.open', m):
            save_to_csv(sample_data, 'test.csv', headers)

        # Check that open was called correctly
        m.assert_called_once_with('test.csv', 'w', newline='', encoding='utf-8')

        # Check what was written to the file
        handle = m()
        # The DictWriter writes the header first
        handle.write.assert_any_call('Title,Price,Availability\r\n')
        # Then it writes the rows
        handle.write.assert_any_call('Book 1,£10.00,In stock\r\n')

    def test_save_to_csv_with_no_data(self):
        """
        Test that save_to_csv does nothing and logs a warning if data is empty.
        """
        m = mock_open()
        with patch('builtins.open', m):
            with self.assertLogs('scraper.storage', level='WARNING') as cm:
                save_to_csv([], 'test.csv', ['Title'])

                # Check that a warning was logged
                self.assertIn("No data provided to save.", cm.output[0])

                # Check that open was not called
                m.assert_not_called()

    @patch('builtins.open')
    def test_save_to_csv_io_error(self, mock_open_func):
        """
        Test that save_to_csv logs an error if an IOError occurs.
        """
        # Configure the mock to raise an IOError
        mock_open_func.side_effect = IOError("Permission denied")

        sample_data = [{'Title': 'Book 1'}]
        headers = ['Title']

        with self.assertLogs('scraper.storage', level='ERROR') as cm:
            save_to_csv(sample_data, 'test.csv', headers)

            # Check that an error was logged
            self.assertIn("I/O error occurred while writing to test.csv: Permission denied", cm.output[0])

if __name__ == '__main__':
    unittest.main()