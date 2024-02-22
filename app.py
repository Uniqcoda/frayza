import torch
import nltk
from nltk.tokenize import sent_tokenize
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

nltk.download('punkt')

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

def summarize_sentence(text):
    alternatives = get_alternatives(text)
    return alternatives[0]
