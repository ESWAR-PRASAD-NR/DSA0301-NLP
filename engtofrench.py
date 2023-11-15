from transformers import MarianMTModel, MarianTokenizer

def translate_english_to_french(text):
    # Load pre-trained MarianMT model and tokenizer for English to French translation
    model_name = "Helsinki-NLP/opus-mt-en-fr"
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    # Tokenize and translate the input text
    input_ids = tokenizer.encode(text, return_tensors="pt")
    translation_ids = model.generate(input_ids)

    # Decode the translated text
    translated_text = tokenizer.decode(translation_ids[0], skip_special_tokens=True)

    return translated_text

# Example usage
english_text = "Hello, how are you?"
french_translation = translate_english_to_french(english_text)

print(f"English Text: {english_text}")
print(f"French Translation: {french_translation}")
