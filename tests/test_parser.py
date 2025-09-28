# -*- coding: utf-8 -*-

import unittest
from scraper.parser import parse_books

class TestParser(unittest.TestCase):

    def test_parse_books_with_valid_html(self):
        """
        Test that the parser correctly extracts data from a sample HTML.
        """
        sample_html = """
        <html>
            <body>
                <article class="product_pod">
                    <h3><a title="Book 1">Book 1</a></h3>
                    <p class="price_color">£10.00</p>
                    <p class="instock availability">In stock</p>
                </article>
                <article class="product_pod">
                    <h3><a title="Book 2">Book 2</a></h3>
                    <p class="price_color">£20.50</p>
                    <p class="instock availability">
                        In stock
                    </p>
                </article>
            </body>
        </html>
        """
        expected_data = [
            {'Title': 'Book 1', 'Price': '£10.00', 'Availability': 'In stock'},
            {'Title': 'Book 2', 'Price': '£20.50', 'Availability': 'In stock'}
        ]

        parsed_data = parse_books(sample_html)
        self.assertEqual(parsed_data, expected_data)

    def test_parse_books_with_no_books(self):
        """
        Test that the parser returns an empty list if no books are found.
        """
        sample_html = "<html><body><p>No books here.</p></body></html>"
        parsed_data = parse_books(sample_html)
        self.assertEqual(parsed_data, [])

    def test_parse_books_with_empty_html(self):
        """
        Test that the parser returns an empty list for empty or None HTML content.
        """
        self.assertEqual(parse_books(""), [])
        self.assertEqual(parse_books(None), [])

if __name__ == '__main__':
    unittest.main()