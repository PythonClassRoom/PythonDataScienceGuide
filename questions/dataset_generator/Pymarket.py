"""
This script will create a large dataset about Pymarket
"""
import pandas as pd
import numpy as np

cols = ['Tom', 'Joe', 'Charlie']
total_records = 1000
total_nans_whole_row = 45
total_nans_cols = 154
total_limit = 21
limit = 10

def fill_nan(df):
    """
    This function adds some nans for the whole row of the df
    you can verify the number of nans by: df.isnull().sum(axis = 0)
    """
    for _ in range(total_nans_whole_row):
        df.iloc[np.random.randint(low=0, high=total_records)] = np.nan


def fill_nan_by_colum(df):
    """
    This function adds some nans for some columns of the df
    you can verify the number of nans by: df.isnull().sum(axis = 0)
    """
    for _ in range(total_nans_cols):
        df.iloc[np.random.randint(low=0, high=total_records)][np.random.randint(0, len(cols))] = np.nan


def fill_less_limit(df, limit):
    """
    This function adds for each colum values under limit
    """
    for _ in range(total_limit):
        df.iloc[np.random.randint(low=0, high=total_records)] = [np.round(np.random.uniform(
            0, limit), decimals=2) for i in range(len(cols))]


def generate_pymarket():
    data = np.round(np.random.uniform(0, 500, size=(total_records, len(cols))), decimals=2)
    idx = pd.date_range(end='07/12/2019', freq='D', periods=total_records)
    df = pd.DataFrame(columns=cols, data=data, index=idx)
    fill_nan(df)
    fill_nan_by_colum(df)
    fill_less_limit(df,limit)
    df.to_csv("pymarket.csv")


if __name__ == '__main__':
    generate_pymarket()
    print("PyMarket.csv generated")
    pass
