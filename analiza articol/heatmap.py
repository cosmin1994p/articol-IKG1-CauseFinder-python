import pandas as pd


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


data = pd.read_excel("/Users/cosmin/Desktop/projects/script cause finder articol vasile/analiza articol/heatmap.xlsx")
print(data.dtypes)

countries_HPC = ['CI', 'CZ', 'EE', 'HU', 'PL', 'SI']
countries_LPC = ['BG', 'HR', 'LT', 'LV', 'RO', 'SK']


def create_university_heatmap(df):
   
    correlation_matrix = df.pivot(index='Univ(i)', columns='Univ(j)', values='Corr2')
    
    # Create a figure with appropriate size
    plt.figure(figsize=(15, 12))
    
    # Create heatmap
    sns.heatmap(correlation_matrix, 
                cmap='viridis',  # Red-Blue diverging colormap
                center=0,       # Center the colormap at 0
                vmin=-1,       # Minimum correlation value
                vmax=1,        # Maximum correlation value
                square=True,   # Make cells square
                annot=False,   # Don't show numbers in cells (too many cells)
                cbar_kws={'label': 'Correlation'})
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    
    # Add title
    plt.title('University Correlations Heatmap', pad=20)
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    return plt.gcf()


create_university_heatmap(data)
plt.show()