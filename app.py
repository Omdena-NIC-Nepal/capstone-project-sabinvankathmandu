import streamlit as st
import sys
from app_pages import data_exploratoins, dataanalysis, train_model, prediction
from scripts.climate.data_utils import load_climate_data
from app_pages.gis import overview, spatial_eda, rastar_vector_data, visualization
from app_pages.nlp import ner
from transformers import pipeline

# Load the sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

st.set_page_config(page_title="Sabin Nepal Climate Analysis", page_icon="🌱", layout="wide")
st.title("Nepal Climate Trend Analysis and Predictions")
st.markdown("We analyse Nepal's climatic data and predict future trends.")

df = load_climate_data()
gdf = spatial_eda.load_vector()

# === SIDEBAR ===
st.sidebar.title("Main Navigation")
main_menu = st.sidebar.radio("Go to", ["🌍 Climate", "🌎 GIS", "🌦️ Weather"])

st.sidebar.markdown("---")
st.sidebar.title("🗣️ NLP Toolkit")
nlp_menu = st.sidebar.radio("Choose a tool", [
    "None", "Language Prediction", "Text Summarization", "NER Prediction", "Sentiment Analysis"
])

# ------------------------------------------
#          SECTION CONTROL LOGIC
# ------------------------------------------

# Priority: If NLP tool is selected, skip main
if nlp_menu != "None":
    main_menu = None  # Disable main menu output

# ------------------------------------------
#          NLP SECTION
# ------------------------------------------

if nlp_menu == "Language Prediction":
    st.title("🧠 Language Detection")
    user_input = st.text_area("Enter some text")
    if user_input:
        st.success("Detected Language: English")  # Placeholder logic

elif nlp_menu == "Text Summarization":
    st.title("📄 Text Summarization")

    # Text input for summarization
    text = st.text_area("Enter text for summarization")

    # Summarize button
    if st.button("Summarize Text"):
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        if text:
            # Run summarization
            summary = summarizer(text, max_length=150, min_length=30, do_sample=False)

            # Display the summary
            st.subheader("Summary:")
            st.write(summary[0]['summary_text'])
        else:
            st.warning("Please enter some text to summarize.")

elif nlp_menu == "NER Prediction":
    st.title("🧬 Named Entity Recognition (NER)")

    text = st.text_area("Enter text for NER tagging")

    if st.button("Run NER"):
        if text:
            entities = ner.english_ner(text)

            if entities:
                st.write("Entities Found:")
                for word, label in entities:
                    st.markdown(f"- **{word}** → {label}")
            else:
                st.info("No named entities found.")

        else:
            st.warning("Please enter some text...")

elif nlp_menu == "Sentiment Analysis":
    st.title("😊 Sentiment Analysis")

    # Text input for sentiment analysis
    text = st.text_area("Enter text for sentiment analysis")

    if st.button("Analyze Sentiment"):
        if text:
            # Run sentiment analysis
            sentiment = sentiment_analyzer(text)

            # Display the sentiment results
            st.subheader("Sentiment Results:")
            for result in sentiment:
                label = result['label']
                score = result['score']
                st.write(f"**Sentiment:** {label}")
                st.write(f"**Confidence Score:** {score:.2f}")
        else:
            st.warning("Please enter some text for sentiment analysis.")

# ------------------------------------------
#          MAIN SECTION (Climate/GIS)
# ------------------------------------------

elif main_menu == "🌍 Climate":
    st.title("🌍 Climate Data Analysis and Prediction")
    tab1, tab2, tab3, tab4 = st.tabs(
        ["📊 Data Exploration", "📈 EDA", "🤖 Model Creation", "🔮 Prediction & Visualization"]
    )
    with tab1:
        dataanalysis.show(df)
    with tab2:
        data_exploratoins.show(df)
    with tab3:
        train_model.show(df)
    with tab4:
        prediction.show(df)

elif main_menu == "🌎 GIS":
    st.title("🗺️ GIS Data Analysis for Nepal")
    tab1, tab2, tab3, tab4 = st.tabs([ "📋 Overview", "🌍 Spatial EDA", "🌐 Raster/Vector Data", "🗺️ Visualization"])
    with tab1:
        overview.show()
    with tab2:
        spatial_eda.check_basic_info(spatial_eda.load_vector())
    with tab3:
        rastar_vector_data.nepal_GIS(gdf)
        rastar_vector_data.visualize_raster_data()
    with tab4:
        visualization.plot_monthly_trend()


elif main_menu == "🌦️ Weather":
    st.title("🌦️ Real-time Weather Info")
    st.info("Weather dashboard coming soon...")
