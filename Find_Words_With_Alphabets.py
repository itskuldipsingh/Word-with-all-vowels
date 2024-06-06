import time

# Start the timer
StartTime = time.time()

def find_words_with_all_given_alphabets(file_path):
    alphabets = set("aeiou")
    all_alphabets_words = []

    # Open the file and read it line by line
    with open(file_path, 'r') as file:
        for word in file:
            word = word.strip()  # Remove any surrounding whitespace/newline characters
            word_set = set(word.lower())
            if alphabets.issubset(word_set):
                all_alphabets_words.append(word)
    
    return all_alphabets_words

# File path to the words file (relative path assuming the file is in the same directory)
file_path = 'words.txt'

# Find words with all given alphabets
words_with_all_alphabets = find_words_with_all_given_alphabets(file_path)

# Print the result
print(words_with_all_alphabets)

# End the timer
EndTime = time.time()
Time = EndTime - StartTime
print(f"Time: {Time} seconds")
