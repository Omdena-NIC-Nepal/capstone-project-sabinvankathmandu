from scripts.climate.eda_climate import *
import sys
import streamlit as st

sys.path.append(
    "C:/My Computer/D DRIVE/Omdena/assignment/capstoneproject/capstone-project-sabinvankathmandu"
)

def show(df):
    st.header(":blue[Data General Analysis]")
    st.subheader(
        "Dataset used in Nepal Climate Analysis - Rawdata before processing",
        divider="blue",
    )
    st.dataframe(df)

    # st.subheader("Check for null values", divider="blue")
    # st.write(check_null_values(df))
    st.subheader("Data after cleaning", divider="blue")
    st.write(handle_null_values(df))
    st.subheader("General Summary statistics", divider="blue")
    st.write(general_summary_statistics(df))
