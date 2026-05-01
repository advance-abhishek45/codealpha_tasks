import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("unemployment.csv")

# Show first rows
print(df.head())

# Column names clean कर
df.columns = df.columns.str.strip()

# Date convert कर
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Null values remove कर
df = df.dropna()

# -------- GRAPH 1 --------
plt.figure(figsize=(10,5))
sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', data=df)
plt.title("Unemployment Rate Over Time")
plt.xticks(rotation=45)
plt.show()

# -------- GRAPH 2 --------
plt.figure(figsize=(10,5))
sns.barplot(x='Region', y='Estimated Unemployment Rate (%)', data=df)
plt.title("State-wise Unemployment")
plt.xticks(rotation=90)
plt.show()

# -------- GRAPH 3 --------
covid_data = df[df['Date'].dt.year == 2020]

plt.figure(figsize=(10,5))
sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', data=covid_data)
plt.title("Covid Impact (2020)")
plt.xticks(rotation=45)
plt.show()