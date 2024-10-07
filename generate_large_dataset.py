import random
import pandas as pd

# Modular parts of sentences for positive and negative reviews

# Positive review components
positive_intros = [
    "Absolutely loved it!", "What a fantastic movie!", 
    "A brilliant masterpiece!", "One of the best movies I've ever seen!", 
    "Loved every moment of it.", "Incredible storytelling!"
]

positive_details = [
    "The plot was engaging", "The acting was top-notch", 
    "The cinematography was breathtaking", "The characters were well-developed",
    "It kept me on the edge of my seat", "The direction was flawless",
    "It had an emotional depth that really resonated with me"
]

positive_conclusions = [
    "Highly recommend it to anyone!", "An unforgettable experience.",
    "A must-watch for everyone.", "Would definitely watch again!",
    "It’s an absolute classic!", "You won't regret watching it!"
]

# Negative review components
negative_intros = [
    "Hated it from start to finish.", "What a waste of time!",
    "Terrible movie.", "One of the worst movies I've seen.",
    "I couldn't wait for it to end.", "Completely unwatchable."
]

negative_details = [
    "The plot made no sense", "The acting was terrible", 
    "The cinematography was bland", "The characters were one-dimensional",
    "It was painfully predictable", "The direction was a mess",
    "It was just boring and uninteresting"
]

negative_conclusions = [
    "Don't waste your time.", "I regret watching this.",
    "Definitely not worth watching.", "Save yourself the trouble.",
    "I would never recommend this to anyone.", "Avoid at all costs!"
]

# Define the number of entries (increase to 10,000)
num_entries = 10000

# Create lists to hold the data
reviews = []
sentiments = []

# Generate 50% positive and 50% negative reviews
for _ in range(num_entries // 2):
    review = f"{random.choice(positive_intros)} {random.choice(positive_details)}. {random.choice(positive_conclusions)}"
    reviews.append(review)
    sentiments.append("positive")

for _ in range(num_entries // 2):
    review = f"{random.choice(negative_intros)} {random.choice(negative_details)}. {random.choice(negative_conclusions)}"
    reviews.append(review)
    sentiments.append("negative")

# Combine into a DataFrame
dataset = pd.DataFrame({
    'review': reviews,
    'sentiment': sentiments
})

# Shuffle the dataset
dataset = dataset.sample(frac=1).reset_index(drop=True)

# Save the dataset to an Excel file
dataset.to_excel("imdb_reviews_large_10000.xlsx", index=False)

print("Dataset with 10,000 entries has been generated and saved as 'imdb_reviews_large_10000.xlsx'.")
