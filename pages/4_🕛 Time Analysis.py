import streamlit as st
import pandas as pd


# Load the dataset
@st.cache_data
def load_data():
    return pd.read_excel("preprocessed_categorized_file.xlsx")


df = load_data()


def show_time_analysis(df):
    st.subheader("Time Analysis")
    st.write("This section will contain analysis related to time.")

    # Visualization 5: Line plot of Views over time
    st.subheader("Line plot of Views over time")
    df["Uploaded Date"] = pd.to_datetime(df["Uploaded Date"])
    views_over_time = df.groupby("Uploaded Date")["Views"].sum()
    st.line_chart(views_over_time)


show_time_analysis(df)
