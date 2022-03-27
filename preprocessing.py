import numpy as np
import pandas as pd

df = pd.read_csv("consumo_cerveja.csv")
# print(df.head())

# rename the col
df.rename(
    columns={
        "Data": "Date",
        "Temperatura Media (C)": "temp_median_c",
        "Temperatura Minima (C)": "temp_min_c",
        "Temperatura Maxima (C)": "temp_max_c",
        "Precipitacao (mm)": "precip_mm",
        "Final de Semana": "weekend",
        "Consumo de cerveja (litros)": "beer_cons_liters",
    },
    inplace=True,
)

df.drop("Date", axis=1, inplace=True)

# drop empty cols
df = df.dropna()

# clean the data and frame the data types
df["temp_median_c"] = df["temp_median_c"].str.replace(",", ".")
df["temp_median_c"] = df["temp_median_c"].astype("float")

df["temp_min_c"] = df["temp_min_c"].str.replace(",", ".")
df["temp_min_c"] = df["temp_min_c"].astype("float")

df["temp_max_c"] = df["temp_max_c"].str.replace(",", ".")
df["temp_max_c"] = df["temp_max_c"].astype("float")

df["precip_mm"] = df["precip_mm"].str.replace(",", ".")
df["precip_mm"] = df["precip_mm"].astype("float")

df.to_csv("beer.csv", index=False)
