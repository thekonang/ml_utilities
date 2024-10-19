import random
import pandas as pd
import matplotlib.pyplot as plt

def generate_colors(n : int, seed=0) -> list:
    """
    Generates a list of n visually distinct colors with a consistent seed.

    Parameters:
    n (int): Number of colors to generate.
    seed (int): Seed for the random number generator.

    Returns:
    list: A list of hex color codes.
    """
    random.seed(seed)  # Set the seed for reproducibility
    colors = ['#%06X' % random.randint(0, 0xFFFFFF) for _ in range(n)]
    return colors

def plot_histograms(df : pd.DataFrame) -> None:
    colors_for_histograms = generate_colors(len(df) + 1 )  
    for i, column in enumerate(df):
        plt.figure()
        plt.hist(df[column], color=colors_for_histograms[i], bins=20)
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.title(f'Histogram of {column}')
        plt.show()
