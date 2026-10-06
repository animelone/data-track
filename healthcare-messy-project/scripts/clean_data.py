import pandas as pd

# Load the original raw dataset so it remains unchanged.
df = pd.read_csv("data/raw/bodyfat.csv")

# Remove the record with an implausible adult height of 29.5 inches.
df = df[df["Height"] >= 50]

# Remove the record with a BodyFat value of 0%, which is not a credible measurement.
df = df[df["BodyFat"] > 0]

# Save the cleaned dataset as a new file so the raw data is preserved.
df.to_csv("data/bodyfat_cleaned.csv", index=False)

print("Cleaning complete.")
print(f"Original rows: 252")
print(f"Cleaned rows: {len(df)}")
print(f"Rows removed: {252 - len(df)}")