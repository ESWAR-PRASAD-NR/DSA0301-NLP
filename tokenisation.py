import nltk
nltk.download('punkt')  # Download the Punkt tokenizer models if not already downloaded

from nltk.tokenize import word_tokenize, sent_tokenize

# Sample text
text = "Tokenization is an important step in NLP. It splits text into tokens."

# Tokenize the text into words
words = word_tokenize(text)

# Tokenize the text into sentences
sentences = sent_tokenize(text)

# Print the results
print("Word tokens:")
print(words)

print("\nSentence tokens:")
print(sentences)
