"""
Test goes here

"""

from lib import (
    PDdescribe,
    unique_values,
    value_counts,
)
import pandas as pd
import numpy as np


def test_PDdescribe():
    """Function calling PDdescribe"""
    # Call the function to be tested
    result = PDdescribe("nba.csv")
    assert result.shape == (8, 4), "Descriptive statistics do not match expected size"


def test_unique_values():
    # Test the unique_values function
    data = {
        "Age": [25, 30, 35, 40, 45, 30],
        "Salary": [50000, 60000, 75000, 80000, 90000, 60000],
        "Education": ["Bachelor", "Master", "Bachelor", "PhD", "Master", "Master"],
    }
    df = pd.DataFrame(data)
    unique_education = unique_values(df, "Education")
    assert (
        unique_education == np.array(["Bachelor", "Master", "PhD"])
    ).all(), "Unique values do not match expected values"


def test_value_counts():
    # Test the value_counts function
    data = {
        "Age": [25, 30, 35, 40, 45, 30],
        "Salary": [50000, 60000, 75000, 80000, 90000, 60000],
        "Education": ["Bachelor", "Master", "Bachelor", "PhD", "Master", "Master"],
    }
    df = pd.DataFrame(data)
    value_counts_education = value_counts(df, "Education")
    assert (
        value_counts_education["Master"] == 3
    ), "Value counts do not match expected values"


test_PDdescribe()
test_unique_values()
test_value_counts()
