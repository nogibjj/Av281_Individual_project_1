"""
Test goes here

"""

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
import matplotlib.pyplot as plt


def test_PDdescribe():
    """Function calling PDdescribe"""
    # Call the function to be tested
    result = PDdescribe("nba.csv")
    assert result.shape == (8, 4), "Descriptive statistics do not match expected size"

# Sample DataFrame for testing
data = {
    'Age': [25, 30, 35, 40, 45, 30],
    'Salary': [50000, 60000, 75000, 80000, 90000, 60000],
    'Education': ['Bachelor', 'Master', 'Bachelor', 'PhD', 'Master', 'Master']
}
df = pd.DataFrame(data)

def test_unique_values():
    # Test the unique_values function
    unique_education = eaf.unique_values(df, 'Education')
    expected_result = ['Bachelor', 'Master', 'PhD']
    assert sorted(unique_education) == sorted(expected_result), "Unique values do not match expected values"

def test_value_counts():
    # Test the value_counts function
    value_counts_education = eaf.value_counts(df, 'Education')
    expected_result = {'Bachelor': 2, 'Master': 3, 'PhD': 1}
    assert value_counts_education.to_dict() == expected_result, "Value counts do not match expected values"

test_PDdescribe()
test_unique_values()
test_value_counts()

# run data visualization code
test_data = pd.read_csv("nba.csv")

plot_countplot(testing_data, "Position")
plot_histogram(testing_data, "Weight")
plot_boxplot(testing_data, "Age")

#test correlation heatmap
data = {
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 75000, 80000, 90000],
    'Experience': [2, 5, 8, 10, 12]
}
df = pd.DataFrame(data)

# Let's add a highly correlated column for demonstration purposes
df['Bonus'] = df['Salary'] * 0.1  # Assume Bonus is 10% of Salary

# Plot the correlation matrix heatmap
plot_correlation_heatmap(df)
