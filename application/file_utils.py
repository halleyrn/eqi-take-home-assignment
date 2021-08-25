import pandas as pd
from pathlib import Path
from typing import Union


def read_csv_into_df(filename: Union[str, Path]):
    return pd.read_csv(filename, header=None)
