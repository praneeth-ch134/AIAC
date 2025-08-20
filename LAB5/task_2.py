import re

def analyze_review():
    positive_words = {'good', 'great', 'excellent', 'amazing', 'wonderful', 'love',
                       'fantastic', 'positive', 'satisfied', 'happy'}
    negative_words = {'bad', 'terrible', 'poor', 'awful', 'hate', 'disappointed',
                       'negative', 'unsatisfied', 'sad', 'worst'}

    review = input("Enter your review: ").lower()
    words = set(re.findall(r'\b\w+\b', review))

    pos_count = len(words & positive_words)
    neg_count = len(words & negative_words)

    if pos_count > neg_count:
        print("The review is positive.")
    elif neg_count > pos_count:
        print("The review is negative.")
    else:
        print("The review is neutral or cannot be determined.")

# Example usage:
analyze_review()