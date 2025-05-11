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
 🔎 NER: spaCy

 📄 Summarization: facebook/bart-large-cnn

 😊 Sentiment: distilbert-base-uncased-finetuned-sst-2-english via HuggingFace Transformers

## ✍️ Author
 Sabin Bajracharya
 📍 Kathmandu → Amsterdam
🎓 MSc IT | 🌱 Omdena Climate Capstone Fellow


## 🧩 Project Structure
capstone-project-sabinvankathmandu/
ª   .gitignore
ª   app.py
ª   README.md
ª   requirements.txt
ª   structure.txt
ª
+---.github
ª       .keep
ª
+---app_pages
ª   ª   dataanalysis.py
ª   ª   data_exploratoins.py
ª   ª   prediction.py
ª   ª   train_model.py
ª   ª
ª   +---climate
ª   ª   ª   dataanalysis.cpython-312.pyc
ª   ª   ª   data_exploratoins.cpython-312.pyc
ª   ª   ª   prediction.cpython-312.pyc
ª   ª   ª   train_model.cpython-312.pyc
ª   ª   ª
ª   ª   +---__pycache__
ª   ª           overview.cpython-312.pyc
ª   ª
ª   +---gis
ª   ª   ª   overview.py
ª   ª   ª   rastar_vector_data.py
ª   ª   ª   spatial_eda.py
ª   ª   ª   visualization.py
ª   ª   ª
ª   ª   +---__pycache__
ª   ª           overview.cpython-312.pyc
ª   ª           rastar_vector_data.cpython-312.pyc
ª   ª           spatial_eda.cpython-312.pyc
ª   ª           visualization.cpython-312.pyc
ª   ª
ª   +---nlp
ª   ª   ª   ner.py
ª   ª   ª
ª   ª   +---__pycache__
ª   ª           ner.cpython-312.pyc
ª   ª
ª   +---__pycache__
ª           dataanalysis.cpython-312.pyc
ª           data_exploratoins.cpython-312.pyc
ª           prediction.cpython-312.pyc
ª           train_model.cpython-312.pyc
ª
+---data
ª   ª   yearly_climate_nepal.csv
ª   ª
ª   +---rastar
ª   ª   +---nepal_climate_data
ª   ª           metadata.json
ª   ª           nepal_admin_regions.gpkg
ª   ª           nepal_glaciers.gpkg
ª   ª           nepal_precipitation_2020.tif
ª   ª           nepal_precipitation_2050.tif
ª   ª           nepal_rivers.gpkg
ª   ª           nepal_temperature_2020.tif
ª   ª           nepal_temperature_2050.tif
ª   ª
ª   +---vector
ª       +---Shape_Data
ª               local_unit.dbf
ª               local_unit.prj
ª               local_unit.sbn
ª               local_unit.sbx
ª               local_unit.shp
ª               local_unit.shx
ª
+---model
ª       climate_model.pkl
ª
+---notebooks
ª       datautils_exploration.ipynb
ª
+---scripts
    +---climate
    ª   ª   data_utils.py
    ª   ª   eda_climate.py
    ª   ª   models.py
    ª   ª   prediction.py
    ª   ª   visualization.py
    ª   ª
    ª   +---__pycache__
    ª           data_utils.cpython-312.pyc
    ª           eda_climate.cpython-312.pyc
    ª           models.cpython-312.pyc
    ª           prediction.cpython-312.pyc
    ª
    +---gis
    ª       gis.py
    ª
    +---weather
