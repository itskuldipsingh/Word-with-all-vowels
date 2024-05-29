def find_words_with_all_given_alphabets(words):
    # Define the set of alphabets that we need to check in each word
    alphabets = set("aeiou")
    
    # Initialize an empty list to store words that contain all the alphabets
    all_alphabets_words = []

    # Iterate through each word in the provided list
    for word in words:
        # Convert the word to lowercase and create a set of its characters
        word_set = set(word.lower())
        
        # Check if the set of alphabets is a subset of the word's character set
        if alphabets.issubset(word_set):
            # If true, add the word to the result list
            all_alphabets_words.append(word)

    # Return the list of words containing all the alphabets
    return all_alphabets_words

# List of words to be checked
words = ["ant", "elephant", "aeioud", "apple", "banana", "hello", "aeiou", "rhythm", "unique", 
         "python", "zebra", "friend", "family", "faint", "weight", "doubt", "faulty", "beauty",
         "rhythm", "curious", "courage", "patient", "whisper", "island", "mountain", "ocean", 
         "rainbow", "sunshine", "science", "literature", "history", "geography", "mathematics", 
         "music", "art", "dance", "theatre", "cinema", "computer", "internet", "website", "email", 
         "software", "delicious", "fantastic", "wonderful", "magnificent", "splendid", "vehicle", 
         "transport", "journey", "destination", "explore", "aedious"]

# Find words with all given alphabets
words_with_all_alphabets = find_words_with_all_given_alphabets(words)

# Print the result
print(words_with_all_alphabets)
