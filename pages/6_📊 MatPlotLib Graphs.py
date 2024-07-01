import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load the dataset
@st.cache_data
def load_data():
    return pd.read_excel("preprocessed_categorized_file.xlsx")


df = load_data()

st.subheader("Distribution of Duration Category")
sns.countplot(data=df, x="Duration_Category")
plt.xticks(rotation=45)
st.pyplot()

st.subheader("Top 10 videos by Views")
top_10_views = df.nlargest(10, "Views")
st.write(top_10_views)

# Visualization 4: Box plot of Views by Duration Category
st.subheader("Box plot of Views by Duration Category")
sns.boxplot(data=df, x="Duration_Category", y="Views")
plt.xticks(rotation=45)
plt.ylabel("Views")
st.pyplot()

# Visualization 5: Distribution of Comments
st.subheader("Distribution of Comments")
sns.histplot(df["Comments"], bins=20, kde=True)
plt.xlabel("Number of Comments")
plt.ylabel("Frequency")
st.pyplot()

# Visualization 6: Pairplot of numeric variables
st.subheader("Pairplot of numeric variables")
sns.pairplot(df[["Views", "Likes", "Comments", "Duration_Seconds"]])
st.pyplot()

# Visualization 7: Correlation heatmap
st.subheader("Correlation heatmap")
correlation = df[["Views", "Likes", "Comments", "Duration_Seconds"]].corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
st.pyplot()

# Visualization 8: Bar plot of Average Likes and Comments by Category
st.subheader("Bar plot of Average Likes and Comments by Category")
avg_likes_comments = df.groupby("Category")[["Likes", "Comments"]].mean()
avg_likes_comments.plot(kind="bar")
plt.xlabel("Category")
plt.ylabel("Average Likes/Comments")
st.pyplot()

# Visualization 1: Pie chart of Views by Category
# Visualization 1: Pie chart of Views by Category
st.subheader("Pie chart of Views by Category")
views_by_category = (
    df.groupby("Category")["Views"]
    .sum()
    .sort_values(ascending=False)
    .drop(
        [
            "Tablets",
            "Headphones Reviews",
            "Wearable & Devices",
            "Headphone Reviews",
            "Laptop Reviews",
            "Tech Tutorial",
        ]
    )
)
pie_chart = views_by_category.plot.pie(autopct="%1.1f%%")

# Adjusting font size and label spacing
plt.rcParams["font.size"] = 6
plt.rcParams["text.color"] = "black"  # You can adjust label color if needed
plt.rcParams["text.usetex"] = False
plt.subplots_adjust(wspace=3)  # Adjust spacing between labels

st.pyplot(pie_chart.figure)

st.set_option("deprecation.showPyplotGlobalUse", False)
