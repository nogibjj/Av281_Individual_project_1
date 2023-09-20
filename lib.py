"""Importing module pandas for my function."""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Function to get descriptive statistics of a data set in csv form
def PDdescribe(filename):
    """
    function which returns descriptive stats about input data
    """
    df = pd.read_csv(filename)
    return df.describe()


def unique_values(df, column):
    """
    Display unique values in a categorical column.
    """
    return df[column].unique()


# Function to display value counts for a categorical column
def value_counts(df, column):
    """
    Display value counts for a categorical column.
    """
    return df[column].value_counts()


# Function to plot a histogram of a numeric column
def plot_histogram(df, column):
    """
    Plot a histogram of a numeric column.
    """
    plt.figure(figsize=(8, 6))
    sns.histplot(df[column], kde=True)
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()


# Function to plot a boxplot of a numeric column
def plot_boxplot(df, column):
    """
    Plot a boxplot of a numeric column.
    """
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df[column])
    plt.title(f"Boxplot of {column}")
    plt.xlabel(column)
    plt.show()


# Function to display a correlation matrix heatmap
def plot_correlation_heatmap(df):
    """
    Display a correlation matrix heatmap.
    """
    correlation_matrix = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix Heatmap")
    plt.show()


# Function to display a count plot of a categorical column
def plot_countplot(df, column):
    """
    Display a count plot of a categorical column.
    """
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x=column)
    plt.title(f"Count Plot of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.show()
