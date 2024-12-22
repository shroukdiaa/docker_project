import pandas as pd

# Example of reading data
data = pd.read_csv('winter_data.csv')

# Basic descriptive statistics
print(data.describe())

# Check for missing values
print(data.isnull().sum())

# Plot data distributions
import seaborn as sns
sns.histplot(data['Temperature'])  

# Handle missing values
data = data.fillna(data.mean())

# Remove outliers
from scipy import stats
z_scores = stats.zscore(data)
data_clean = data[(z_scores < 3).all(axis=1)]