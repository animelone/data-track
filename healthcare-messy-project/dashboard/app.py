import streamlit as st
import pandas as pd



st.title("Body Fat Analysis Dashboard")

st.write(
    "This dashboard explores how body fat percentage varies by age, "
    "weight, and body measurements using a cleaned body composition dataset."
)

df = pd.read_csv("data/bodyfat_cleaned.csv")



# Key performance indicators
col1, col2, col3 = st.columns(3)

col1.metric(
    "Records",
    len(df)
)

col2.metric(
    "Average Body Fat",
    f"{df['BodyFat'].mean():.1f}%"
)

col3.metric(
    "Average Age",
    f"{df['Age'].mean():.1f}"
)

# Create age groups for analysis.
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0, 29, 39, 49, 59, 100],
    labels=["Under 30", "30-39", "40-49", "50-59", "60+"]
)

# Interactive age-group filter.
selected_age = st.selectbox(
    "Select an age group",
    ["All"] + list(df["AgeGroup"].dropna().unique())
)

if selected_age != "All":
    filtered_df = df[df["AgeGroup"] == selected_age]
else:
    filtered_df = df

st.write(f"Showing {len(filtered_df)} records")

st.dataframe(filtered_df)

st.subheader("Average Body Fat by Age Group")

age_bodyfat = (
    df.groupby("AgeGroup", observed=True)["BodyFat"]
    .mean()
    .reset_index()
)

st.bar_chart(
    age_bodyfat,
    x="AgeGroup",
    y="BodyFat"
)

st.subheader("Average Body Fat by Weight Group")

df["WeightGroup"] = pd.cut(
    df["Weight"],
    bins=[0, 150, 175, 200, 250, 1000],
    labels=["Under 150", "150-175", "176-200", "201-250", "Over 250"]
)

weight_bodyfat = (
    df.groupby("WeightGroup", observed=True)["BodyFat"]
    .mean()
    .reset_index()
)

st.bar_chart(
    weight_bodyfat,
    x="WeightGroup",
    y="BodyFat"
)

st.subheader("Body Measurements vs. Body Fat")

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

correlations = (
    df[measurements + ["BodyFat"]]
    .corr()["BodyFat"]
    .drop("BodyFat")
    .sort_values(ascending=False)
)

correlation_table = correlations.reset_index()
correlation_table.columns = ["Measurement", "Correlation"]

st.bar_chart(
    correlation_table,
    x="Measurement",
    y="Correlation"
)