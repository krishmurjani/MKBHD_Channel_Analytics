import streamlit as st
import pandas as pd
import random

# Load the dataset
data = pd.read_excel("preprocessed_categorized_file.xlsx")

# Define categories to exclude
exclude_categories = ["headphones reviews", "tech tutorial", "wearable & devices"]

# Filter categories
filtered_categories = [
    category
    for category in data["Category"].unique()
    if category.lower() not in map(str.lower, exclude_categories)
]

# Define placeholders and their substitutes
substitutes = {
    "[topic]": [
        "smartphones",
        "electric vehicles",
        "software updates",
        "future trends",
        "product reviews",
    ],
    "[person]": [
        "Elon Musk",
        "Tim Cook",
        "Marques Brownlee",
        "Jeff Bezos",
        "Mark Zuckerberg",
    ],
}


# Function to generate suggestions
def generate_suggestions(data):
    suggestions = {}
    for category, group in data.groupby("Category"):
        # Randomly select 4-5 suggestions
        random_suggestions = random.sample(
            [
                f"This video was really helpful, thanks for sharing!",
                f"I would love to see a sequel to this video: {group['Title'].sample().iloc[0]}",
                f"I have a suggestion for a new video: {group['Title'].sample().iloc[0]}",
                f"I really like your style of videos, keep up the good work!",
                f"Can you make a video about {random.choice(substitutes['[topic]'])}?",
                f"I'm glad I found your channel, I'm subscribed now!",
                f"I think you should make a video about {random.choice(substitutes['[topic]'])} more often",
                f"I'm really enjoying your videos, thanks for making them!",
                f"I really enjoyed this video, thanks for making it!",
                f"Add more videos like this",
                f"I appreciate the effort you put into making this video. Keep up the good work!",
                f"I'm not a fan of the editing style in this video. It felt too rushed.",
                f"Please continue making videos like this. They are incredibly helpful!",
                f"I expected more from this video. It didn't meet my expectations.",
                f"I'm glad I stumbled upon your channel. Subscribed for more!",
                f"This video was a bit too technical for my taste. Could you make it more beginner-friendly?",
                f"I really enjoyed the humor in this video. It kept me engaged throughout!",
                f"I think you should focus more on {random.choice(substitutes['[topic]'])} in your future videos. It's an area of interest for many.",
            ],
            k=random.randint(4, 5),
        )  # Randomly select 4-5 suggestions
        # random_suggestions = random.sample(random_suggestions, k=random.randint(4, 5))
        # Replace placeholders with substitutes
        for i, suggestion in enumerate(random_suggestions):
            for placeholder, substitutes_list in substitutes.items():
                if placeholder in suggestion:
                    substitute = random.choice(substitutes_list)
                    random_suggestions[i] = suggestion.replace(placeholder, substitute)
        suggestions[category] = random_suggestions
    return suggestions


# Generate suggestions
suggestions = generate_suggestions(data)


# Streamlit UI
# def main():
#     st.title("YouTube Channel Suggestions")

#     # Add navigation bar to switch between pages
#     pages = ["Home", "Suggestions"]
#     choice = st.sidebar.radio("Navigation", pages)

#     if choice == "Home":
#         st.write("Welcome to the YouTube Channel Suggestions dashboard!")
#         # Add any other content for the home page here
#     elif choice == "Suggestions":
#         st.write("Here are some suggestions for your YouTube channel:")
#         # Display suggestions
#         for category, suggested_comments in suggestions.items():
#             st.subheader(f"Category: {category}")
#             for i, comment in enumerate(suggested_comments):
#                 st.write(f"{i+1}: {comment}")
#             st.write("---")  # Add a horizontal line between categories


def main():
    st.title("YouTube Channel Suggestions")

    # Add select box to choose category
    category = st.selectbox("Select Category", sorted(filtered_categories))

    # Display suggestions for the selected category
    st.write(f"Here are some suggestions for the '{category}' category:")
    category_videos = data[data["Category"] == category]["Title"].tolist()
    for i, suggestion in enumerate(suggestions[category]):
        random_video_title = random.choice(category_videos)
        st.write(f"{i+1}. Video Name: {random_video_title}, Suggestion: {suggestion}")


if __name__ == "__main__":
    main()
