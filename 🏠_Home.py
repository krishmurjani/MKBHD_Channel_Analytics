import streamlit as st
import pandas as pd


# Load the dataset
@st.cache_data
def load_data():
    return pd.read_excel("preprocessed_categorized_file.xlsx")


df = load_data()

# Title of the dashboard
st.title("YouTube Video Analytics Dashboard")

# Define functions for each section

st.write(df.describe())
st.sidebar.header("Filters")
selected_category = st.sidebar.selectbox("Select Category", df["Category"].unique())

# Filter data based on user selection
filtered_df = df[df["Category"] == selected_category]

# Display filtered data
st.write("## Filtered YouTube Dataset")
st.write(filtered_df)
