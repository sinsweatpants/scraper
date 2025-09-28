# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

def parse_books(html_content):
    """
    Parses the HTML content to extract book data.

    Args:
        html_content (str): The HTML content of the page.

    Returns:
        list: A list of dictionaries, where each dictionary represents a book.
    """
    if not html_content:
        return []

    soup = BeautifulSoup(html_content, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    scraped_data = []

    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()

        scraped_data.append({
            'Title': title,
            'Price': price,
            'Availability': availability
        })

    return scraped_data