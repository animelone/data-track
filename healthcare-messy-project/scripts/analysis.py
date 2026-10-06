import pandas as pd

df = pd.read_csv("data/bodyfat_cleaned.csv")

# Question 1: How does average body fat differ across age groups?
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0, 29, 39, 49, 59, 100],
    labels=["Under 30", "30-39", "40-49", "50-59", "60+"]
)

age_analysis = df.groupby("AgeGroup", observed=True)["BodyFat"].mean()

print("\nAVERAGE BODY FAT BY AGE GROUP")
print(age_analysis)


# Question 2: Does average body fat increase as weight increases?
df["WeightGroup"] = pd.cut(
    df["Weight"],
    bins=[0, 150, 175, 200, 250, 1000],
    labels=["Under 150", "150-175", "176-200", "201-250", "Over 250"]
)

weight_analysis = df.groupby("WeightGroup", observed=True)["BodyFat"].mean()

print("\nAVERAGE BODY FAT BY WEIGHT GROUP")
print(weight_analysis)


# Question 3: Which body measurement has the strongest relationship with body fat?
measurements = [
    "Neck",
    "Chest",
    "Abdomen",
    "Hip",
    "Thigh",
    "Knee",
    "Ankle",
    "Biceps",
    "Forearm",
    "Wrist"
]

correlations = df[measurements + ["BodyFat"]].corr()["BodyFat"].drop("BodyFat")

correlation_table = (
    correlations
    .sort_values(ascending=False)
    .reset_index()
)

correlation_table.columns = ["Measurement", "Correlation"]

print("\nCORRELATION TABLE")
print(correlation_table)


# Question 4: How does average body fat differ across height groups?
df["HeightGroup"] = pd.cut(
    df["Height"],
    bins=[0, 65, 68, 71, 74, 100],
    labels=["Under 65", "65-68", "69-71", "72-74", "75+"]
)

height_analysis = df.groupby("HeightGroup", observed=True)["BodyFat"].mean()

print("\nAVERAGE BODY FAT BY HEIGHT GROUP")
print(height_analysis)