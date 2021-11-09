import streamlit as st
import spacy
from spacy import displacy
from spacy_streamlit import visualize_parser, visualize_ner

nlp = spacy.load('es_core_news_md')

def dependency():
    message = st.text_input('Message for Dependency')
    doc = nlp(message)
    return visualize_parser(doc), visualize_ner(doc, labels=['ORG','PER', 'DATE', 'MONEY', 'LANGUAGE', 'LOC','EVENT','FAC','PERSON'])