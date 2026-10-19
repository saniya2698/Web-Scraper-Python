# 🕷️ Web Scraping & Data Cleaning Project

A Python-based web scraping project that extracts book information from [Books to Scrape](https://books.toscrape.com/) using Requests and BeautifulSoup, cleans and validates the collected data using Pandas, and exports the processed dataset to a CSV file.

## 📌 Project Overview

This project demonstrates the complete workflow of a web scraping and data cleaning system, from collecting data from a website to exporting a structured dataset for further analysis.

### 🔄 Project Workflow

```text
Website
   ↓
Send HTTP Request
   ↓
Receive HTML Response
   ↓
Parse HTML using BeautifulSoup
   ↓
Extract Book Information
   ↓
Navigate Multiple Pages
   ↓
Validate and Clean Data
   ↓
Check Missing Values & Duplicates
   ↓
Convert Prices and Ratings
   ↓
Export Cleaned Data to CSV
```

The scraper automatically navigates through available pages and extracts the following information:

- 📖 **Product Name** — Title of the book
- 💰 **Price** — Book price converted into a numeric value
- ⭐ **Rating** — Book rating converted into a number from 1 to 5
- 📦 **Availability** — Stock availability displayed on the website

## ✨ Features

- Automatically scrapes book information from multiple pages.
- Sends HTTP requests using the Requests library.
- Parses website HTML using BeautifulSoup.
- Extracts product names, prices, ratings, and availability.
- Handles pagination to navigate through multiple pages.
- Removes currency symbols from price values.
- Converts prices into numeric data types.
- Converts rating words into numeric values.
- Identifies and removes duplicate records.
- Checks for missing and invalid data.
- Removes incomplete or invalid records.
- Resets the DataFrame index after cleaning.
- Creates the output directory automatically.
- Exports the cleaned dataset to a CSV file.
- Displays scraping progress and data validation results in the console.
- Handles website request errors and incomplete product information.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Requests | Sending HTTP requests to the website |
| BeautifulSoup | Parsing HTML and extracting product details |
| Pandas | Data cleaning, validation, and transformation |
| CSV | Storing the cleaned dataset |
| OS Module | Creating the output directory |
| urllib.parse | Joining URLs for pagination |

## 📂 Project Structure

```text
web-scraping-project/
│
├── scraper.py
├── requirements.txt
├── README.md
│
└── output/
    └── products_cleaned.csv
```

### File Description

- `scraper.py` — Contains the main scraping, data cleaning, validation, and export functions.
- `requirements.txt` — Contains the required Python libraries.
- `README.md` — Provides project documentation and setup instructions.
- `output/products_cleaned.csv` — Stores the cleaned product dataset generated after execution.

## 🔧 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/web-scraping-project.git
```

Replace `your-username` with your GitHub username and use your actual repository name.

### 2. Navigate to the Project Directory

```bash
cd web-scraping-project
```

### 3. Install Required Libraries

Run the following command:

```bash
pip install -r requirements.txt
```

Alternatively, install the libraries individually:

```bash
pip install requests beautifulsoup4 pandas
```

### 4. Configure Requirements

Create a `requirements.txt` file with the following contents:

```text
requests
beautifulsoup4
pandas
```

## ▶️ Run the Project

Execute the following command in the terminal:

```bash
python scraper.py
```

The program will begin scraping the website, process the collected records, perform validation checks, and export the cleaned dataset.

### Example Console Output

```text
Scraping: https://books.toscrape.com/
Scraping: https://books.toscrape.com/catalogue/page-2.html
Scraping: https://books.toscrape.com/catalogue/page-3.html

Scraping completed!

--- DATA VALIDATION ---
Records before cleaning: [actual count]

Missing values:
Product Name      0
Price             0
Rating            0
Availability      0

Invalid prices: 0
Invalid ratings: 0
Duplicate rows: 0

Records after cleaning: [actual count]
Data cleaning completed!

CSV saved at: output/products_cleaned.csv
```

*Note: The values shown are illustrative. Actual counts and validation results depend on the data returned by the website.*

## 📊 Extracted Data

The generated dataset contains four columns:

| Column | Description | Example |
|---|---|---|
| Product Name | Name of the book | A Light in the Attic |
| Price | Book price as a numeric value | 51.77 |
| Rating | Rating represented as a number | 3 |
| Availability | Stock status | In stock |

### Example Dataset

The following values illustrate the output format:

| Product Name | Price (£) | Rating | Availability |
|---|---:|---:|---|
| A Light in the Attic | 51.77 | 3 | In stock |
| Tipping the Velvet | 53.74 | 1 | In stock |
| Soumission | 50.10 | 1 | In stock |

These are example records; the actual CSV file is generated by running the scraper.

## 🧹 Data Cleaning and Validation

The project performs several data-cleaning operations using Pandas before exporting the dataset.

### 1. Currency Removal

Removes the pound symbol from the price.

```text
£51.77 → 51.77
```

### 2. Price Conversion

Converts price strings into numeric floating-point values.

```text
"51.77" → 51.77
```

This makes the price column suitable for numerical calculations and analysis.

### 3. Rating Conversion

Converts rating words into numeric values.

| Original Rating | Numeric Rating |
|---|---:|
| One | 1 |
| Two | 2 |
| Three | 3 |
| Four | 4 |
| Five | 5 |

### 4. Duplicate Removal

Identifies and removes duplicate rows using Pandas.

```python
df.drop_duplicates(inplace=True)
```

### 5. Missing Value Removal

Removes rows containing missing values.

```python
df.dropna(inplace=True)
```

### 6. Invalid Data Checks

The project checks for:

- Missing or invalid prices.
- Negative prices.
- Missing or out-of-range ratings.
- Empty product names.
- Duplicate records.

After validation, the DataFrame index is reset and the cleaned dataset is exported.

## 🔄 Pagination

The scraper uses the website's **Next** button to navigate between pages automatically.

```text
Page 1
   ↓
Find Next Button
   ↓
Page 2
   ↓
Find Next Button
   ↓
Page 3
   ↓
Continue Until Last Page
   ↓
Stop Scraping
```

This approach allows the project to collect books from multiple pages instead of limiting extraction to the first page.

## 📁 Output

After successful execution, the cleaned dataset is saved at:

```text
output/products_cleaned.csv
```

The `output` directory is created automatically if it does not exist.

The CSV file can be opened in Microsoft Excel for sorting, filtering, reviewing, and further data analysis.

## 🧪 Testing

The project can be tested using the following scenarios:

| Test Case | Expected Result |
|---|---|
| Website is accessible | HTML response is received |
| Product information is available | Product details are extracted |
| Multiple pages exist | Pagination continues to the next page |
| Price contains a currency symbol | Symbol is removed and price is converted |
| Rating is available as a word | Rating is converted to a number |
| Duplicate records exist | Duplicate rows are removed |
| Missing or invalid values exist | Invalid records are checked and filtered |
| Website request fails | Request error is displayed |
| Scraping completes successfully | CSV file is generated |

Actual test results should be recorded after executing the project.

## 🎯 Learning Objectives

This project was developed to gain practical experience in:

- Python programming and functions.
- HTTP requests and website responses.
- HTML structure and parsing.
- BeautifulSoup selectors.
- Web scraping and data extraction.
- Pagination handling.
- Data cleaning using Pandas.
- Data type conversion.
- Data validation and quality checks.
- Duplicate and missing-value handling.
- CSV file export and file management.
- Exception handling.

## ⚠️ Limitations

- The scraper depends on the availability and HTML structure of the target website.
- Changes to the website may require updates to the scraping logic.
- Network problems may interrupt data collection.
- The project uses basic validation rules and may require additional checks for other datasets.
- The scraper is designed for the Books to Scrape practice website and may need modifications for other websites.

## 🚀 Future Improvements

- Export data to Excel format.
- Generate charts and visual reports using Matplotlib or Plotly.
- Store scraped data in an SQLite or MySQL database.
- Add logging and retry mechanisms for failed requests.
- Add configurable scraping options.
- Generate a detailed data quality report.
- Extend validation to cover more data-quality rules.

## 🌐 Data Source

**Books to Scrape:** https://books.toscrape.com/

This website is designed for practicing web scraping and learning how to extract structured information from HTML pages.

## 👨‍💻 Author

**Your Name**

Python | Web Scraping | Data Cleaning | Data Analysis

## 📄 Disclaimer

This project is intended for educational and academic purposes. Always review the target website's terms, applicable access rules, and rate limits before scraping data from any website.
