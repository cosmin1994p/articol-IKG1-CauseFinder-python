import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def create_university_heatmap(df, figsize=(15, 12), title='University Correlations Heatmap'):
    """
    Create a correlation heatmap for university data with universities sorted by Contribution Horizon.
    """
    # Create correlation matrix
    correlation_matrix = df.pivot(index='Univ(i)', 
                                columns='Univ(j)', 
                                values='Corr2')
    
    # Calculate average Contribution Horizon for each university
    funding_i = df.groupby('Univ(i)')['Contribution Horizon'].mean()
    funding_j = df.groupby('Univ(j)')['Contribution Horizon'].mean()
    
    # Combine the funding values (some universities might only appear in i or j)
    funding = pd.concat([funding_i, funding_j]).groupby(level=0).mean()
    
    # Sort universities based on funding
    sorted_unis = funding.sort_values(ascending=True).index
    
    # Reorder correlation matrix
    correlation_matrix = correlation_matrix.reindex(index=sorted_unis)
    correlation_matrix = correlation_matrix.reindex(columns=sorted_unis)
    
    # Create figure
    plt.figure(figsize=figsize)
    
    # Create heatmap
    sns.heatmap(correlation_matrix, 
                cmap='viridis',
                center=0,
                vmin=-1,
                vmax=1,
                square=True,
                annot=False,
                cbar_kws={'label': 'Correlation'})
    
    # Customize labels
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    
    # Add title
    plt.title(title, pad=20)
    
    # Adjust layout
    plt.tight_layout()
    
    return plt.gcf()

# Usage
data = pd.read_excel("/Users/cosmin/Desktop/projects/script cause finder articol vasile/analiza articol/heatmap.xlsx")
fig = create_university_heatmap(data)
plt.show()





# Read Excel

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Read Excel
df = pd.read_excel("/Users/cosmin/Desktop/projects/script cause finder articol vasile/analiza articol/heatmap.xlsx")

# Sum funding for Univ(i) only, since it represents the source university
funding_per_univ = df.groupby('Univ(i)')['Contribution Horizon'].sum()
ordered_univs = funding_per_univ.sort_values(ascending=True).index
funding_order = df.groupby('Univ(i)')['Contribution Horizon'].sum().sort_values(ascending=True).index


# Create pivot table
pivot_table = pd.pivot_table(df, values='Corr2', 
                           index='Univ(i)', 
                           columns='Univ(j)',
                           fill_value=0)

# # Only reorder based on Univ(i) funding
# pivot_table = pivot_table.reindex(index=ordered_univs)
# pivot_table = pivot_table.reindex(index=funding_order, columns=funding_order)
pivot_table = pivot_table.reindex(index=funding_order, columns=funding_order)


plt.figure(figsize=(20, 15))  # Increased figure size
sns.heatmap(pivot_table, 
            cmap='viridis',
            annot=False,
            fmt='.1f',
            center=0,
            vmin=-1,
            vmax=1,
            annot_kws={'size': 6},
            square=True)

plt.xticks(rotation=90)  # Vertical text for better readability
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
