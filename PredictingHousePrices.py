import pandas as pd

rawHousingData = pd.read_csv("https://raw.githubusercontent.com/wilkmzhou/vancouverHousePricePrediction/refs/heads/main/synthetic_house_prices_20_years.csv")


print(rawHousingData.head(n = 3))