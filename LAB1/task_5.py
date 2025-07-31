def word_frequency():
    text = input("Enter a string: ")
    words = text.split()
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    return freq_dict

# Example usage
if __name__ == "__main__":
    result = word_frequency()
    print(result)