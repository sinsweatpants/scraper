# -*- coding: utf-8 -*-

import logging
from scraper.fetcher import fetch_page
from scraper.parser import parse_books
from scraper.storage import save_to_csv

# --- Configuration ---
TARGET_URL = "http://books.toscrape.com/"
OUTPUT_FILE = "scraped_books.csv" # Renaming back for consistency
CSV_HEADERS = ['Title', 'Price', 'Availability']
LOG_FILE = "scraper.log"

def setup_logging():
    """Configures the logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] - %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )

def main():
    """
    Main function to orchestrate the web scraping process.
    """
    setup_logging()
    logging.info("Starting the scraping process...")

    # Step 1: Fetch the web page content
    logging.info(f"Fetching content from {TARGET_URL}")
    html_content = fetch_page(TARGET_URL)

    if html_content:
        # Step 2: Parse the HTML and extract data
        logging.info("Parsing HTML content.")
        scraped_data = parse_books(html_content)
        logging.info(f"Found {len(scraped_data)} books to scrape.")

        # Step 3: Save the data to a CSV file
        save_to_csv(scraped_data, OUTPUT_FILE, CSV_HEADERS)
    else:
        logging.error("Failed to fetch HTML content. Halting process.")

    logging.info("Scraping process finished.")

if __name__ == "__main__":
    main()