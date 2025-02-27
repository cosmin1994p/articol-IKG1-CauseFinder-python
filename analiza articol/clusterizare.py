import pandas as pd 
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/cosmin/Desktop/projects/script cause finder articol vasile/analiza articol/data_base_ikg.csv")

describe= df.describe()

print(df.head())

print(df.columns)

import networkx as nx

# Create graph with multiple edge attributes
G = nx.from_pandas_edgelist(
    df,
    source="Univ (i)",
    target="Univ(j)",
    edge_attr=["Papers", "Distance (ij)", "No Projects"],
    create_using=nx.Graph()  # Use nx.DiGraph() for directed networks
)

print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")

density = nx.density(G)
print(f"Graph Density: {density}")


degree_centrality = nx.degree_centrality(G)
print(degree_centrality)

betweenness_centrality = nx.betweenness_centrality(G)
print(betweenness_centrality)

# for u, v in G.edges():
#     print(type(G[u][v]['Y(ij) - joint']))
#     print(G[u][v]['Y(ij) - joint'])

for u, v in G.edges():
    print(G[u][v]['Papers'])
    G[u][v]['Papers'] = int(G[u][v]['Papers']) 

import matplotlib.pyplot as plt

# Define node size and edge width based on attributes
node_size = [100 * G.degree(node) for node in G.nodes()]  # Scale by degree
node_color = [G.degree(node) for node in G.nodes()] 
      
edge_width = [G[u][v]['Papers'] / 10 for u, v in G.edges()]  # Scale Papers for width

pos = nx.spring_layout(G, seed=42)  # Reproducible layout

plt.figure(figsize=(12, 8))
nx.draw(
    G,
    pos=pos,
    with_labels=True,
    node_size=node_size,
    width=edge_width,
    font_size=8,
    edge_color='blue',
    labels={node: node for node in G.nodes()},
)
plt.title("University Collaboration Network")

plt.show()




# Create a network graph of university collaborations
G = nx.from_pandas_edgelist(df, 'Univ (i)', 'Univ(j)', ['Papers', 'Distance (ij)', 'No Projects'])

# Analyze network characteristics
print("Network Metrics:")
print(f"Total Nodes: {G.number_of_nodes()}")
print(f"Total Edges: {G.number_of_edges()}")
print(f"Average Clustering Coefficient: {nx.average_clustering(G)}")

import folium
from folium.plugins import MarkerCluster

# Create a map highlighting universities
# m = folium.Map(location=[50, 10], zoom_start=4)
# marker_cluster = MarkerCluster().add_to(m)

# # Add markers for each university's location
# for _, row in df.iterrows():
#     folium.Marker(
#         location=[row['geolocation'].split(',')[0], row['geolocation'].split(',')[1]],
#         popup=row['Univ (i)']
#     ).add_to(marker_cluster)

# m.save('university_map2.html')

from sklearn.cluster import DBSCAN
import numpy as np

# Extract coordinates
coordinates = df['geolocation'].apply(lambda x: [float(coord) for coord in x.split(',')])
X = np.array(coordinates.tolist())

# Perform spatial clustering
clustering = DBSCAN(eps=2, min_samples=3).fit(X)
df['Cluster'] = clustering.labels_

# Analyze clusters
cluster_summary = df.groupby('Cluster').agg({
    'Univ(j)': 'count',
    'Papers': 'sum',
    'Country': lambda x: x.value_counts().index[0]
})
print(cluster_summary)