import pandas as pd
from prophet import Prophet
df = pd.read_csv("GlobalLandTemperaturesByMajorCity.csv")
df = df.rename(columns={"dt":"ds","AverageTemperature":"y"})
df = df[df['City'] == "New York"]
df = df[df.y.notnull()]
print(df)
