
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the figure DPI when creating the figure
plt.figure(figsize=(8, 6), dpi=300)  # 300 DPI is typically good for publication quality

# You can also set the global DPI for all figures
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300

# Read and process data
df = pd.read_excel("/Users/cosmin/Desktop/projects/script cause finder articol vasile/analiza articol/gini.xlsx")

countries_HPC = ['CI', 'CZ', 'EE', 'HU', 'PL', 'SI']
countries_LPC = ['BG', 'HR', 'LT', 'LV', 'RO', 'SK']


HPC_df = df[df['Country'].isin(countries_HPC)]
LPC_df = df[df['Country'].isin(countries_LPC)]


columns_to_correlate = ['Funding', 'No Projects', 'Degrees']
correlation_matrix = LPC_df[columns_to_correlate].corr()


print(HPC_df)

# Create heatmap
sns.heatmap(correlation_matrix, 
            annot=True,
            cmap='viridis',
            vmin=-1, vmax=1,
            center=0,
            fmt='.2f')

plt.title('Correlation Matrix')
plt.tight_layout()

# # When saving, you can also specify the DPI
# plt.savefig('correlation_matrix_high_res.png', 
#             dpi=400,
#             bbox_inches='tight',
#             format='png')

# # Or save in vector format (PDF or SVG) for infinite resolution
# plt.savefig('correlation_matrix_vector.pdf',
#             bbox_inches='tight',
#             format='pdf')

# plt.savefig('correlation_matrix_vector.svg',
#             bbox_inches='tight',
#             format='svg')

plt.show()