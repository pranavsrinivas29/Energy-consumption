# 📄 app.py
import streamlit as st
from country_page import show_country_page
from continent_page import show_continent_page

# Set page title
st.set_page_config(page_title="AI-Powered EDA Generator", layout="wide")

# Sidebar Navigation
page = st.sidebar.selectbox("Select Analysis", ["🏠 Home", "📍 Country Data", "🌍 Continent Data"])

# Load the selected page
if page == "🏠 Home":
    st.title("📊 AI-Powered Automated EDA Report Generator")
    st.write("Use the sidebar to navigate between Country and Continent analysis.")

elif page == "📍 Country Data":
    show_country_page()

elif page == "🌍 Continent Data":
    show_continent_page()
