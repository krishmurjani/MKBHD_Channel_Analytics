import streamlit as st
import pandas as pd


# Load the dataset
@st.cache_data
def load_data():
    return pd.read_excel("preprocessed_categorized_file.xlsx")


df = load_data()


def show_likes_comments(df):
    st.subheader("Likes and Comments")
    st.write("This section will contain analysis related to likes and comments.")

    # Visualization 3: Bar plot of Likes and Comments by Category
    st.subheader("Bar plot of Likes and Comments by Category")
    likes_comments_by_category = df.groupby("Category")[["Likes", "Comments"]].sum()
    st.bar_chart(likes_comments_by_category)

    # Visualization 4: Correlation between Likes and Comments
    st.subheader("Correlation between Likes and Comments")
    st.write(df[["Likes", "Comments"]].corr())


show_likes_comments(df)
