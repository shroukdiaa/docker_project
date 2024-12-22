# test_data.py
import pandas as pd
import numpy as np

# Create sample data
data = {
    'Date': pd.date_range(start='2024-01-01', periods=100),
    'Temperature': np.random.normal(0, 10, 100),
    'Precipitation': np.random.exponential(5, 100)
}

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('winter_data.csv', index=False)