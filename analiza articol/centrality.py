import pandas as pd


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel("/Users/cosmin/Desktop/projects/script cause finder articol vasile/analiza articol/gini.xlsx")
print(data.dtypes)

countries_HPC = ['CI', 'CZ', 'EE', 'HU', 'PL', 'SI']
countries_LPC = ['BG', 'HR', 'LT', 'LV', 'RO', 'SK']


HPC_df = data[data['Country'].isin(countries_HPC)]
LPC_df = data[data['Country'].isin(countries_LPC)]

print(HPC_df)

# formated_data = data['average']

# def plot_university_scatter(df):
    
#     # Create the scatter plot
#     plt.figure(figsize=(12, 8))
    
#     # Create scatter plot with sizes proportional to CD
#     scatter = plt.scatter(df['Funding'], 
#                          df['No Projects'],
#                          s=df['CD']*100,  # Multiply CD by 100 to make dots more visible
#                          alpha=0.6)
    
#     # Add labels for each point
#     for idx, row in df.iterrows():
#         plt.annotate(row['University Name'], 
#                     (row['Funding'], row['No Projects']),
#                     xytext=(5, 5),  
#                     textcoords='offset points',
#                     fontsize=8,
#                     alpha=0.8)
    
#     # Customize the plot
#     plt.xlabel('Funding')
#     plt.ylabel('Number of Projects')
#     plt.title('University Projects vs Funding\n(Dot size represents CD value)')
    
#     # Format x-axis labels to show funding in millions/thousands
#     current_values = plt.gca().get_xticks()
#     plt.gca().set_xticklabels([f'${x:,.0f}' for x in current_values])
    
#     # Add grid for better readability
#     plt.grid(True, alpha=0.3)
    
#     # Adjust layout to prevent label cutoff
#     plt.tight_layout()
    
#     return plt

# plot = plot_university_scatter(data)
# plt.show()



###########################################
#data

data['Number'] = range(1, len(data) + 1)
# Create the scatter plot
plt.figure(figsize=(15, 10))

# Create scatter plot with sizes proportional to Centrality Degree
scatter = plt.scatter(data['Funding'], 
                     data['No Projects'],
                     s=data['Degrees']/30,  # Adjust size scaling
                     alpha=0.6,
                     c=data['Degrees'],
                     cmap='viridis')  # Add some transparency

# Add labels for each point
for idx, row in data.iterrows():
    plt.annotate(str(row['Number']), 
                (row['Funding'], row['No Projects']),
                 ha='center', 
                va='center',
                color="black",
                fontsize=14,
                alpha=0.7)

# Customize the plot
plt.xlabel('Total Funds Received (€)', fontsize=12)
plt.ylabel('Number of Projects', fontsize=12)
plt.title('LPC universities with HPC\nSize of dots represents Degree of Centrality', 
          fontsize=14, pad=20)

# Format x-axis labels to show funding in millions
plt.gca().get_xaxis().set_major_formatter(
    plt.FuncFormatter(lambda x, p: f'€{x/1e6:.1f}M'))

# Add grid for better readability
plt.grid(True, alpha=0.3)

# Adjust layout to prevent label cutoff
plt.tight_layout()

plt.show()


import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 1]

plt.plot(x, y)

# Annotate with different textcoords
plt.annotate('Data Coordinates', xy=(2, 4), xytext=(2.5, 4.5), textcoords='data')
plt.annotate('Axes Fraction', xy=(2, 4), xytext=(0.8, 0.9), textcoords='axes fraction')
plt.annotate('Offset Points', xy=(2, 4), xytext=(10, 10), textcoords='offset points')

plt.show()