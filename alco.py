import pandas as pd

df_age = pd.read_csv("modified_cardio_base.csv")  
df_alcohol = pd.read_csv("cardio_alco.csv", sep=';')  
above_50_df = df_age[df_age['age_in_years'] > 50]

total_above_50 = len(above_50_df)

alcohol_consumers_above_50 = df_alcohol[df_alcohol['id'].isin(above_50_df['id'])]['alco'].sum()

percentage_alcohol_consumers_above_50 = (alcohol_consumers_above_50 / total_above_50) * 100

print(f"Percentage of people above 50 who consume alcohol: {percentage_alcohol_consumers_above_50:.2f}%")
