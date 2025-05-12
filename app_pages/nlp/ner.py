# # app_pages/nlp/ner.py
# import spacy
# import streamlit as st

# # Load English spaCy model
# nlp_en = spacy.load("en_core_web_sm")

# # Optional: Nepali support using stanza (if you have it installed)
# # from stanza.pipeline.core import Pipeline
# # nlp_ne = Pipeline(lang="ne")


# def english_ner(text):
#     doc = nlp_en(text)
#     return [(ent.text, ent.label_) for ent in doc.ents]


# def show():
#     st.title("🧬 Named Entity Recognition (NER)")

#     text = st.text_area("Enter text for NER tagging")

#     if st.button("Run NER"):
#         if text:
#             entities = english_ner(text)
#             if entities:
#                 st.subheader("Entities Found:")
#                 for word, label in entities:
#                     st.markdown(f"- **{word}** → {label}")
#             else:
#                 st.info("No named entities found.")
#     else:
#         st.warning("Please enter some text to analyze.")

