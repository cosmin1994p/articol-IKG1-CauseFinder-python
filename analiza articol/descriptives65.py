import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("/Users/cosmin/Desktop/projects/script cause finder articol vasile/analiza articol/data_base_ikg.csv")




# Get the first 65 rows (including all columns)
df_first_65 = data.head(64) 

# Display the result
print(df_first_65)

summary = df_first_65.describe()
summary.to_excel("describe.xlsx")