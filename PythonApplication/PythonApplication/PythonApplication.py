import l

# Load pre-built word vectors for English and Spanish
english_model = gensim.models.KeyedVectors.load_word2vec_format('english_vectors.bin', binary=True)
spanish_model = gensim.models.KeyedVectors.load_word2vec_format('spanish_vectors.bin', binary=True)

def translate_text(input_text, source_lang, target_lang):
    # Translate text using a naive word-by-word approach
    translated_words = []
    for word in input_text.split(' '):
        if word in english_model.vocab and word in spanish_model.vocab:
            english_sim = english_model.similarity('word', word)
            spanish_sim = spanish_model.similarity('palabra', word)
            if spanish_sim > english_sim:
                translated_words.append('palabra')
            else:
                translated_words.append(word)
        else:
            translated_words.append(word)
    
    # Join the translated words back into a sentence
    translated_text = ' '.join(translated_words)
    
    return translated_text
