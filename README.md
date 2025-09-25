# Task 3: Web Scraper for News Headlines

## Objective
Scrape top headlines from a news website using Python.

## Tools
- Python
- requests
- BeautifulSoup

## How It Works
1. The script fetches HTML from **BBC News**.
2. BeautifulSoup parses the page to extract `<h2>` and `<h3>` tags.
3. The extracted headlines are saved into a text file (`headlines.txt`).

## Files
- `news_scraper.py` → Python script for scraping
- `headlines.txt` → Output file containing the scraped headlines

## Outcome
Automates data collection from a public website by saving top news headlines into a text file.
