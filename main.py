from lib import (
    PDdescribe,
    unique_values,
    value_counts,
    plot_histogram,
    plot_boxplot,
    plot_correlation_heatmap,
    plot_countplot,
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

plot_countplot(testing_data, "cylinders")
plot_histogram(testing_data, "mpg")
plot_boxplot(testing_data, "mpg")

test_data = testing_data.drop("name", axis=1)
print("The correlation beetween variables is visualized below")

plot_correlation_heatmap(test_data)
