import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

def perform_geospatial_clustering(df):
    coordinates = df['geolocation'].apply(lambda x: [float(coord) for coord in x.split(',')])
    X = np.array(coordinates.tolist())
    
    X_normalized = StandardScaler().fit_transform(X)
    
    # Perform spatial clustering
    # eps: maximum distance between two samples to be considered in the same neighborhood
    # min_samples: minimum number of samples in a neighborhood for a point to be considered a core point
    clustering = DBSCAN(eps=0.5, min_samples=2).fit(X_normalized)
    
    # Add cluster labels to the dataframe
    df['Cluster'] = clustering.labels_
    
    return df, X

def plot_cluster_matplotlib(df, X):
    """Create a matplotlib scatter plot of clusters"""
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(X[:, 1], X[:, 0], c=df['Cluster'], cmap='viridis', 
                          edgecolor='black', linewidth=1, alpha=0.75)
    plt.title('University Geospatial Clustering')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.colorbar(scatter, label='Cluster')
    
    # Annotate points with university names
    for i, (lon, lat) in enumerate(X):
        plt.annotate(df.loc[i, 'Univ(j)'], (lon, lat), 
                     xytext=(5, 5), textcoords='offset points', 
                     fontsize=8, alpha=0.7)
    
    plt.tight_layout()
    plt.savefig('university_clusters_matplotlib.png')
    plt.close()

def create_interactive_cluster_map(df):
    """Create an interactive folium map of clusters"""
    # Create base map centered on the mean coordinates
    center_lat = df['geolocation'].apply(lambda x: float(x.split(',')[0])).mean()
    center_lon = df['geolocation'].apply(lambda x: float(x.split(',')[1])).mean()
    
    m = folium.Map(location=[center_lat, center_lon], zoom_start=4)
    
    # Color palette for clusters
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 
              'lightred', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple']
    
    # Add markers for each university, colored by cluster
    for idx, row in df.iterrows():
        lat, lon = map(float, row['geolocation'].split(','))
        
        # Determine color (use default if cluster is -1 (noise))
        cluster_color = colors[row['Cluster'] % len(colors)] if row['Cluster'] != -1 else 'gray'
        
        folium.CircleMarker(
            location=[lat, lon],
            radius=5,
            popup=f"{row['Univ(j)']}<br>Cluster: {row['Cluster']}",
            color=cluster_color,
            fill=True,
            fillColor=cluster_color
        ).add_to(m)
    
    # Save the map
    m.save('university_clusters_map.html')

def analyze_clusters(df):
    """Analyze and print cluster characteristics"""
    # Cluster summary
    cluster_summary = df.groupby('Cluster').agg({
        'Univ(j)': 'count',
        'Papers': ['mean', 'sum'],
        'Country': lambda x: x.value_counts().index[0]
    }).reset_index()
    
    print("Cluster Summary:")
    print(cluster_summary)
    
    # Noise points (unclustered)
    noise_points = df[df['Cluster'] == -1]
    print("\nNoise Points (Unclustered Universities):")
    print(noise_points[['Univ(j)', 'Country', 'geolocation']])

# Main execution
def main():
    # Load the dataset (replace with your actual data loading method)
    df = pd.read_csv("/Users/cosmin/Desktop/projects/script cause finder articol vasile/analiza articol/data_base_ikg.csv")
    
    # Perform clustering
    clustered_df, coordinates = perform_geospatial_clustering(df)
    
    # Visualize clusters
    plot_cluster_matplotlib(clustered_df, coordinates)
    create_interactive_cluster_map(clustered_df)
    
    # Analyze clusters
    analyze_clusters(clustered_df)

if __name__ == '__main__':
    main()