import pandas as pd

df = pd.read_csv("cardio_base.csv")

mean_height = df['height'].mean()
std_height = df['height'].std()

upper_bound = mean_height + 2 * std_height
lower_bound = mean_height - 2 * std_height

count_outside_range = ((df['height'] > upper_bound) | (df['height'] < lower_bound)).sum()

percentage_outside_range = (count_outside_range / len(df)) * 100

print(f"Percentage of people who are 2 standard deviations away from the average height: {percentage_outside_range:.2f}%")
