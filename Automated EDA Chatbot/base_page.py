# 📄 base_page.py
import streamlit as st
import pandas as pd
import os
from eda_analysis import automated_eda
from ai_summary import generate_nlp_summary

class BaseAnalysisPage:
    def __init__(self, title, data_file, stats_file):
        self.title = title
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.DATA_FOLDER = os.path.join(self.BASE_DIR, "..", "data")
        self.DATA_ANALYSIS_FOLDER = os.path.join(self.BASE_DIR, "..", "data_analysis")
        
        self.DATA_PATH = os.path.join(self.DATA_FOLDER, data_file)
        self.STATS_PATH = os.path.join(self.DATA_ANALYSIS_FOLDER, stats_file)

    def load_data(self):
        """Loads the raw dataset and precomputed statistics."""
        if not os.path.exists(self.DATA_PATH) or not os.path.exists(self.STATS_PATH):
            st.error(f"Error: Missing required files! Ensure {self.DATA_PATH} and {self.STATS_PATH} exist.")
            return None, None

        df_data = pd.read_csv(self.DATA_PATH)
        df_stats = pd.read_csv(self.STATS_PATH)
        df_stats_cleaned = automated_eda(df_stats)

        return df_data, df_stats_cleaned

    def show_page(self):
        """Displays the analysis page."""
        st.title(self.title)

        df_data, df_stats_cleaned = self.load_data()

        if df_data is not None:
            # Generate AI Summary based on cleaned statistics
            #ai_summary = generate_nlp_summary(df_stats_cleaned.to_string())

            # Display AI-generated insights
            st.subheader(f"📋 AI-Generated EDA Summary ({self.title})")
            st.write("")

            # Display raw data overview
            st.subheader(f"📊 Raw Dataset Overview ({self.title})")
            st.write(df_data.head())

            # Display precomputed summary statistics (Cleaned)
            st.subheader(f"📈 Summary Statistics ({self.title})")
            st.dataframe(df_stats_cleaned, height=400, width=1000)
