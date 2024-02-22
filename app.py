import torch
import streamlit as st
from nltk.tokenize import sent_tokenize
from transformers import PegasusForConditionalGeneration, PegasusTokenizer


model_name = 'tuner007/pegasus_paraphrase'
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)

def get_alternatives(input_text):
  batch = tokenizer([input_text],truncation=True,padding='longest',max_length=60, return_tensors="pt").to(torch_device)
  translated = model.generate(**batch,max_length=60, do_sample=True)
  tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
  return tgt_text

def paraphrase_sentence(text):
    sentences = sent_tokenize(text)
    result = []
    for sentence in sentences:
       alternatives = get_alternatives(sentence)
       result.append(alternatives[0])
    
    return ' '.join(result)


st.title("Paraphrase your text!")

text_input = st.text_input("Enter your text here:")

if text_input:
    sentence = text_input.lower()
    paraphrased_text = paraphrase_sentence(sentence)
    st.write("Original text:", text_input)
    st.write("Paraphrased text:", paraphrased_text)


# Sample Test:
# The ultimate test of your knowledge is your capacity to convey it to another.

# Some 59 MPs have now signed a no confidence motion telling the Speaker to quit. Downing Street repeatedly refused to say whether Rishi Sunak has confidence in him today, while the SNP has called for a vote of no confidence in him. Issuing a further apology in the Commons, Sir Lindsay said he “never, ever wanted to go through a situation where I pick up a phone to find a friend of whatever side has been murdered by a terrorist”. He said: “I also don’t want another attack on this House. I was in the chair on that day. I have seen, I have witnessed. I won’t share the details but the details of the things that have been brought to me are absolutely frightening on all members of this House, on all sides.