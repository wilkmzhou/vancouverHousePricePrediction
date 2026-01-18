import pandas as pd

rawHousingData = pd.read_csv("https://raw.githubusercontent.com/wilkmzhou/vancouverHousePricePrediction/refs/heads/main/synthetic_house_prices_20_years.csv")

print(rawHousingData.head(n = 3))
print(len(rawHousingData))

rawHousingData["is_Renovated"] = rawHousingData["Renovation Year"].isnull().astype(int)
rawHousingData["adjusted_house_age"] = 2024 - rawHousingData[["Year Built", "Renovation Year"]].max(axis = 1)
rawHousingData["Garage Type"] = rawHousingData["Garage Type"].fillna("No Garage")
rawHousingData = rawHousingData.drop(columns =["Renovation Year"],axis = 1)
# maybe remove year and season after plotting EDA
# year and season should be all random and have no association with market price

housingData = rawHousingData.dropna()
housingData = housingData.drop_duplicates()

print(housingData.head(n = 3))
print(len(housingData))
