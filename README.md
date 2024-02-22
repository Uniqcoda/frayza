# frayza
A paraphrasing tool

Create virtual environment
```
python -m venv .venv
```

Activate virtual environment
```
source .venv/bin/activate
```

Upgrade pip
```
python3 -m pip install --upgrade pip
```

Install streamlit, Hugging transformers, Torch, NLTK, sentencepiece
```
pip install streamlit torch transformers nltk SentencePiece
```

if you haven't downloaded NLTK stopwords, run the prep.py file
```
python prep.py
```

Run app
```
streamlit run app.py 
```

Docs  
[Pegasus Paraphraser](https://huggingface.co/tuner007/pegasus_paraphrase)