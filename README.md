# Google Maps Scraper

This project scrapes data from Google Maps based on a search query and outputs it into a CSV file.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Google Maps Scraper is a Python-based tool designed to extract valuable information from Google Maps. It scrapes place names, reviews, websites, and other details and outputs the data into a structured CSV file.

## Features
- Scrapes detailed information such as place names, reviews, and websites.
- Outputs the scraped data into a user-friendly CSV file.
- Easy-to-use Python script.

## Installation

### Prerequisites
- Python 3.8 or higher
- Google Chrome installed

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/hassanahmad2136/google-maps-scraper.git
   cd google-maps-scraper
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Navigate to the project directory:
   ```bash
   cd google-maps-scraper
   ```

2. Run the scraper:
   ```bash
   python src/scrape.py
   ```

3. Output data will be saved to the `output/output.csv` file.

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

## Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and make changes as you'd like. Submit a pull request for review.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
