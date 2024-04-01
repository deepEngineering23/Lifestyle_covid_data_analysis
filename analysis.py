import pandas as pd

df = pd.read_csv("modified_cardio_base.csv")

#df['age_in_years'] = (df['age'] / 365).astype(int)

smokers_count = df.groupby('gender')['smoke'].sum()

print(smokers_count)

top_1_percent_height = df['height'].quantile(0.99)

print("Height of the top 1% of people:", top_1_percent_height)

#df.to_csv("modified_cardio_base.csv", index=False)
