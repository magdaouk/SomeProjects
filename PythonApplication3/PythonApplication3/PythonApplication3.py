import langid

# Define a function to translate text
def translate_text(input_text, source_lang, target_lang):
    # Detect the language of the input text
    detected_lang = langid.classify(input_text)[0]
    
    # Only translate if the detected language matches the source language
    if detected_lang != source_lang:
        return input_text

    # Define the translation dictionary
    translation_dict = {'hello': 'hola', 'how': 'como', 'are': 'estas', 'you': 'tu'}
    
    # Tokenize the input text
    input_tokens = input_text.split()

    # Translate the input text
    translated_words = []
    for token in input_tokens:
        if token.lower() in translation_dict:
            translated_words.append(translation_dict[token.lower()])
        else:
            translated_words.append(token)
    
    # Join the translated words back into a sentence
    translated_text = ' '.join(translated_words)
    return translated_text

# Example usage
input_text = "Hello, how are you?"
source_lang = "en"
target_lang = "es"
translated_text = translate_text(input_text, source_lang, target_lang)
print(translated_text) 
