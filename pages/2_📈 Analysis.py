import streamlit as st
import pandas as pd
import numpy as np


# Load the dataset
@st.cache_data
def load_data():
    return pd.read_excel("preprocessed_categorized_file.xlsx")


df = load_data()


def show_views_analysis(df):
    st.subheader("Views Analysis")
    st.write("This section will contain analysis related to views.")

    # Visualization 2: Bar plot of Views by Views Category
    st.subheader("Bar plot of Views by Views Category")
    views_by_views_category = (
        df.groupby("Views_Category")["Views"].sum().sort_values(ascending=False)
    )
    st.bar_chart(views_by_views_category)

    st.subheader("Scatterplot")

    chart_data = pd.DataFrame(df, columns=["Views", "Likes", "Comments"])

    st.scatter_chart(
        chart_data,
        x="Likes",
        y="Views",
        color="Views",
        size="Likes",
    )


show_views_analysis(df)
