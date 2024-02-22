import streamlit as st
import nltk
from nltk.corpus import wordnet
import random

# Function to get the synonyms of a word
def get_synonyms(word, tag):
    pos_dict = {
        'v': 'VB', # Verb
        's': 'JJ', # Adjective
        'a': 'JJ', # Adjective
        'r': 'RB', # Adverb
        # 'n': 'NN', # Nouns
    }
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            syn_pos = syn.pos()
            if syn_pos in pos_dict and pos_dict[syn_pos] == tag[:2]:
                print({'lemma_name': lemma.name(), 'syn_pos': syn_pos})
                synonyms.append(lemma.name())
    return synonyms


# Paraphrasing function
def paraphrase_sentence(sentence):
    words = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(words)
    print({'tagged_words': tagged_words})
    paraphrased_words = []

    for word, tag in tagged_words:
        if tag.startswith('NN'):  # to skip only proper nouns use NNP
            print(f'{word} is a noun')
            paraphrased_words.append(word)
            continue

        synonyms = get_synonyms(word, tag=tag)
        print(f'synonyms of {word}', synonyms)
        if synonyms:
            paraphrased_words.append(random.choice(synonyms))
        else:
            paraphrased_words.append(word)
    
    return ' '.join(paraphrased_words)


st.title("Paraphrase your text!")

text_input = st.text_input("Enter your text here:")

if text_input:
    sentence = text_input.lower()
    paraphrased_text = paraphrase_sentence(sentence)
    st.write("Original text:", text_input)
    st.write("Paraphrased text:", paraphrased_text)


# Sample text: The quick brown fox jumps over the lazy dog
# The super adjustable chair can turn against you if you don't know how to use it.
# Sample text:
# This paper is a report on a computer vision algorithm developed to extract the physical features of skin disease and to further distinguish between cancerous and non-cancerous skin lesions. These features are popularly known as the ABCD features namely: Asymmetry, Border, Colour, and Diameter. The algorithm is broken into 4 main processes namely: pre-processing, lesion segmentation, feature extraction and lesion classification. The pre-processing step involves resizing the images using bilinear interpolation, and hair removal using binary thresholding to identify hair pixels. For lesion segmentation, 2 models were developed: using the Otsu thresholding technique which iteratively selects the best threshold value for identifying lesions from other parts of the skin, and deep learning (U-Net). The lesion classification step compares different machine learning models such as Support Vector Machine (SVM) and Deep Learning models. The model with the best accuracy has an accuracy value of 90%. The models were trained on skin images from the ISIC archive. Finally, a web application was developed to view segmentation, ABCD features and prediction results.

# {'tagged_words': [('the', 'DT'), ('super', 'NN'), ('adjustable', 'JJ'), ('chair', 'NN'), ('can', 'MD'), ('turn', 'VB'), ('against', 'IN'), ('you', 'PRP'), ('if', 'IN'), ('you', 'PRP'), ('do', 'VBP'), ("n't", 'RB'), ('know', 'VB'), ('how', 'WRB'), ('to', 'TO'), ('use', 'VB'), ('it', 'PRP'), ('.', '.')]}