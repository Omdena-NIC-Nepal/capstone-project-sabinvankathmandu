# 🌍 Nepal Climate Trend Analysis and NLP Toolkit

This Streamlit application provides a comprehensive platform for analyzing climate change trends in Nepal using GIS and Machine Learning techniques, alongside an integrated NLP toolkit for text-based insights.

---

## 📌 Features

### 🔬 Climate Data Analysis
- Load and explore historical climate datasets (Temperature and Precipitation)
- Perform Exploratory Data Analysis (EDA)
- Build predictive models for climate forecasting
- Visualize trends (monthly, yearly) and compare changes over time

### 🌐 GIS Data Processing
- Display and explore vector and raster datasets of Nepal (districts, provinces)
- Compare temperature and precipitation changes (2020 vs. 2050)
- Interactive GIS visualizations using Matplotlib and Streamlit

### 🗣️ Natural Language Processing (NLP) Toolkit
- **Language Detection** (placeholder logic for now)
- **Text Summarization** using `facebook/bart-large-cnn`
- **Named Entity Recognition (NER)** for English (Spacy-based)
- **Sentiment Analysis** using HuggingFace Transformers

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:Omdena-NIC-Nepal/capstone-project-sabinvankathmandu.git
   cd capstone-project-sabinvankathmandu.git


## 🛠️ Virtual Environment

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   	python -m venv venv
	source venv/bin/activate  # On Windows use `venv\Scripts\activate`

## 🛠️ Dependencies

3. Install the dependencies:
   ```bash
   	pip install -r requirements.txt

## 🛠️ Apploication

4. Run the Application
   ```bash
   	streamlit run app.py

## 🧠 Models Used
### 🔎 NER: spaCy

### 📄 Summarization: facebook/bart-large-cnn

### 😊 Sentiment: distilbert-base-uncased-finetuned-sst-2-english via HuggingFace Transformers

# ✍️ Author
## Sabin Bajracharya
## 📍 Kathmandu → Amsterdam
## 🎓 MSc IT | 🌱 Omdena Climate Capstone Fellow


nepal-climate-nlp/
│
├── app.py                         # Main Streamlit entry point
├── requirements.txt              # Required packages
├── scripts/
│   └── climate/
│       └── data_utils.py         # Data loading functions
├── app_pages/
│   ├── gis/
│   │   ├── overview.py
│   │   ├── spatial_eda.py
│   │   └── rastar_vector_data.py
│   ├── data_exploratoins.py
│   ├── dataanalysis.py
│   ├── train_model.py
│   ├── prediction.py
│   └── nlp/
│       ├── ner.py                # NER utilities
│       └── ...
└── assets/                       # Shapefiles, raster files, etc.
