import pandas as pd
import matplotlib.pyplot as plt


def PDdescribe(filename):
    """function which returns descriptive stats about input data"""
    df = pd.read_csv(filename)
    return df.describe()


results = PDdescribe("nba.csv")

print(results)

nba = pd.read_csv("nba.csv")
plt.figure(figsize=(10, 8))
plt.scatter(nba["Age"], nba["Weight"])
plt.title("NBA player Weight vs Age")
plt.xlabel("Height")
plt.ylabel("Age")
plt.show(block=True)
