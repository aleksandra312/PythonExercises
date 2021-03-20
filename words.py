def print_upper_words(words, must_start_with):
    """Print words in upper case."""
    for word in words:
        print(word.upper())

def print_words_start_with(words, must_start_with):
    """Print words starting with a letter."""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word)
                break
