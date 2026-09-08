from ETL.extract import extract_products, extract_users
from ETL.transform import transformed_products, transformed_users
from ETL.load import load_to_postgres

def run_pipeline():
    print('starting pipeline')

    products_df = extract_products()
    users_df = extract_users()

    print('starting transformations')

    products_df = transformed_products(products_df)
    users_df = transformed_users(users_df)

    print('loading to postgres')

    load_to_postgres(products_df, 'products')
    load_to_postgres(users_df, 'users')

    print('pipeline completed')

if __name__ == '__main__':
    run_pipeline()


