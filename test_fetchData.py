import numpy as np
import pandas as pd
import pytest
from fetchData import combined_df, apple_data, google_data, microsoft_data, jpmc_data, wfc_data, jnj_data, pfizer_data, merk_data, exxon_data, chevron_data, conocoPhillips_data, verizon_data, facebook_data, atnt_data

def test_shape_nonzero():
    # Assert that the DataFrame is not empty
    assert not combined_df.empty
    assert combined_df.shape == (66042, 10)

def test_not_empty():
    assert not apple_data.empty, "The DataFrame is empty"
    assert not google_data.empty, "The DataFrame is empty"
    assert not microsoft_data.empty, "The DataFrame is empty"
    assert not jpmc_data.empty, "The DataFrame is empty"
    assert not wfc_data.empty, "The DataFrame is empty"
    assert not jnj_data.empty, "The DataFrame is empty"
    assert not pfizer_data.empty, "The DataFrame is empty"
    assert not merk_data.empty, "The DataFrame is empty"
    assert not exxon_data.empty, "The DataFrame is empty"
    assert not chevron_data.empty, "The DataFrame is empty"
    assert not conocoPhillips_data.empty, "The DataFrame is empty"
    assert not verizon_data.empty, "The DataFrame is empty"
    assert not facebook_data.empty, "The DataFrame is empty"
    assert not atnt_data.empty, "The DataFrame is empty"

def test_columns():
    expected_columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'MACD', 'Signal Line', 'company_name']
    assert all(column in apple_data.columns for column in expected_columns), "Missing columns in DataFrame"
    assert all(column in google_data.columns for column in expected_columns), "Missing columns in DataFrame"
    assert all(column in microsoft_data.columns for column in expected_columns), "Missing columns in DataFrame"
    assert all(column in jpmc_data.columns for column in expected_columns), "Missing columns in DataFrame"
    assert all(column in wfc_data.columns for column in expected_columns), "Missing columns in DataFrame"
    assert all(column in jnj_data.columns for column in expected_columns), "Missing columns in DataFrame"
    assert all(column in pfizer_data.columns for column in expected_columns), "Missing columns in DataFrame"
    assert all(column in merk_data.columns for column in expected_columns), "Missing columns in DataFrame"
    assert all(column in chevron_data.columns for column in expected_columns), "Missing columns in DataFrame"
    assert all(column in verizon_data.columns for column in expected_columns), "Missing columns in DataFrame"
    assert all(column in facebook_data.columns for column in expected_columns), "Missing columns in DataFrame"
    assert all(column in atnt_data.columns for column in expected_columns), "Missing columns in DataFrame"

def test_df_index():
    assert isinstance(apple_data.index, pd.DatetimeIndex), "Index is not a DateTimeIndex"
    assert isinstance(google_data.index, pd.DatetimeIndex), "Index is not a DateTimeIndex"
    assert isinstance(microsoft_data.index, pd.DatetimeIndex), "Index is not a DateTimeIndex"
    assert isinstance(jpmc_data.index, pd.DatetimeIndex), "Index is not a DateTimeIndex"
    assert isinstance(wfc_data.index, pd.DatetimeIndex), "Index is not a DateTimeIndex"
    assert isinstance(jnj_data.index, pd.DatetimeIndex), "Index is not a DateTimeIndex"
    assert isinstance(pfizer_data.index, pd.DatetimeIndex), "Index is not a DateTimeIndex"
    assert isinstance(merk_data.index, pd.DatetimeIndex), "Index is not a DateTimeIndex"
    assert isinstance(exxon_data.index, pd.DatetimeIndex), "Index is not a DateTimeIndex"
    assert isinstance(chevron_data.index, pd.DatetimeIndex), "Index is not a DateTimeIndex"
    assert isinstance(conocoPhillips_data.index, pd.DatetimeIndex), "Index is not a DateTimeIndex"
    assert isinstance(verizon_data.index, pd.DatetimeIndex), "Index is not a DateTimeIndex"
    assert isinstance(facebook_data.index, pd.DatetimeIndex), "Index is not a DateTimeIndex"
    assert isinstance(atnt_data.index, pd.DatetimeIndex), "Index is not a DateTimeIndex"
