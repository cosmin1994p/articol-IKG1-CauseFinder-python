import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_excel("/Users/cosmin/Desktop/projects/script cause finder articol vasile/analiza articol/gini.xlsx")
print(data.dtypes)

countries_HPC = ['CI', 'CZ', 'EE', 'HU', 'PL', 'SI']
countries_LPC = ['BG', 'HR', 'LT', 'LV', 'RO', 'SK']


HPC_df = data[data['Country'].isin(countries_HPC)]
LPC_df = data[data['Country'].isin(countries_LPC)]

print(HPC_df)

# trebuie rulat o data pt fiecare categorie. Once for HPC, then LPC, and all
formated_data = LPC_df['Funding']

def calculate_gini_and_lorenz(data):
    """
    Calculate Gini coefficient and Lorenz curve data points
    
    Args:
        data: array-like, input values (e.g., funding amounts)
    
    Returns:
        float: Gini coefficient
        tuple: (cumulative population %, cumulative funding %)
    """
    # Sort data in ascending order
    sorted_data = np.sort(data)
    n = len(sorted_data)
    
    # Calculate cumulative population percentages
    cum_pop_pcts = np.arange(1, n + 1) / n * 100
    
    # Calculate cumulative funding
    cum_funding = np.cumsum(sorted_data)
    cum_funding_pcts = (cum_funding / cum_funding[-1]) * 100
    
    # Calculate Gini coefficient
    # A = Area between line of perfect equality and Lorenz curve
    # B = Area under line of perfect equality (always 0.5)
    lorenz_area = np.trapz(cum_funding_pcts, cum_pop_pcts) / 10000
    gini = 1 - 2 * lorenz_area
    
    return gini, (cum_pop_pcts, cum_funding_pcts)

def plot_lorenz_curve(cum_pop_pcts, cum_funding_pcts, gini):
    """
    Create Lorenz curve plot with viridis color scheme
    """
    plt.figure(figsize=(10, 10))
    
    # Get colors from viridis
    colors = plt.cm.viridis([0.2, 0.8])  # Get two distinct colors from viridis
    
    # Plot line of perfect equality with first viridis color
    plt.plot([0, 100], [0, 100], '--', color=colors[0], 
             label='Line of Perfect Equality', linewidth=2)
    
    # Plot Lorenz curve with second viridis color
    plt.plot([0] + list(cum_pop_pcts), [0] + list(cum_funding_pcts), 
             '-', color=colors[1], label='Lorenz Curve', linewidth=2)
    
    # Add labels and title
    plt.xlabel('Cumulative % of Universities')
    plt.ylabel('Cumulative % of Funding')
    plt.title(f'Lorenz Curve\nGini Coefficient: {gini:.4f}')
    
    # Add grid and legend
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Set axis limits and aspect ratio
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    
    return plt


# Calculate Gini coefficient and get Lorenz curve data
gini_coef, (cum_pop, cum_fund) = calculate_gini_and_lorenz(formated_data)

# Create and display the plot
plot = plot_lorenz_curve(cum_pop, cum_fund, gini_coef)

# Print detailed statistics
print(f"Gini Coefficient: {gini_coef:.4f}")
print("\nDetailed Statistics:")
print(f"Number of universities: {len(data)}")
print(f"Total funding: ${formated_data.sum():,.2f}")
print(f"Mean funding: ${formated_data.mean():,.2f}")
print(f"Median funding: ${np.median(formated_data):,.2f}")
plot.show()


###### HPC vs LPC 
#  HPC 
# Cyprus
# Czech
# Estonia
# Hungary
# Poland
# Slovenia

# LPC
# Bugaria
# Croatia
# Lithuania
# Latvia
# Romania
# Slovakia

