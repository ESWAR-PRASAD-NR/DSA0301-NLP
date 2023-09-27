import spacy

# Load the language model
nlp = spacy.load('en_core_web_sm')

# Text to be processed
text = "This is the first sentence. Here is the second sentence. And this is the third sentence."

# Process the text using spaCy
doc = nlp(text)

# Extract individual sentences
sentences = list(doc.sents)

# Print the sentences
for sentence in sentences:
    print(sentence.text)
