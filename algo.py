def analyze_sentence(sentence):
    # Initialize counters
    sentence_length = 0
    word_count = 0
    vowel_count = 0
    in_word = False  # A flag to track if we are in a word

    vowels = "aeiouAEIOU"  # String containing both lowercase and uppercase vowels
    
    for char in sentence:
        # Increase sentence length for each character
        sentence_length += 1
        
        # Check if character is a vowel
        if char in vowels:
            vowel_count += 1
        
        # Check if the character is a space and we are in a word
        if char == ' ':
            if in_word:  # If we were in a word, the word ends
                word_count += 1
                in_word = False  # Reset word flag
        
        elif char != ' ':  # Any non-space character is part of a word
            if not in_word:  # We just entered a word
                word_count += 1
                in_word = True  # Set word flag
    
    # Last character is a period, which we do not count as part of a word
    # But we do count it in the sentence length (we stop when we hit the period)
    
    return sentence_length, word_count, vowel_count

# Example usage:
sentence = "Hello World."
length, words, vowels = analyze_sentence(sentence)
print(f"Length: {length}, Words: {words}, Vowels: {vowels}")
