import pandas as pd

def transformations(features_df, sales_df, stores_df):
    features_df["Date"] = pd.to_datetime(features_df["Date"])
    sales_df['Date'] = pd.to_datetime(sales_df['Date'], dayfirst=True)

    markdowncolumns = ['MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5']
    features_df = features_df.drop(columns=markdowncolumns, errors='ignore')

    store_dimn = stores_df.drop_duplicates().reset_index(drop=True)
    date_dimn = sales_df[['Date', 'IsHoliday']].drop_duplicates().copy()

    date_dimn['year'] = date_dimn['Date'].dt.year
    date_dimn['month'] = date_dimn['Date'].dt.month
    date_dimn['week'] = date_dimn['Date'].dt.isocalendar().week.astype('int')

    features_dimn = features_df.drop_duplicates().reset_index(drop = True)
    fact_sales = sales_df.copy()

    def normalize(df):
        df.columns = df.columns.str.lower().str.replace('', '_')
        return df

    date_dimn = normalize(date_dimn)
    features_dimn = normalize(features_dimn)
    store_dimn = normalize(store_dimn)
    fact_sales = normalize(fact_sales)

    return date_dimn, features_dimn, store_dimn, fact_sales
    