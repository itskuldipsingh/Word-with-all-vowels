def find_words_with_all_given_alphabets(words):

  alphabets = set("aeiou")
  all_alphabets_words = []

  for word in words:
    word_set = set(word.lower())
    if alphabets.issubset(word_set):
      all_alphabets_words.append(word)

  return all_alphabets_words

words = ["ant", "elephant", "aeioud", "apple", "banana", "hello", "aeiou", "rhythm","unique", "python", "zebra", "friend", "family","faint", "weight", "doubt", "faulty", "beauty",
    "rhythm", "curious", "courage", "patient", "whisper",    "island", "mountain", "ocean", "rainbow", "sunshine",    "science", "literature", "history", "geography", "mathematics", "music", "art", "dance", "theatre", "cinema",    "computer", "internet", "website", "email", "software", "delicious", "fantastic", "wonderful", "magnificent", "splendid", "vehicle", "transport", "journey", "destination", "explore", "aedious"]
    
words_with_all_alphabets = find_words_with_all_alphabets(words)

print(words_with_all_alphabets)
