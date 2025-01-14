# Google Maps Scraper

This project scrapes data from Google Maps based on a search query and outputs it into a CSV file.

## Features
- Scrapes place names, reviews, websites, and other details.
- Outputs data into a structured CSV file.

## Project Structure
```
google-maps-scraper/
├── src/
│   ├── scrape.py       # Main script for scraping
│   ├── helpers.py      # Helper functions
│   ├── constants.py    # Stores constants
├── output/
│   └── output.csv      # Output data
├── README.md           # Documentation
├── requirements.txt    # Dependencies
└── .gitignore          # Ignore unnecessary files
```

## Prerequisites
- Python 3.8 or higher
- Google Chrome installed

## Setup and Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/google-maps-scraper.git
   cd google-maps-scraper
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the scraper:
   ```bash
   python src/scrape.py
   ```

4. Output data will be saved to the `output/output.csv` file.
