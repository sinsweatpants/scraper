# -*- coding: utf-8 -*-

import requests
import logging

# Get a logger instance for this module
logger = logging.getLogger(__name__)

def fetch_page(url):
    """
    Fetches the content of a web page.

    Args:
        url (str): The URL of the page to fetch.

    Returns:
        str: The HTML content of the page, or None if an error occurs.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        logger.info(f"Successfully fetched page: {url}")
        return response.content
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching page {url}: {e}")
        return None