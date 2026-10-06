# Healthcare Body Fat Analysis

## Project Overview

This project analyzes a body composition dataset to explore patterns in body fat percentage across age, weight, and body measurements.

The project follows a complete data analytics workflow:

1. Data auditing
2. Data cleaning
3. Exploratory analysis
4. Data visualization
5. Interactive dashboard development

## Dataset

The dataset contains 252 observations and 15 variables describing body composition measurements.

Key variables include:

- BodyFat
- Age
- Weight
- Height
- Neck
- Chest
- Abdomen
- Hip
- Thigh
- Knee
- Ankle
- Biceps
- Forearm
- Wrist

The cleaned dataset contains 250 observations after removing two records identified as implausible measurements.

## Data Cleaning

The raw dataset was audited using:

- `df.info()`
- `df.isna().sum()`
- Duplicate checks
- Descriptive statistics
- Range checks
- IQR-based outlier analysis

### Cleaning decisions

Two records were removed:

1. A record with a height of 29.5 inches, which was considered implausible for an adult body-composition measurement.
2. A record with a body-fat value of 0%, which was considered an implausible measurement for this analysis.

Potential statistical outliers were not automatically removed because an outlier is not necessarily an error.

The original raw dataset was preserved, and the cleaned dataset was saved separately.

## Analysis Questions

The analysis focused on four questions:

### 1. How does average body fat differ across age groups?

Average body fat generally increased with age.

The highest average was observed in the 60+ group at approximately 24.36%.

### 2. Does average body fat increase as weight increases?

A strong upward pattern was observed.

| Weight Group | Average Body Fat |
|---|---:|
| Under 150 | 10.78% |
| 150-175 | 16.54% |
| 176-200 | 20.65% |
| 201-250 | 25.93% |
| Over 250 | 34.85% |

### 3. Which body measurement has the strongest relationship with body fat?

Abdomen circumference had the strongest correlation with body fat.

| Measurement | Correlation |
|---|---:|
| Abdomen | 0.809 |
| Chest | 0.696 |
| Hip | 0.613 |
| Thigh | 0.544 |
| Knee | 0.494 |
| Neck | 0.490 |
| Biceps | 0.487 |
| Forearm | 0.351 |
| Wrist | 0.344 |
| Ankle | 0.254 |

Correlation describes association and does not establish causation.

### 4. How does average body fat differ across height groups?

Height did not show a clear consistent relationship with body fat in this dataset.

## Dashboard

The Streamlit dashboard includes:

- Interactive age-group filtering
- Record count KPI
- Average body-fat KPI
- Average-age KPI
- Average body fat by age group
- Average body fat by weight group
- Body-measurement correlation analysis
- Filtered dataset table

## Project Structure

```text
healthcare-messy-project/
│
├── data/
│   ├── raw/
│   │   └── bodyfat.csv
│   └── bodyfat_cleaned.csv
│
├── notebooks/
│
├── scripts/
│   ├── audit.py
│   ├── clean_data.py
│   └── analysis.py
│
├── dashboard/
│   └── app.py
│
└── README.md