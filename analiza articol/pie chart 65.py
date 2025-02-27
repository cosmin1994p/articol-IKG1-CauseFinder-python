import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# # # Load the dataset
# # data = pd.read_csv("/Users/cosmin/Desktop/projects/script cause finder articol vasile/analiza articol/data_base_ikg.csv")




# # # Get the first 65 rows (including all columns)
# # df_first_65 = data.head(64) 

# # # Display the result
# # print(df_first_65)

import pandas as pd
import plotly.express as px

# # Read your data (assuming it's in a DataFrame)
# df = pd.DataFrame({
#     'Univ (i)': ['UNIVERSITY OF CYPRUS'] * 64,  # Your data
#     'Country': ['EE', 'SI', 'CZ', 'CZ', 'CZ', 'EE', 'PL', 'CZ', 'RO', 'HU', 'HU', 'CY', 'BG', 'PL', 'LV', 'PL', 'SK', 'PL', 'HU', 'LT', 'CZ', 'HR', 'SK', 'SK', 'LT', 'PL', 'CZ', 'SI', 'RO', 'LT', 'LV', 'HU', 'PL', 'PL', 'LT', 'PL', 'HU', 'PL', 'HU', 'HU', 'PL', 'PL', 'RO', 'PL', 'RO', 'PL', 'PL', 'BG', 'PL', 'HR', 'PL', 'PL', 'PL', 'PL', 'RO', 'RO', 'RO', 'RO', 'RO', 'RO', 'HR', 'HR', 'SK', 'SK'],  # Your data
#     'Contribution_Horizon': [52444253.64, 48273117.5, 42184054.1, 33702351.18, 32924004.68, 30065589.57, 28918622.74, 27386453.32, 21262969.32, 20575367.03, 19329058.92, 19267425.71, 19079908.91, 16553204.24, 9299962.74, 13923689.97, 12689962.5, 11901816.01, 11078888.54, 10065665.09, 9844313.6, 9400475.63, 8495864.6, 8072537.81, 8047928.93, 7997194.85, 7476542.92, 6926672.29, 6678885.07, 2243583.75, 6280618.51, 5575205.96, 5388254.48, 4476852.14, 1953341.4, 4455062.99, 4436448.26, 4394292.98, 3928536.47, 3240164.06, 3671677.64, 3463222.01, 3451021.61, 3139200, 3429908.06, 2737620.35, 2612464.44, 3323848.36, 2323038.57, 13961302.95, 2215533.75, 2169549.13, 2037715.48, 1912047.45, 2973457.64, 1577328.75, 1177769.69, 1120190.63, 1030937.5, 966062.58, 3030046.45, 1908024.95, 2964780.5, 1838822.09]  # Your data
# })

# # Group by country and sum contributions
# country_funding = df.groupby('Country')['Contribution_Horizon'].sum().reset_index()
# country_funding['Percentage'] = (country_funding['Contribution_Horizon'] / country_funding['Contribution_Horizon'].sum() * 100).round(1)

# # Sort by contribution amount
# country_funding = country_funding.sort_values('Contribution_Horizon', ascending=False)

# # Create pie chart
# fig = px.pie(country_funding, 
#              color_discrete_sequence=px.colors.sequential.Viridis,
#              values='Contribution_Horizon',
#              names='Country',
#              title='Funding Distribution by Country (%)',
#              hover_data=['Percentage'])
# fig.update_traces(textfont_size=30)
# fig.show()
# print("\nFunding Distribution by Country:")
# print(country_funding.to_string(index=False))




df = pd.DataFrame({
    'Country': ['EE', 'SI', 'CZ', 'CZ', 'CZ', 'EE', 'PL', 'CZ', 'RO', 'HU', 'HU', 'CY', 'BG', 'PL', 'LV', 'PL', 'SK', 'PL', 'HU', 'LT', 'CZ', 'HR', 'SK', 'SK', 'LT', 'PL', 'CZ', 'SI', 'RO', 'LT', 'LV', 'HU', 'PL', 'PL', 'LT', 'PL', 'HU', 'PL', 'HU', 'HU', 'PL', 'PL', 'RO', 'PL', 'RO', 'PL', 'PL', 'BG', 'PL', 'HR', 'PL', 'PL', 'PL', 'PL', 'RO', 'RO', 'RO', 'RO', 'RO', 'RO', 'HR', 'HR', 'SK', 'SK'],
    'Contribution_Horizon': [52444253.64, 48273117.5, 42184054.1, 33702351.18, 32924004.68, 30065589.57, 28918622.74, 27386453.32, 21262969.32, 20575367.03, 19329058.92, 19267425.71, 19079908.91, 16553204.24, 9299962.74, 13923689.97, 12689962.5, 11901816.01, 11078888.54, 10065665.09, 9844313.6, 9400475.63, 8495864.6, 8072537.81, 8047928.93, 7997194.85, 7476542.92, 6926672.29, 6678885.07, 2243583.75, 6280618.51, 5575205.96, 5388254.48, 4476852.14, 1953341.4, 4455062.99, 4436448.26, 4394292.98, 3928536.47, 3240164.06, 3671677.64, 3463222.01, 3451021.61, 3139200, 3429908.06, 2737620.35, 2612464.44, 3323848.36, 2323038.57, 13961302.95, 2215533.75, 2169549.13, 2037715.48, 1912047.45, 2973457.64, 1577328.75, 1177769.69, 1120190.63, 1030937.5, 966062.58, 3030046.45, 1908024.95, 2964780.5, 1838822.09]
})

# Define country groups
hpc = ['CY', 'CZ', 'EE', 'SI', 'HU', 'PL']
lpc = ['LV', 'SK', 'BG', 'RO', 'HR', 'LT']

# Create group labels
df['Group'] = df['Country'].apply(lambda x: 'HPC' if x in lpc else 'LPC')

# Calculate group totals
group_funding = df.groupby('Group')['Contribution_Horizon'].sum().reset_index()
group_funding['Percentage'] = (group_funding['Contribution_Horizon'] / group_funding['Contribution_Horizon'].sum() * 100).round(1)

# Create pie chart
fig = px.pie(group_funding, 
             color_discrete_sequence=['#26828E','#FDE725'],
             values='Contribution_Horizon',
             names='Group',
             title='Funding Distribution: HPC vs LPC Countries (%)',
             hover_data=['Percentage'])
fig.update_traces(textfont_size=30)

fig.show()
print("\nFunding Distribution by Group:")
print(group_funding.to_string(index=False))


