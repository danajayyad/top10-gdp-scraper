# Top 10 Largest Economies Scraper

## Overview
This project extracts the **top 10 largest economies of the world** by GDP in **Billion USD**, using data logged by the **International Monetary Fund (IMF)** from Wikipedia.  

It demonstrates web scraping with **pandas**, data cleaning with **pandas & numpy**, and exporting the results to a CSV file.

---

## Features
- Extracts country names and GDP data from Wikipedia tables.  
- Converts GDP from **Millions USD → Billions USD**, rounded to **2 decimal places**.  
- Saves the cleaned data to `Largest_economies.csv`.  
- Modular, reusable functions for scraping and processing.

---

## Requirements
- Python 3.7+  
- Libraries: `pandas`, `numpy`

Install required libraries:

```bash
pip install pandas numpy
