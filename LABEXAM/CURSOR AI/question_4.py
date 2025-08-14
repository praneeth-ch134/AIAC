import string

# Define a set of common English stop words
stop_words = {
    "a", "an", "the", "and", "or", "but", "if", "while", "with", "of", "at", "by", "for", "to", "in", "on", "from",
    "up", "down", "out", "over", "under", "again", "further", "then", "once", "here", "there", "all", "any", "both",
    "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
    "too", "very", "can", "will", "just", "don", "should", "now", "is", "am", "are", "was", "were", "be", "been",
    "being", "have", "has", "had", "do", "does", "did", "having", "he", "she", "it", "they", "them", "his", "her",
    "its", "their", "you", "your", "yours", "me", "my", "mine", "we", "us", "our", "ours", "him", "who", "whom",
    "this", "that", "these", "those", "as", "about", "into", "through", "during", "before", "after", "above", "below",
    "between", "because", "until", "against", "off", "over", "under", "again", "further", "then", "once"
}
text = input("Enter your text: ")# Remove punctuation
text_no_punct = text.translate(str.maketrans('', '', string.punctuation))

# Convert to lowercase
text_lower = text_no_punct.lower()

# Split into words
words = text_lower.split()

# Remove stop words
filtered_words = [word for word in words if word not in stop_words]

# Join and display the result
output = ' '.join(filtered_words)
print("Processed text:", output)
