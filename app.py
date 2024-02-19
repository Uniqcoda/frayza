import streamlit as st
import nltk
from nltk.corpus import wordnet
import random

# Function to get the synonyms of a word
def get_synonyms(word, pos=None):
    synonyms = []
    for syn in wordnet.synsets(word):
        print({'syn': syn})
        for lemma in syn.lemmas():
            print({'lemma_name': lemma.name(), 'pos': pos, 'syn_pos': syn.pos()})
            if not pos or syn.pos() == pos:
                synonyms.append(lemma.name())
    return synonyms


# Paraphrasing function
def paraphrase_sentence(sentence):
    words = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(words)
    print({'tagged_words': tagged_words})
    paraphrased_words = []
    tag_dict = {
        'VB': 'v', # Verb
        'JJ': 'a', # Adjective
        'RB': 'r', # Adverb
        # 'NN': 'n', # Nouns
    }
    
    for word, tag in tagged_words:
        if tag.startswith('NN'):  # to skip proper nouns use NNP
            print(f'{word} is a noun')
            paraphrased_words.append(word)
            continue
        if tag[:2] in tag_dict:
            pos = tag_dict[tag[:2]]
        else:
            pos = None
        synonyms = get_synonyms(word, pos=pos)
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
# Sample text:
# This paper is a report on a computer vision algorithm developed to extract the physical features of skin disease and to further distinguish between cancerous and non-cancerous skin lesions. These features are popularly known as the ABCD features namely: Asymmetry, Border, Colour, and Diameter. The algorithm is broken into 4 main processes namely: pre-processing, lesion segmentation, feature extraction and lesion classification. The pre-processing step involves resizing the images using bilinear interpolation, and hair removal using binary thresholding to identify hair pixels. For lesion segmentation, 2 models were developed: using the Otsu thresholding technique which iteratively selects the best threshold value for identifying lesions from other parts of the skin, and deep learning (U-Net). The lesion classification step compares different machine learning models such as Support Vector Machine (SVM) and Deep Learning models. The model with the best accuracy has an accuracy value of 90%. The models were trained on skin images from the ISIC archive. Finally, a web application was developed to view segmentation, ABCD features and prediction results.
