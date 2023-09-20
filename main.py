from lib import (
    PDdescribe,
    unique_values,
    value_counts,
)
import pandas as pd

testing_data = pd.read_csv("Auto.csv")
print(
    "First, the functions PDdescribe, unique_values, value_counts, plot_histogram, plot_boxplot, 
    plot_correlation_heatmap, and plot_countplot are imported from lib.py to be used in this notebook. 
    Then, the testing data from Auto.csv is read in as a pandas dataframe, with the first few rows 
    shown below."
)
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
