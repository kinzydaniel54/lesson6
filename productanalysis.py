# Task 1 Keyword Highlighter --------------------------------------------------------------------------------
# List of reviews
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
# List of keywords to be capitalized
keywords = ["good", "excellent", "bad", "poor", "average"]
# Function to capitalize keywords in a review
def capitalize_keywords(review, keywords):
    # Iterate over each keyword in the list
    for keyword in keywords:
        # Replace the keyword with its uppercase version (lowercase and capitalized)
        review = review.replace(keyword, keyword.upper())
        review = review.replace(keyword.capitalize(), keyword.upper())
    return review
# Iterate over each review in the reviews list
for review in reviews:
    # Capitalize keywords in the current review and print the result
    print(capitalize_keywords(review, keywords))


# Task 2: Sentiment Tally--------------------------------------------------------------------------------
# List of positive and negative words and the reviews
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing", "impressed", "recommended"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
# Function to tally the number of positive and negative words in a review
def sentiment_tally(reviews, positive_words, negative_words):
    positive_count = 0
    negative_count = 0
    # Iterate over each review in the reviews list
    for review in reviews:
        # Check if the word is in the list of positive words
        words = review.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '').split()
        for word in words:
            # Check if the word is in the list of positive words
            if word in positive_words:
                positive_count += 1
            # Check if the word is in the list of negative words
            elif word in negative_words:
                negative_count += 1
    return positive_count, negative_count
positive_count, negative_count = sentiment_tally(reviews, positive_words, negative_words)
print("Positive words count:", positive_count)
print("Negative words count:", negative_count)

#Task 3: Review Summary --------------------------------------------------------------------------------
# Function to create a summary of each review
def create_review_summary(review):
    # Trim review to first 30 characters
    summary = review[:30]
    # Ensure summary doesn't cut off in the middle of a word
    if len(review) > 30:
        # Find the last space within the first 30 characters
        last_space_index = summary.rfind(' ')
        # Trim to the last space
        if last_space_index != -1:
            summary = summary[:last_space_index]
        # Add ellipsis at the end
        summary += "…"
    return summary
# Create summaries for each review
for review in reviews:
    summary = create_review_summary(review)
    print(summary)