import streamlit as st

st.title("AgriData Explorer")
st.write("Agriculture Data Analysis Dashboard")
st.info(
    "This dashboard provides insights into agricultural production, "
    "crop performance, cultivated area, and production efficiency."
)
import streamlit as st


import pandas as pd

# Load agriculture dataset
df = pd.read_csv(r"C:/Users/WINDOWS/Downloads/agriculture_data.csv")
# Crop Filter

st.sidebar.header("Filter Data")

selected_crop = st.sidebar.selectbox(
    "Select Crop",
    ["All"] + sorted(df["Crop"].unique().tolist())
)

if selected_crop != "All":
    df = df[df["Crop"] == selected_crop]

# State Filter

selected_state = st.sidebar.selectbox(
    "Select State",
    ["All"] + sorted(df["State"].unique().tolist())
)

if selected_state != "All":
    df = df[df["State"] == selected_state]

# Year Filter

selected_year = st.sidebar.selectbox(
    "Select Year",
    ["All"] + sorted(df["Year"].unique().tolist())
)

if selected_year != "All":
    df = df[df["Year"] == selected_year]

# Display the dataset
st.subheader("Agriculture Dataset")
st.dataframe(df)
# Dataset Summary

st.subheader("Dataset Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(df))
col2.metric("Total Crops", df["Crop"].nunique())
col3.metric("Total Production", f"{df['Production_Tonnes'].sum():,} tonnes")
# Crop-wise Production

st.subheader("Crop-wise Production")

crop_production = df.groupby("Crop")["Production_Tonnes"].sum()

st.bar_chart(crop_production)
# State-wise Production

st.subheader("State-wise Production")

state_production = df.groupby("State")["Production_Tonnes"].sum()

st.bar_chart(state_production)
# Area vs Production

st.subheader("Area vs Production")

st.scatter_chart(
    df,
    x="Area_Hectares",
    y="Production_Tonnes"
)
# Production per Hectare

st.subheader("Production per Hectare")

df["Production_Per_Hectare"] = (
    df["Production_Tonnes"] / df["Area_Hectares"]
)

st.dataframe(
    df[["State", "Crop", "Production_Per_Hectare"]]
)
# Average Production per Hectare

average_production = df["Production_Per_Hectare"].mean()

st.metric(
    "Average Production per Hectare",
    f"{average_production:.2f} tonnes/hectare"
)
# Highest Producing Crop

highest_crop = df.groupby("Crop")["Production_Tonnes"].sum().idxmax()
highest_production = df.groupby("Crop")["Production_Tonnes"].sum().max()

st.subheader("Highest Producing Crop")

st.success(
    f"{highest_crop} - {highest_production:,} tonnes"
)