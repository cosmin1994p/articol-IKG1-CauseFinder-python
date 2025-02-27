import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("/Users/cosmin/Desktop/projects/script cause finder articol vasile/analiza articol/data_base_ikg.csv")

# Clean and preprocess
data['Distance (ij)'] = data['Distance (ij)'].str.replace(',', '').astype(float)
data['Papers'] = data['Papers'].astype(int)

# Create a graph
G = nx.Graph()

# Add nodes
for index, row in data.iterrows():
    G.add_node(row['Univ (i)'], country=row['Country'], city=row['City'])
    G.add_node(row['Univ(j)'], country=row['Country'], city=row['City'])

    # Add edge if there's collaboration
    if row['Papers'] > 0:
        G.add_edge(row['Univ (i)'], row['Univ(j)'], weight=row['Papers'])

# Visualize the graph
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G, seed=42)  # Layout for positioning nodes
nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_weight="bold")
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
plt.title("University Collaboration Network")
plt.show()



# from pyvis.network import Network
# import pandas as pd
# import networkx as nx

# # Load the dataset
# data = pd.read_csv("/Users/cosmin/Desktop/projects/script cause finder articol vasile/analiza articol/data_base_ikg.csv")


# # Clean and preprocess
# data['Distance (ij)'] = data['Distance (ij)'].str.replace(',', '').astype(float)
# data['Papers'] = data['Papers'].astype(int)

# # Create a NetworkX graph
# G = nx.Graph()

# # Add nodes and edges
# for index, row in data.iterrows():
#     # Add nodes for universities
#     G.add_node(row['Univ (i)'], country=row['Country'], city=row['City'])
#     G.add_node(row['Univ(j)'], country=row['Country'], city=row['City'])

#     # Add edges with weights (if collaboration exists)
#     if row['Papers'] > 0:
#         G.add_edge(row['Univ (i)'], row['Univ(j)'], weight=row['Papers'])

# # Convert NetworkX graph to Pyvis network
# net = Network(height="800px", width="100%", notebook=True ,cdn_resources='in_line')

# # Load graph into Pyvis
# net.from_nx(G)

# # Add physics for better node spacing
# net.toggle_physics(True)

# # Save and display
# output_path = "/Users/cosmin/Desktop/projects/script cause finder articol vasile/analiza articol/data/interactive_graph.html"  # Save the interactive graph as an HTML file
# net.show(output_path)
