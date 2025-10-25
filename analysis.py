# Sample script for ai-assisted-research-tools
import pandas as pd

df = pd.read_csv('data/sample_data.csv')
print(df.head())

# Replace this with analysis code. Example: basic cleaning
df = df.dropna()
df.to_csv('data/cleaned_sample_data.csv', index=False)
