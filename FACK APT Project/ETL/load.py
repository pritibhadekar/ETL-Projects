from sqlalchemy import create_engine

host = 'localhost'
port = 5432
username = 'postgres'
pwd = pwd
db_name = 'fack_store_db'

def load_to_postgres(df, table_name):
    engine = create_engine(f'postgresql://{username}:{pwd}@{host}:{port}/{db_name}')

    df.to_sql(table_name,
               engine,
               if_exists = 'replace',
               index = False)

    print('data loaded to postgres successfully')