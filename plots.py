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

def plot_histograms(df: pd.DataFrame) -> None:
    """
    Plots histograms for each column in the given DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame containing data to plot histograms for.

    This function creates a grid of subplots with histograms of each column in the DataFrame.
    The number of rows and columns in the grid is dynamically calculated based on the number
    of columns in the DataFrame, ensuring no empty subplots are created.
    """
    colors_for_histograms = generate_colors(len(df.columns))
    num_columns = len(df.columns)
    num_rows = (num_columns + 2) // 3  # Calculate the number of rows needed

    # Create only the necessary subplots with dynamic grid size
    fig, axes = plt.subplots(num_rows, min(3, num_columns), figsize=(10, 10))
    axes = axes.flatten()

    # Plot histograms for each column
    for i, column in enumerate(df.columns):
        axes[i].hist(df[column], color=colors_for_histograms[i], bins=20)
        axes[i].set_xlabel(column)
        axes[i].set_ylabel('Frequency')
        axes[i].set_title(f'Histogram of {column}')

    # Hide any extra subplots
    for j in range(num_columns, len(axes)):
        fig.delaxes(axes[j])

    # Adjust layout for better spacing
    plt.tight_layout()
    plt.show()
