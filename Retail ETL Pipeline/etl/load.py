from sqlalchemy import create_engine

def load_data(date_dimn, features_dimn, store_dimn, fact_sales):
    db_name = 'fack_store_db'
    db_host = 'localhost'
    db_port = '5432'
    pwd = your_pwd
    user = 'postgres'

    engine = create_engine(f'postgresql://{user}:{pwd}@{db_host}:{db_port}/{db_name}')

    date_dimn.to_sql('date_dim', engine, schema = 'public', if_exists = 'replace', index = False)
    features_dimn.to_sql('features_dimn', engine, schema = 'public', if_exists = 'replace', index = False)
    store_dimn.to_sql('store_dimn', engine, schema = 'public', if_exists = 'replace', index = False)
    fact_sales.to_sql('fact_sales', engine, schema = 'public', if_exists = 'replace', index = False)

    print('data loaded to postgresql successfully')
   