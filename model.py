import pandas as pd
from sklearn.cluster import KMeans

def cluster_data(file_path):
    df = pd.read_csv(file_path)
    
    # Select numeric columns for clustering
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    
    # Apply K-means
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(numeric_df)
    
    # Count records in each cluster
    cluster_counts = pd.Series(clusters).value_counts().sort_index()
    
    # Save results
    with open('k.txt', 'w') as f:
        f.write(f"Records in each cluster:\n{cluster_counts.to_string()}")

if __name__ == "__main__":
    cluster_data('res_dpre.csv')