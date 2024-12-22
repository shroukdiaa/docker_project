import pandas as pd

def analyze_data(file_path):
    df = pd.read_csv(file_path)
    
    # Generate insights
    insights = [
        f"Dataset shape: {df.shape}",
        f"Correlation between first two numeric columns: {df.select_dtypes('number').iloc[:, 0:2].corr().iloc[0,1]}",
        f"Number of unique values in each column: {df.nunique().to_dict()}"
    ]
    
    # Save insights
    for i, insight in enumerate(insights, 1):
        with open(f'eda-in-{i}.txt', 'w') as f:
            f.write(insight)
    
    # Call next script
    import vis
    vis.create_visualization('res_dpre.csv')

if __name__ == "__main__":
    analyze_data('res_dpre.csv')