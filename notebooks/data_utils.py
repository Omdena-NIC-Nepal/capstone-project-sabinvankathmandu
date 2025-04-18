import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def load_data():
	"""
	Generate or load data / loading csv files
	"""
	path = "../data/dailyclimate.csv"
	df = pd.read_csv(path)

