import streamlit as st
import pandas as pd
from wordcloud import WordCloud


# Load the dataset
@st.cache_data
def load_data():
    return pd.read_excel("preprocessed_categorized_file.xlsx")


df = load_data()


def show_tags(df):
    st.subheader("Tags Analysis")
    st.write("This section will contain analysis related to tags.")

    # Visualization 6: Word cloud of Tags
    st.subheader("Word cloud of Tags")
    tags_text = " ".join(df["Tags"].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color="#0e1117").generate(
        tags_text
    )
    st.image(wordcloud.to_array())
    # st.image(tags_text, caption="Word Cloud of Tags")


show_tags(df)
