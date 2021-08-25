from application.validation import is_csv, is_10_rows, is_3_columns, is_dataframe_complete
from application.file_utils import read_csv_into_df
import pandas as pd
from pathlib import Path

TEST_DIR = Path('./test')
TEST_FILE = 'test.csv'
TEST_DF = read_csv_into_df(TEST_DIR / TEST_FILE)


def test_is_csv():
    assert is_csv(TEST_FILE)


def test_is_10_rows():
    assert is_10_rows(TEST_DF)


def test_is_3_columns():
    assert is_3_columns(TEST_DF)


def test_is_dataframe_complete():
    assert is_dataframe_complete(TEST_DF)


def test_is_not_csv():
    assert not is_csv('test.txt')


def test_is_not_10_rows():
    df = read_csv_into_df(TEST_DIR / 'test_fail_row.csv')
    assert not is_10_rows(df)


def test_is_not_3_columns():
    df = read_csv_into_df(TEST_DIR / 'test_fail_column.csv')
    assert not is_3_columns(df)


def test_is_not_dataframe_complete():
    df = read_csv_into_df(TEST_DIR / 'test_fail_complete.csv')
    assert not is_dataframe_complete(df)
