# -*- coding: utf-8 -*-

import csv
import logging

# Get a logger instance for this module
logger = logging.getLogger(__name__)

def save_to_csv(data, filename, headers):
    """
    Saves a list of dictionaries to a CSV file.

    Args:
        data (list): The list of dictionaries to save.
        filename (str): The name of the output CSV file.
        headers (list): A list of strings for the CSV header.
    """
    if not data:
        logger.warning("No data provided to save.")
        return

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        logger.info(f"Data successfully saved to {filename}")
    except IOError as e:
        logger.error(f"I/O error occurred while writing to {filename}: {e}")