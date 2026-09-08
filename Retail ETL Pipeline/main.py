from etl.extract import extract_files
from etl.load import load_data
from etl.transform import transformations

def run_pipeline():
    print('pipeline started')
    features_df, sales_df, stores_df = extract_files()
    date_dimn, features_dimn, store_dimn, fact_sales = transformations(features_df, sales_df, stores_df)
    load_data(date_dimn, features_dimn, store_dimn, fact_sales)

    print('pipeline run successfully')

if __name__ == '__main__':
    run_pipeline()
