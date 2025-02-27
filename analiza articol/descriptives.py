import pandas as pd #For reading dataset files
import networkx as nx #For network creation/analysis
from networkx.algorithms import community
import matplotlib.pyplot as plt #For plotting graphs

def plot_degree_centrality(G, figsize=(12, 6), top_n=None):
    degree_centrality = nx.degree_centrality(G)
    df = pd.DataFrame.from_dict(degree_centrality, orient='index', 
                               columns=['Degree Centrality'])
    df.index.name = 'Node'
    df = df.sort_values('Degree Centrality', ascending=False)
    
    if top_n:
        df = df.head(top_n)
    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=figsize)
    bars = ax.bar(range(len(df)), df['Degree Centrality'])
    ax.set_title('Node Degree Centrality', pad=20, fontsize=14)
    ax.set_xlabel('Nodes', fontsize=12)
    ax.set_ylabel('Degree Centrality', fontsize=12)
    
    ax.set_xticks(range(len(df)))
    ax.set_xticklabels(df.index, rotation=45, ha='right')
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.3f}',
                ha='center', va='bottom')
    plt.tight_layout()
    return fig, ax

df = pd.read_csv("/Users/cosmin/Desktop/projects/script cause finder articol vasile/analiza articol/data_base_ikg.csv")

edges = df.groupby(['Univ (i)', 'Univ(j)', 'Country'])['Papers'].sum().reset_index()

print(edges.head())
plt.figure(figsize=(10,10))

G = nx.from_pandas_edgelist(edges, source='Univ (i)', target='Univ(j)',edge_attr=True)

# original_labels = list(G.nodes)
# simplified_labels = {node: f"U{i+1}" for i, node in enumerate(original_labels)}
# G = nx.relabel_nodes(G, simplified_labels)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)

plt.title("network graph")
plt.show()

# If you want to plot only top 10 nodes
# fig, ax = plot_degree_centrality(G, top_n=10)
# plt.show()



#Network centrality Measures
#  
#Check nodes
G.nodes()

plt.figure(figsize=(10,10))

degrees = [G.degree(n) for n in G.nodes()]
plt.hist(degrees)

plt.show()

plt.figure(figsize=(10,10))
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
plt.loglog(degree_sequence,marker='*')
plt.show()

#Degree centrality for unweighted graph    -cum dracu isi alege pe baza a ce variabila face centralitatea 
degree_centrality = nx.degree_centrality(G)
degree_centrality
print(degree_centrality)

for node in sorted(degree_centrality, key=degree_centrality.get, reverse=True):
  print(node, degree_centrality[node])