# ds_Agridata_explorer

import pandas as pd

# Load raw agriculture data CSV
df = pd.read_csv('data/raw_data.csv')

# Data cleaning steps
df.drop_duplicates(inplace=True)
df.fillna(method='ffill', inplace=True)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Save cleaned data to new CSV
df.to_csv('data/cleaned_data.csv', index=False)

print("Data cleaning complete. Cleaned data saved to 'data/cleaned_data.csv'.")


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv('data/cleaned_data.csv')

# Example: Top 5 crops by average yield
top_crops = df.groupby('crop')['yield'].mean().sort_values(ascending=False).head(5)

print("Top 5 crops by average yield:")
print(top_crops)

# Plotting yield of top 5 crops
plt.figure(figsize=(10,6))
sns.barplot(x=top_crops.index, y=top_crops.values, palette='viridis')
plt.title('Top 5 Crops by Average Yield')
plt.ylabel('Average Yield')
plt.xlabel('Crop')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


-- 1. Total crop production by year
SELECT year, SUM(production) AS total_production
FROM crop_data
GROUP BY year
ORDER BY year;

-- 2. Average yield by crop
SELECT crop, AVG(yield) AS avg_yield
FROM crop_data
GROUP BY crop
ORDER BY avg_yield DESC;

-- 3. Top 5 states by total production
SELECT state, SUM(production) AS total_production
FROM crop_data
GROUP BY state
ORDER BY total_production DESC
LIMIT 5;

-- 4. Correlation analysis example: Rainfall vs Yield (assumes rainfall column)
SELECT rainfall, yield
FROM crop_data
WHERE rainfall IS NOT NULL AND yield IS NOT NULL;
