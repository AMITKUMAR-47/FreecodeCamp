
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Import data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # First line of best fit (1880-present)
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred = pd.Series(range(1880, 2051))
    y_pred = res.slope * x_pred + res.intercept
    ax.plot(x_pred, y_pred, color="red")

    # Second line of best fit (2000-present)
    recent = df[df["Year"] >= 2000]
    res_recent = linregress(recent["Year"], recent["CSIRO Adjusted Sea Level"])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = res_recent.slope * x_recent + res_recent.intercept
    ax.plot(x_recent, y_recent, color="green")

    # Labels
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    fig.savefig("sea_level_plot.png")
    return fig
