import pandas as pd

df = pd.read_csv("data/raw/bodyfat.csv")

print("DATASET INFO")
print(df.info())

print("\nMISSING VALUES")
print(df.isna().sum())

print("\nDUPLICATES")
print("Duplicate rows:", df.duplicated().sum())

print("\nFIRST 5 ROWS")
print(df.head())

print("\nNUMERIC SUMMARY")
print(df.describe().T)

print("\nSUSPICIOUS HEIGHTS")
print(df[df["Height"] < 50])

print("\nSUSPICIOUS BODY FAT")
print(df[df["BodyFat"] <= 0])

print("\nVERY HIGH WEIGHT")
print(df[df["Weight"] > 300])

print("\nPOTENTIAL OUTLIERS")

for column in df.select_dtypes(include="number").columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df[column] < lower) | (df[column] > upper)]

    print(f"{column}: {len(outliers)} potential outliers")