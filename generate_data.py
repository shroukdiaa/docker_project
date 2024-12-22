# save as generate_data.py
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate 10000 records
n_records = 10000

# Create simple winter data
data = {
    'Date': pd.date_range(start='2023-12-01', periods=n_records, freq='H'),
    'Temperature': np.random.normal(-5, 10, n_records).round(1),  # Temperature in Celsius
    'Snowfall': np.random.exponential(5, n_records).round(1),     # Snowfall in cm
    'Activity': np.random.choice(['Skiing', 'Snowboarding', 'Ice Skating'], n_records),
    'Visitors': np.random.randint(10, 200, n_records),
    'Rating': np.random.randint(1, 6, n_records)                  # Rating 1-5
}

# Create DataFrame
df = pd.DataFrame(data)

# Add some missing values (5%)
mask = np.random.random(n_records) < 0.05
df.loc[mask, 'Temperature'] = np.nan

# Save to CSV
df.to_csv('winter_data.csv', index=False)

# Show sample and info
print("\nFirst 5 rows of the dataset:")
print(df.head())
print("\nDataset Info:")
print(df.info())
