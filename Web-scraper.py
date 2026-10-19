
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from urllib.parse import urljoin

# Website URL
BASE_URL = "https://books.toscrape.com/"


# Step 1: Scrape all books
def scrape_products():

    current_url = BASE_URL
    all_products = []

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        while current_url:

            print("Scraping:", current_url)

            response = requests.get(
                current_url,
                headers=headers,
                timeout=15
            )

            response.raise_for_status()

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            products = soup.find_all(
                "article",
                class_="product_pod"
            )

            for product in products:

                try:
                    name = product.find(
                        "h3"
                    ).find("a")["title"]

                    price_text = product.find(
                        "p",
                        class_="price_color"
                    ).get_text(strip=True)

                    rating_tag = product.find(
                        "p",
                        class_="star-rating"
                    )

                    rating = rating_tag["class"][1]

                    availability_tag = product.find(
                        "p",
                        class_="instock availability"
                    )

                    availability = (
                        availability_tag.get_text(strip=True)
                    )

                    all_products.append({
                        "Product Name": name,
                        "Price": price_text,
                        "Rating": rating,
                        "Availability": availability
                    })

                except (AttributeError, KeyError, IndexError):
                    print("Skipped an incomplete product.")

            # Find next page
            next_button = soup.find(
                "li",
                class_="next"
            )

            if next_button:
                next_link = next_button.find("a")["href"]

                current_url = urljoin(
                    current_url,
                    next_link
                )
            else:
                current_url = None

        print("\nScraping completed!")
        return all_products

    except requests.RequestException as error:
        print("Website request failed:", error)
        return all_products


# Step 2: Clean and validate data
def clean_data(products):

    if not products:
        print("No product data found.")
        return pd.DataFrame(
            columns=[
                "Product Name",
                "Price",
                "Rating",
                "Availability"
            ]
        )

    df = pd.DataFrame(products)

    print("\n--- DATA VALIDATION ---")

    # Check total records
    print("Records before cleaning:", len(df))

    # Check missing values
    print("\nMissing values:")
    print(df.isnull().sum())

    # Remove currency symbol and convert price
    df["Price"] = (
        df["Price"]
        .astype(str)
        .str.replace("£", "", regex=False)
        .str.extract(r"(\d+\.\d+)")[0]
    )

    df["Price"] = pd.to_numeric(
        df["Price"],
        errors="coerce"
    )

    # Convert rating words into numbers
    rating_mapping = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    df["Rating"] = df["Rating"].map(
        rating_mapping
    )

    # Check valid prices
    invalid_prices = (
        df["Price"].isna() | (df["Price"] < 0)
    )

    print("\nInvalid prices:", invalid_prices.sum())

    # Check valid ratings
    invalid_ratings = (
        df["Rating"].isna()
        | ~df["Rating"].isin([1, 2, 3, 4, 5])
    )

    print("Invalid ratings:", invalid_ratings.sum())

    # Remove duplicate rows
    duplicates = df.duplicated().sum()
    print("Duplicate rows:", duplicates)

    df.drop_duplicates(inplace=True)

    # Remove rows with missing or invalid data
    df.dropna(inplace=True)
    df = df[df["Price"] >= 0]
    df = df[df["Rating"].isin([1, 2, 3, 4, 5])]

    # Check empty product names
    df["Product Name"] = df["Product Name"].astype(str).str.strip()
    df = df[df["Product Name"] != ""]

    # Reset index
    df.reset_index(drop=True, inplace=True)

    print("\nRecords after cleaning:", len(df))
    print("Data cleaning completed!")

    return df


# Step 3: Export data and report
def export_to_csv(df):

    os.makedirs("output", exist_ok=True)

    file_path = "output/products_cleaned.csv"

    df.to_csv(
        file_path,
        index=False,
        encoding="utf-8-sig"
    )

    print("\n--- FINAL REPORT ---")
    print("Total products:", len(df))

    print("\nColumn data types:")
    print(df.dtypes)

    print("\nMissing values after cleaning:")
    print(df.isnull().sum())

    print("\nFirst 10 products:")
    print(df.head(10).to_string(index=False))

    print("\nCSV saved at:", file_path)


# Step 4: Run the project
if __name__ == "__main__":

    try:
        products = scrape_products()

        df = clean_data(products)

        if not df.empty:
            export_to_csv(df)
        else:
            print("No valid data available to export.")

    except Exception as error:
        print("An unexpected error occurred:", error)
