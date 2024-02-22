import streamlit as st
from helpers import paraphrase_sentence, summarize_sentence

function_options = ['Paraphrase','Summarize']

st.title("Welcome to Frayza")

with st.form("my_form"):
    st.write("**Enter your text and choose whether you want to paraphrase or summarize**")
    text_input = st.text_input("Enter your text here:")
    function = st.radio('Pick one:', function_options)
    submitted = st.form_submit_button("Submit")
    
    if submitted and text_input and function:
        st.write("**Original text:**\n", text_input)
        sentence = text_input.lower()

        with st.spinner('Wait for it...'):
            if function == 'Paraphrase':
                paraphrased_text = paraphrase_sentence(sentence)
                st.write("**Paraphrased text:**\n", paraphrased_text)

            if function == 'Summarize':
                summarized_text = summarize_sentence(sentence)
                st.write("**Summarized text:**\n", summarized_text)
