from lib import (
    PDdescribe,
    unique_values,
    value_counts,
)
import pandas as pd

testing_data = pd.read_csv("Auto.csv")
print("Data from Auto.csv is read in as pandas dataframe. First few rows shown below.")
print(testing_data.head())
print("")
print("summary statistics from Auto.csv:")
print(PDdescribe("Auto.csv"))
print("")
print("unique values of cylinders column are:")
print(unique_values(testing_data, "cylinders"))
print("")
print("counts of cylinders values:")
print(value_counts(testing_data, "cylinders"))
print("")
