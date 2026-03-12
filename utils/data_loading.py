import pandas as pd

# Data file path constants
DATA_DIR = "./data"
CUSTOMERS_FILE = "./data/olist_customers_dataset.csv"
GEOLOCATION_FILE = "./data/olist_geolocation_dataset.csv"
ORDER_ITEMS_FILE = "./data/olist_order_items_dataset.csv"
ORDER_PAYMENTS_FILE = "./data/olist_order_payments_dataset.csv"
ORDER_REVIEWS_FILE = "./data/olist_order_reviews_dataset.csv"
ORDERS_FILE = "./data/olist_orders_dataset.csv"
PRODUCTS_FILE = "./data/olist_products_dataset.csv"
SELLERS_FILE = "./data/olist_sellers_dataset.csv"
PRODUCT_CATEGORY_TRANSLATION_FILE = (
    "./data/product_category_name_translation.csv"
)


def read_csvs_from_data(file_path: str) -> pd.DataFrame:
    """Read a CSV file from the given path and return as a dataframe."""
    return pd.read_csv(file_path)


def merge_ecommerce_data() -> pd.DataFrame:
    """
    Read and merge orders, items, products, and reviews dataframes.

    Returns a merged dataframe with all relevant information.
    """
    orders = read_csvs_from_data(ORDERS_FILE)
    items = read_csvs_from_data(ORDER_ITEMS_FILE)
    products = read_csvs_from_data(PRODUCTS_FILE)
    reviews = read_csvs_from_data(ORDER_REVIEWS_FILE)

    # Merge orders with items
    merged = orders.merge(items, on="order_id", how="left")

    # Merge with products
    merged = merged.merge(products, on="product_id", how="left")

    # Merge with reviews
    merged = merged.merge(reviews, on="order_id", how="left")

    return merged
