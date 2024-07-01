import streamlit as st
import pandas as pd


# Load the dataset
@st.cache_data
def load_data():
    return pd.read_excel("preprocessed_categorized_file.xlsx")


df = load_data()


def show_summary(df):
    st.subheader("Summary Statistics")
    st.write(df.describe())


show_summary(df)
