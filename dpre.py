import numpy as np
import pandas as pd

def process_data(file_path):
    df = pd.read_csv(file_path)
    
    # Data Cleaning
    df = df.dropna()  # Remove missing values
    df = df.drop_duplicates()  # Remove duplicates
    
    # Data Transformation
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = (df[numeric_cols] - df[numeric_cols].mean()) / df[numeric_cols].std()  # Standardization
    
    # Data Reduction
    df = df.select_dtypes(include=['float64', 'int64']).head(1000)  # Sample first 1000 numeric records
    
    # Data Discretization
    for col in numeric_cols:
        try:
            df[f'{col}_binned'] = pd.qcut(df[col], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'], duplicates='drop')
        except ValueError as e:
            print(f"Error binning column {col}: {e}")
    
    # Save results
    df.to_csv('res_dpre.csv', index=False)
    
    # Call next script
    import eda
    eda.analyze_data('res_dpre.csv')

if __name__ == "__main__":
    process_data(r'initial_df.csv')