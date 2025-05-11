import sys
import streamlit as st

sys.path.append("C:/My Computer/D DRIVE/Omdena/assignment/capstoneproject/capstone-project-sabinvankathmandu")

def show():
	st.header("Overview of GIS Data Analysis")
	st.markdown("""
        This section provides an overview of climate change impact assessment in Nepal based on raster datasets
        for precipitation and temperature from 2020 and projections for 2050.
        """)
	st.write(
        "Geographic Information Systems (GIS) are used to map and analyze geographical data. "
        "In this project, we analyze the spatial distribution of climate data in Nepal using GIS techniques."
    )

	st.subheader("Datasets Used")
	st.write("The following datasets are used for the analysis:")
	st.markdown("""
        - **Satellite Images**: For mapping temperature and precipitation variations.
        - **Elevation Data**: To understand the topography of Nepal and its impact on the climate.
        - **Climate Data**: Temperature, precipitation, and other climate parameters.
    """)
	