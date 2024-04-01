import pandas as pd

df = pd.read_csv("covid_data.csv")  
deaths_by_country = df.groupby('location')['new_deaths'].sum()

population_by_country = df.groupby('location')['population'].first()

death_rate_by_country = deaths_by_country / population_by_country

sorted_countries = death_rate_by_country.sort_values(ascending=False)

third_highest_country = sorted_countries.index[2]

print(f"The country with the third-highest death rate is: {third_highest_country}")
