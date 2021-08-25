import pandas as pd
import numpy as np


def is_csv(filename: str):
    """ Returns true if FILENAME ends with 'csv', meaning
    the file is a CSV
    """
    return filename.endswith('.csv')


def is_10_rows(df: pd.DataFrame):
    """ Returns true if DF has 10 rows
    """
    return len(df.index) == 10


def is_3_columns(df: pd.DataFrame):
    """ Returns true if DF has 3 columns
    """
    return len(df.columns) == 3


def is_dataframe_complete(df: pd.DataFrame):
    """ Returns true if data is present in every cell (no NaNs)
    """
    return np.all(~df.isnull())
