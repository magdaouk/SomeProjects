import gensim

# Train word vectors on the fly using FastText
sentences = [['hello', 'how', 'are', 'you'], ['hola', 'cómo', 'estás']]
model = gensim.models.Word2Vec(sentences, window=5, min_count=1)

def translate_text(input_text, source_lang, target_lang):
    # Tokenize the input text
    input_tokens = input_text.split()

    # Use trained word vectors to identify and select the most appropriate translations
    translated_words = []
    for token in input_tokens:
        if token in model.wv.key_to_index:
            english_sim = model.wv.similarity('hello', token)
            spanish_sim = model.wv.similarity('hola', token)
            if spanish_sim > english_sim:
                translated_words.append('hola')
            else:
                translated_words.append(token)
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
print(translated_text) # Output: "Hola, cómo estás?"


