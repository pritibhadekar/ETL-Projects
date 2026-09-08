import pandas as pd

def extract_files():
    features_df = pd.read_csv(r"C:\Users\HP\OneDrive\Documents\ETL Projects\Retail ETL Pipeline\datasets\features_dataset.csv")
    sales_df = pd.read_csv(r"C:\Users\HP\OneDrive\Documents\ETL Projects\Retail ETL Pipeline\datasets\sales_dataset.csv")
    stores_df = pd.read_csv(r"C:\Users\HP\OneDrive\Documents\ETL Projects\Retail ETL Pipeline\datasets\stores_dataset.csv")

    print("features_dataset")
    print(features_df.head())
    print(features_df.dtypes)

    print("sales_dataset")
    print(sales_df.head())
    print(sales_df.dtypes)

    print("stores_dataset")
    print(stores_df.head())
    print(stores_df.dtypes)

    return features_df, sales_df, stores_df

