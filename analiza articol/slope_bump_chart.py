import pandas as pd


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


data = pd.read_excel("/Users/cosmin/Desktop/projects/script cause finder articol vasile/analiza articol/gini.xlsx")
print(data.dtypes)

countries_HPC = ['CY', 'CZ', 'EE', 'HU', 'PL', 'SI']
countries_LPC = ['BG', 'HR', 'LT', 'LV', 'RO', 'SK']

HPC_df = data[data['Country'].isin(countries_HPC)]
LPC_df = data[data['Country'].isin(countries_LPC)]

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# # Sample data - replace with your actual data
# data = {
#     'University': ['Harvard University', 'MIT', 'Stanford University', 'Oxford University', 'Cambridge University'],
#     'Centrality': [0.85, 0.82, 0.79, 0.77, 0.75],
#     'Papers': [1200, 1100, 950, 890, 870]
# }

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# # Example data with an additional metric
# data = {
#     'University': ['Harvard University', 'MIT', 'Stanford University', 'Oxford University', 'Cambridge University'],
#     'Centrality': [0.85, 0.82, 0.79, 0.77, 0.75],
#     'Papers': [1200, 1100, 950, 890, 870],
#     'Citations': [15000, 14500, 13000, 12800, 12600]  # Example additional metric
# }

# def create_bump_chart(data, exclude_columns=['University Name'], figsize=(12, 6)):
    
#     df = pd.DataFrame(data)
    
#     # Get metrics (all columns except excluded ones)
#     metrics = [col for col in df.columns if col not in exclude_columns]
    
#     # Create rankings for each metric
#     rankings = pd.DataFrame()
#     rankings['University Name'] = df['University Name']
    
#     for metric in metrics:
#         rankings[f'{metric}_rank'] = df[metric].rank(ascending=False)
#         print(metric)
    
#     # Create the plot
#     plt.figure(figsize=figsize)
    
#     # Plot lines for each university
#     colors = plt.cm.Set3(np.linspace(0, 1, len(df)))
    
#     for idx, university in enumerate(rankings['University Name']):
#         ranks = [rankings.loc[rankings['University Name'] == university, f'{metric}_rank'].iloc[0] 
#                 for metric in metrics]
#         plt.plot(range(len(metrics)), ranks, 'o-', label=university, color=colors[idx], 
#                 linewidth=2, markersize=10)
    
#     # Customize the plot
#     plt.gca().invert_yaxis()  # Invert y-axis so rank 1 is at the top
#     plt.xticks(range(len(metrics)), metrics, fontsize=12, rotation=45 if len(metrics) > 3 else 0)
#     plt.yticks(range(1, len(df) + 1), fontsize=12)
#     plt.grid(True, linestyle='--', alpha=0.7)
#     plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
#     plt.title('University Rankings by Different Metrics', pad=20, fontsize=14)
#     plt.ylabel('Rank', fontsize=12)
    
#     # Adjust layout to prevent label cutoff
#     plt.tight_layout()
    
#     return plt

def create_bump_chart(data, exclude_columns=['University Name','Country','No of WoS Papers (total)'], figsize=(12, 6)):
    """
    Create a bump chart for university rankings with rank labels on each node.
    """
    df = pd.DataFrame(data)
    
    # Get metrics (all columns except excluded ones)
    metrics = [col for col in df.columns if col not in exclude_columns]
    
    # Create rankings for each metric
    rankings = pd.DataFrame()
    rankings['University Name'] = df['University Name']
    
    for metric in metrics:
        rankings[f'{metric}_rank'] = df[metric].rank(ascending=False)
    
    # Create the plot
    plt.figure(figsize=figsize)
    
    # Plot lines for each university
    # colors = plt.cm.Set3(np.linspace(0, 1, len(df)))
    colors = plt.cm.viridis(np.linspace(0, 1, len(df)))

    
    for idx, university in enumerate(rankings['University Name']):
        ranks = [rankings.loc[rankings['University Name'] == university, f'{metric}_rank'].iloc[0] 
                for metric in metrics]
        
        # Plot the line
        plt.plot(range(len(metrics)), ranks, '-', color=colors[idx], linewidth=2)
        
        # Plot points and add rank labels
        for metric_idx, rank in enumerate(ranks):
            plt.plot(metric_idx, rank, 'o', color=colors[idx], markersize=10)
            # Add rank label
            plt.annotate(f'{int(rank)}', 
                        (metric_idx, rank),
                        xytext=(0, 0),
                        textcoords='offset points',
                        ha='center',
                        va='center',
                        fontsize=10,
                        color='black',
                        fontweight='bold')
    
    # Customize the plot
    plt.gca().invert_yaxis()  # Invert y-axis so rank 1 is at the top
    plt.xticks(range(len(metrics)), metrics, fontsize=12)
    # plt.yticks(data['University Name'], fontsize=12)
    plt.yticks(range(1, len(df) + 1), data['University Name'], fontsize=12)

    plt.grid(True, linestyle='--', alpha=0.7)
    plt.title('University Rankings by Different Metrics', pad=20, fontsize=14)
    plt.ylabel('Rank', fontsize=12)
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    return plt
# Example usage
# You can now add as many columns as you want to the data dictionary



# chart = create_bump_chart(data)
# plt.show()
my_data = {
    'University Name': ['Univ A', 'Univ B', 'Univ C'],
    'Metric1': [100, 200, 150],
    'Metric2': [0.5, 0.8, 0.6],
    'Metric3': [1000, 2000, 1500],
    'Metric4': [50, 40, 45]
}
chart = create_bump_chart(data)
plt.show()
