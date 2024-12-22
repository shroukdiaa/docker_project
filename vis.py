import pandas as pd
import matplotlib.pyplot as plt

def create_visualization(file_path):
    df = pd.read_csv(file_path)
    
    # Create visualization
    plt.figure(figsize=(10, 6))
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns[:2]
    plt.scatter(df[numeric_cols[0]], df[numeric_cols[1]])
    plt.xlabel(numeric_cols[0])
    plt.ylabel(numeric_cols[1])
    plt.title('Scatter Plot of First Two Numeric Columns')
    plt.savefig('vis.png')
    plt.close()
    
    # Call next script
    import model
    model.cluster_data('res_dpre.csv')

if __name__ == "__main__":
    create_visualization('res_dpre.csv')