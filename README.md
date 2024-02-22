# frayza
An NLP AI that can paraphrase and summarize your text.  

Built with:  
🛠️ Huggingface 🤗  
🛠️ NLTK  
🛠️ Streamlit  

Deployed live on [Streamlit](https://frayza.streamlit.app/)

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

Install Streamlit, Huggingface transformers, Torch, NLTK, SentencePiece
```
pip install streamlit torch transformers nltk sentencepiece
```

Alternatively, do automatic installation by running
```
pip install -r requirements.txt
```

if you haven't downloaded NLTK punkt, run the prep.py file
```
python prep.py
```

Run app
```
streamlit run app.py 
```

Docs  
[Pegasus Paraphraser](https://huggingface.co/tuner007/pegasus_paraphrase)